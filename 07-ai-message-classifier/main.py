import os
import json
import csv
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


def load_messages_from_csv(file_name):
    messages = []

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            messages.append({
                "customer": row["customer"],
                "message": row["message"]
            })

    return messages


messages = load_messages_from_csv("messages.csv")
classified_messages = []

category_counts = {
    "invoice": 0,
    "order": 0,
    "general": 0
}

if api_key:
    print("Gemini API key is loaded.")

    client = genai.Client(api_key=api_key)

    for item in messages:
        category = classify_with_gemini(client, item["message"])

        classified_messages.append({
            "customer": item["customer"],
            "message": item["message"],
            "category": category
        })

        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts["general"] += 1

    report = {
        "classified_messages": classified_messages,
        "category_counts": category_counts
    }

    file_name = "ai_classification.json"

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"{file_name} created successfully.")
else:
    print("Gemini API key is missing.")
