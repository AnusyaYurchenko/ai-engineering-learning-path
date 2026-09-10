import json
import os

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

CHAT_MODEL = os.getenv("GEMINI_CHAT_MODEL", "gemini-2.5-flash")
EMBEDDING_MODEL = os.getenv("GEMINI_EMBEDDING_MODEL", "models/gemini-embedding-001")
RETRIEVAL_COUNT = 2

ANSWER_PROMPT = ChatPromptTemplate.from_template("""
You are a customer support assistant.

Use only the retrieved FAQ context to answer the customer question.
If the answer is not in the retrieved context, say: I do not know based on the FAQ.

Retrieved FAQ context:
{context}

Customer question:
{question}

Return only valid JSON.
Do not use markdown.

JSON format:
{{
    "answer": "...",
    "source": "...",
    "confidence": "..."
}}

Rules:
- source must be one FAQ section name from the retrieved context
- confidence must be high, medium, or low
- if the answer is not in the FAQ, use source: unknown and confidence: low
""")


def configure_api_key():
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    if api_key and not os.getenv("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = api_key

    return api_key


def load_text_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


def load_questions(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    questions = []

    for line in lines:
        question = line.strip()

        if question:
            questions.append(question)

    return questions


def create_faq_documents(faq_text):
    documents = []
    current_source = "General"
    current_lines = []

    for line in faq_text.splitlines():
        clean_line = line.strip()

        if not clean_line:
            continue

        if clean_line.endswith(":"):
            if current_lines:
                documents.append(Document(
                    page_content="\n".join(current_lines),
                    metadata={"source": current_source}
                ))

            current_source = clean_line[:-1]
            current_lines = []
        else:
            current_lines.append(clean_line)

    if current_lines:
        documents.append(Document(
            page_content="\n".join(current_lines),
            metadata={"source": current_source}
        ))

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=40
    )

    return splitter.split_documents(documents)


def create_vector_store(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    vector_store = InMemoryVectorStore(embedding=embeddings)
    vector_store.add_documents(chunks)

    return vector_store


def format_context(documents):
    context_parts = []

    for document in documents:
        source = document.metadata.get("source", "unknown")
        context_parts.append(f"Source: {source}\n{document.page_content}")

    return "\n\n".join(context_parts)


def get_unique_sources(documents):
    sources = []

    for document in documents:
        source = document.metadata.get("source", "unknown")

        if source not in sources:
            sources.append(source)

    return sources


def get_response_text(response):
    response_text = getattr(response, "text", None)

    if callable(response_text):
        return response_text()

    if isinstance(response_text, str):
        return response_text

    content = getattr(response, "content", "")

    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, dict):
                text_parts.append(block.get("text", ""))
            else:
                text_parts.append(str(block))

        return "".join(text_parts)

    return str(content)


def clean_json_text(text):
    lines = []

    for line in text.strip().splitlines():
        if not line.strip().startswith("```"):
            lines.append(line)

    return "\n".join(lines).strip()


def parse_ai_json(text):
    try:
        return json.loads(clean_json_text(text))
    except json.JSONDecodeError:
        return None


def answer_question(model, vector_store, question):
    retrieved_documents = vector_store.similarity_search(question, k=RETRIEVAL_COUNT)
    context = format_context(retrieved_documents)
    retrieved_sources = get_unique_sources(retrieved_documents)

    response = model.invoke(ANSWER_PROMPT.format_messages(
        context=context,
        question=question
    ))

    data = parse_ai_json(get_response_text(response))

    if not data:
        data = {
            "answer": "I do not know based on the FAQ.",
            "source": "unknown",
            "confidence": "low"
        }

    source = str(data.get("source", "unknown")).strip()
    confidence = str(data.get("confidence", "low")).strip().lower()

    return {
        "question": question,
        "answer": data.get("answer", "I do not know based on the FAQ."),
        "source": source,
        "confidence": confidence,
        "retrieved_sources": retrieved_sources,
        "needs_human_review": source.lower() == "unknown" or confidence == "low"
    }


def create_summary(answers):
    human_review_count = 0

    for answer in answers:
        if answer["needs_human_review"]:
            human_review_count += 1

    return {
        "total_questions": len(answers),
        "resolved_answers": len(answers) - human_review_count,
        "human_review_needed": human_review_count
    }


def save_json_report(file_name, report):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)


def main():
    api_key = configure_api_key()

    if not api_key:
        print("Google or Gemini API key is missing.")
        return

    faq_text = load_text_file("faq.txt")
    questions = load_questions("questions.txt")
    faq_documents = create_faq_documents(faq_text)
    chunks = split_documents(faq_documents)
    vector_store = create_vector_store(chunks)
    model = ChatGoogleGenerativeAI(model=CHAT_MODEL, temperature=0)

    answers = []

    for question in questions:
        answers.append(answer_question(model, vector_store, question))

    report = {
        "answers": answers,
        "summary": create_summary(answers)
    }

    save_json_report("rag_answers_report.json", report)

    print("LangChain FAQ RAG report saved.")


if __name__ == "__main__":
    main()
