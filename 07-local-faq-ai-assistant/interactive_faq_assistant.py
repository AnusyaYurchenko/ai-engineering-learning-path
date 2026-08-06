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
        return "Could not generate answer."


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


def main():
    faq_text = load_text_file("faq.txt")
    question = input("Ask a question: ")

    if not question.strip():
        print("No question provided.")
        return

    if api_key:
        client = genai.Client(api_key=api_key)

        prompt = create_faq_prompt(faq_text, question)
        answer = ask_gemini(client, prompt)
        data = parse_ai_json(answer)

        if data:
            source = data.get("source", "unknown")
            needs_human_review = source.lower() == "unknown"

            result = {
                "question": question,
                "answer": data.get("answer", "I do not know based on the FAQ."),
                "source": source,
                "confidence": data.get("confidence", "low"),
                "needs_human_review": needs_human_review
            }

            if result["needs_human_review"]:
                output_file = "human_review_queue.json"
            else:
                output_file = "resolved_faq_answers.json"

            save_json_file(output_file, [result])

            print(f"Interactive FAQ answer saved to {output_file}.")
        else:
            print("Failed to parse the AI response.")
    else:
        print("Gemini API key is missing.")


if __name__ == "__main__":
    main()
