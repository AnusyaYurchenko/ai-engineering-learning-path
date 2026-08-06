import json


def classify_message(message):
    lower_message = message.lower()

    if "invoice" in lower_message or "receipt" in lower_message or "bill" in lower_message:
        return "invoice"
    elif "order" in lower_message or "package" in lower_message:
        return "order"
    else:
        return "general"


messages = [
    "I need help with my invoice.",
    "Where is my order?",
    "Thanks for your help.",
    "Please send my receipt.",
    "My package has not arrived.",
    "I cannot pay my bill."
]

classified_messages = []

category_counts = {
    "invoice": 0,
    "order": 0,
    "general": 0
}

for message in messages:
    category = classify_message(message)
    classified_messages.append({"message": message, "category": category})
    category_counts[category] += 1

report = {
    "classified_messages": classified_messages,
    "category_counts": category_counts
}

with open("message_classification_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("Message classification report saved.")
