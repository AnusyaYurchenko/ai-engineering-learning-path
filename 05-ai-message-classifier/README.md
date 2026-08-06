# AI Message Classifier

## Problem

Businesses often receive customer messages about invoices, orders, delivery, payments, and general questions.

Sorting these messages manually can take time. This project uses Gemini AI to classify customer messages automatically.

## What This Project Does

The script reads customer messages from a CSV file, sends each message to Gemini, and asks the model to classify each message into one category:

- invoice
- order
- general

The script keeps the customer name connected to each message and saves the results in two formats:

- JSON for apps, APIs, and automation systems
- CSV for Excel, Google Sheets, and business reports

## How It Works

1. The script loads the Gemini API key from `.env`.
2. Customer names and messages are loaded from `messages.csv`.
3. Each CSV row is read as a dictionary with `csv.DictReader`.
4. A prompt is created for each customer message.
5. Gemini classifies the message.
6. Python cleans the AI response with `.strip().lower()`.
7. If the Gemini request fails or returns an unexpected category, Python uses a safe fallback.
8. The script counts how many messages are in each category.
9. The final JSON report is saved to `ai_classification.json`.
10. A spreadsheet-friendly CSV report is saved to `ai_classification_report.csv`.

## Code Structure

The code is organized into reusable functions:

```text
create_classification_prompt()
classify_with_gemini()
load_messages_from_csv()
classify_messages()
save_json_report()
save_csv_report()
main()
```

The `main()` function controls the full workflow, and this block runs the project only when the file is executed directly:

```python
if __name__ == "__main__":
    main()
```

## Project Structure

```text
05-ai-message-classifier/
├── main.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── messages.csv
├── messages.txt
├── ai_classification.json
└── ai_classification_report.csv
```

## Setup

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_real_gemini_api_key_here
```

Do not upload your real `.env` file to GitHub.

## Input File

Add customer messages to:

```text
messages.csv
```

The CSV should contain two columns:

```csv
customer,message
Maria,I was charged twice and need a refund.
Ana,Where is my package?
Sara,Thank you for quick support.
Emma,My order arrived damaged and I am angry.
```

## Install Dependencies

```powershell
pip install -r requirements.txt
```

## How To Run

```powershell
python main.py
```

## Example Output

```text
Gemini API key is loaded.
ai_classification.json created successfully.
ai_classification_report.csv created successfully.
```

## Output Files

The script creates:

```text
ai_classification.json
ai_classification_report.csv
```

Example JSON result:

```json
{
    "classified_messages": [
        {
            "customer": "Maria",
            "message": "I was charged twice and need a refund.",
            "category": "invoice"
        },
        {
            "customer": "Ana",
            "message": "Where is my package?",
            "category": "order"
        }
    ],
    "category_counts": {
        "invoice": 1,
        "order": 1,
        "general": 0
    }
}
```

Example CSV result:

```csv
customer,message,category
Maria,I was charged twice and need a refund.,invoice
Ana,Where is my package?,order
Sara,Thank you for quick support.,general
Emma,My order arrived damaged and I am angry.,order
```

## What I Learned

In this project, I practiced:

- creating prompts for AI classification
- using Gemini API with Python
- loading API keys from `.env`
- protecting secrets with `.gitignore`
- reading input data from a `.csv` file
- using `csv.DictReader` to read rows as dictionaries
- keeping customer names connected to messages
- organizing code into reusable functions
- using a `main()` function
- using `if __name__ == "__main__"`
- looping through customer records
- cleaning AI output with `.strip().lower()`
- counting category totals
- saving structured AI results as JSON
- writing AI results to CSV with `csv.DictWriter`
- adding safe fallback behavior for unexpected AI output

## Business Value

This project shows how AI can help a business sort customer messages faster.

A larger version could read real support messages from a spreadsheet export, classify them, route messages to the correct team, create support reports, or prepare data for a customer service dashboard.
