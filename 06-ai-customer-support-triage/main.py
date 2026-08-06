import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def create_triage_prompt(message):
    return f"""
You are a customer support assistant.

Analyze this customer message and return JSON with:
- category: invoice, order, refund, complaint, or general
- confidence: high, medium, or low
- priority: high, medium, or low
- suggested_action: one short business action

Message:
{message}

Return only valid JSON.
Do not use markdown.
Do not use ```json.
Do not add explanation.
"""


def triage_with_gemini(client, message):
    prompt = create_triage_prompt(message)

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        result_text = response.text.strip()
        return result_text
    except Exception as error:
        print(f"Gemini API error for message: {message}")
        print(error)
        return None


def parse_ai_json(result_text):
    try:
        result = json.loads(result_text)
        return result
    except json.JSONDecodeError:
        return None


def create_triage_result(message, result):
    if result:
        return {
            "message": message,
            "category": result.get("category", "unknown"),
            "confidence": result.get("confidence", "unknown"),
            "priority": result.get("priority", "unknown"),
            "suggested_action": result.get("suggested_action", "Needs human review")
        }

    return {
        "message": message,
        "category": "unknown",
        "confidence": "low",
        "priority": "medium",
        "suggested_action": "Needs human review"
    }


def save_json_report(file_name, report):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)


def main():
    messages = [
        "I was charged twice and need a refund.",
        "Where is my package?",
        "Thank you for quick support.",
        "My order arrived damaged and I am angry."
    ]

    triage_results = []
    report_file = "ai_triage_report.json"

    if not api_key:
        print("API key is missing. Skipping classification.")
        return

    print("API key is loaded.")
    client = genai.Client(api_key=api_key)

    for message in messages:
        result_text = triage_with_gemini(client, message)
        result = parse_ai_json(result_text) if result_text else None

        if not result:
            print(f"Could not parse AI response for message: {message}")

        triage_results.append(create_triage_result(message, result))

    save_json_report(report_file, triage_results)
    print("AI triage report saved.")


if __name__ == "__main__":
    main()
