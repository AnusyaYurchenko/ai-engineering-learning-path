import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def load_text_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


def create_faq_prompt(faq_text, question):
    return f"""
Use only this FAQ to answer the customer question.
If the answer is not in the FAQ, say: I do not know based on the FAQ.

FAQ:
{faq_text}

Customer question:
{question}

Return only valid JSON.
Do not use markdown.
Do not use ```json.
Do not add explanation.

JSON format:
{{
    "answer": "...",
    "source": "...",
    "confidence": "..."
}}

Rules:
- source should be the FAQ section name: Returns, Shipping, Invoices, or Refunds
- confidence should be high, medium, or low
- if the answer is not in the FAQ, use:
  - answer: I do not know based on the FAQ.
  - source: unknown
  - confidence: low
"""


def ask_gemini(client, prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        answer = response.text.strip()
        return answer

    except Exception as error:
        print(f"API error occurred while asking Gemini: {error}")
        return None


def parse_ai_json(answer):
    try:
        data = json.loads(answer)
        return data
    except json.JSONDecodeError as error:
        print(f"JSON parsing error: {error}")
        print("Raw AI answer:")
        print(answer)
        return None


def save_json_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json_list(file_name):
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        return []

    if isinstance(data, list):
        return data

    return []


def append_json_result(file_name, result):
    existing_results = load_json_list(file_name)
    existing_results.append(result)
    save_json_file(file_name, existing_results)


def create_result(question, data):
    if data:
        source = data.get("source", "unknown")

        return {
            "question": question,
            "answer": data.get("answer", "I do not know based on the FAQ."),
            "source": source,
            "confidence": data.get("confidence", "low"),
            "needs_human_review": source.lower() == "unknown"
        }

    return {
        "question": question,
        "answer": "Could not generate or parse answer.",
        "source": "unknown",
        "confidence": "low",
        "needs_human_review": True
    }


def main():
    faq_text = load_text_file("faq.txt")
    question = input("Ask a question: ")

    if not question.strip():
        print("No question provided.")
        return

    if not api_key:
        print("Gemini API key is missing.")
        return

    client = genai.Client(api_key=api_key)

    prompt = create_faq_prompt(faq_text, question)
    answer = ask_gemini(client, prompt)
    data = parse_ai_json(answer) if answer else None
    result = create_result(question, data)

    if result["needs_human_review"]:
        output_file = "human_review_queue.json"
    else:
        output_file = "resolved_faq_answers.json"

    append_json_result(output_file, result)

    print(f"Interactive FAQ answer saved to {output_file}.")


if __name__ == "__main__":
    main()
