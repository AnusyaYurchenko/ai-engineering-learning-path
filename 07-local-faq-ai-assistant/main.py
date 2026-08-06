import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


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
    questions = load_questions("questions.txt")

    if not questions:
        print("No questions found.")
        return

    if api_key:
        client = genai.Client(api_key=api_key)

        resolved_answers = []
        human_review_queue = []

        for question in questions:
            prompt = create_faq_prompt(faq_text, question)
            answer = ask_gemini(client, prompt)
            data = parse_ai_json(answer) if answer else None
            result = create_result(question, data)

            if result["needs_human_review"]:
                human_review_queue.append(result)
            else:
                resolved_answers.append(result)

        save_json_file("resolved_faq_answers.json", resolved_answers)
        save_json_file("human_review_queue.json", human_review_queue)

        print("Resolved FAQ answers saved to resolved_faq_answers.json.")
        print("Human review queue saved to human_review_queue.json.")
    else:
        print("Gemini API key is missing.")


if __name__ == "__main__":
    main()
