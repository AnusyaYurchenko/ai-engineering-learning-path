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

FAQ:
{faq_text}

Customer question:
{question}

Return only valid JSON with:
- answer
- source
- confidence

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
        return None


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
            result = {
                "question": question,
                "answer": data.get("answer", "I do not know based on the FAQ."),
                "source": data.get("source", "unknown"),
                "confidence": data.get("confidence", "low")
            }

            with open("interactive_faq_answer.json", "w", encoding="utf-8") as file:
                json.dump(result, file, indent=4)

            print("Interactive FAQ answer saved.")
        else:
            print("Failed to parse the AI response.")
    else:
        print("Gemini API key is missing.")


if __name__ == "__main__":
    main()
