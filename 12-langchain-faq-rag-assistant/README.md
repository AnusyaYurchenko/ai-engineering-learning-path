# LangChain FAQ RAG Assistant

## Problem

A normal FAQ assistant can become expensive and unreliable when it sends the full FAQ file to the AI model every time.

This project improves the earlier FAQ assistant by using LangChain, embeddings, and vector search to retrieve only the most relevant FAQ sections before asking Gemini to answer.

## How It Works

The script reads a local FAQ file and customer questions from `questions.txt`.

For each run, it:

1. Loads the FAQ text.
2. Splits the FAQ into sections and chunks.
3. Creates embeddings for the chunks.
4. Stores the embeddings in an in-memory vector store.
5. Searches for the most relevant chunks for each question.
6. Sends only the retrieved context to Gemini through LangChain.
7. Saves structured answers to `rag_answers_report.json`.
8. Marks unknown or low-confidence answers for human review.

## Project Structure

```text
12-langchain-faq-rag-assistant/
├── README.md
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── faq.txt
├── questions.txt
└── rag_answers_report.json
```

## Setup

Install the required packages:

```powershell
pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

The script also supports `GEMINI_API_KEY` because earlier projects used that name.

## How To Run

```powershell
python main.py
```

## Example Output

```text
LangChain FAQ RAG report saved.
```

## Output File

The script creates:

```text
rag_answers_report.json
```

Example result:

```json
{
    "question": "When will I get my refund?",
    "answer": "Refunds are processed within 7 business days after approval.",
    "source": "Refunds",
    "confidence": "high",
    "retrieved_sources": [
        "Refunds",
        "Returns"
    ],
    "needs_human_review": false
}
```

## What I Learned

In this project, I practiced:

- using LangChain in a Python project
- using a local text file as a knowledge source
- splitting text into chunks
- creating embeddings with Gemini through LangChain
- storing chunks in an in-memory vector store
- semantic search with `similarity_search()`
- retrieval augmented generation logic
- using retrieved context in an AI prompt
- returning structured JSON from an AI model
- separating unknown answers for human review

## Business Value

This project shows how a business can answer customer questions from internal knowledge without sending every document to the AI model every time.

It is useful for FAQ bots, internal support tools, customer service automation, help desk routing, and knowledge base assistants.

## Documentation Used

This project follows current LangChain patterns for:

- `ChatGoogleGenerativeAI`
- `GoogleGenerativeAIEmbeddings`
- `RecursiveCharacterTextSplitter`
- `InMemoryVectorStore`

## Note

This is a beginner-friendly RAG project. In production, a business would usually use a persistent vector database, logging, tests, evaluation data, and access control.
