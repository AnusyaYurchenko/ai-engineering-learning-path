# AI Message Classifier

## Problem

Businesses often receive customer messages about invoices, orders, delivery, payments, and general questions.

Sorting these messages manually can take time. This project uses Gemini AI to classify customer messages automatically.

## What This Project Does

The script sends customer messages to Gemini and asks the model to classify each message into one category:

- invoice
- order
- general

The script then saves the AI classification results to a JSON file.

## How It Works

1. The script loads the Gemini API key from `.env`.
2. A prompt is created for each customer message.
3. Gemini classifies the message.
4. Python cleans the AI response with `.strip().lower()`.
5. The result is saved to `ai_classification.json`.

## Project Structure

```text
07-ai-message-classifier/
├── main.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── ai_classification.json
```

## Setup

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_real_gemini_api_key_here
```

Do not upload your real `.env` file to GitHub.

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
```

## Output File

The script creates:

```text
ai_classification.json
```

Example JSON result:

```json
[
    {
        "message": "I was charged twice.",
        "category": "invoice"
    },
    {
        "message": "Where is my package?",
        "category": "order"
    },
    {
        "message": "Thank you for quick support.",
        "category": "general"
    }
]
```

## What I Learned

In this project, I practiced:

- creating prompts for AI classification
- using Gemini API with Python
- loading API keys from `.env`
- protecting secrets with `.gitignore`
- using functions for reusable code
- looping through customer messages
- cleaning AI output with `.strip().lower()`
- saving AI results as JSON

## Business Value

This project shows how AI can help a business sort customer messages faster.

A larger version could be used to route messages to the correct team, create support reports, or prepare data for a customer service dashboard.
