import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def create_classification_prompt(message):
    return f"""
Classify this customer message into one category:
invoice, order, or general.

Category rules:
- invoice: payment, receipt, bill, charged, refund, or invoice questions
- order: order status, delivery, package, shipping, tracking, or product arrival questions
- general: greetings, thanks, or other messages

Message:
{message}

Return only the category name.
"""


def classify_with_gemini(client, message):
    prompt = create_classification_prompt(message)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    category = response.text.strip().lower()
    return category


messages = [
    "I was charged twice.",
    "Where is my package?",
    "Thank you for quick support."
]

classified_messages = []

if api_key:
    print("Gemini API key is loaded.")

    client = genai.Client(api_key=api_key)

    for message in messages:
        category = classify_with_gemini(client, message)

        classified_messages.append({
            "message": message,
            "category": category
        })

    file_name = "ai_classification.json"

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(classified_messages, file, indent=4)

    print(f"{file_name} created successfully.")
else:
    print("Gemini API key is missing.")
