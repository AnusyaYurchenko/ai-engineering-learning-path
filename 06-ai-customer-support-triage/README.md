# AI Customer Support Triage

## Problem

Businesses often receive many customer support messages every day.

Some messages are simple, but others need faster attention, such as refunds, complaints, billing issues, or delivery problems.

Manually sorting these messages can take time and may cause urgent messages to be missed.

## What This Project Does

This project uses Gemini AI to analyze customer messages and create a support triage report.

For each message, the script returns:

- the original message
- category
- confidence
- priority
- suggested action

The script also includes basic reliability handling so failed or unclear AI responses do not disappear from the report.

## How It Works

1. The script loads the Gemini API key from `.env`.
2. A triage prompt is created for each customer message.
3. Gemini returns structured JSON.
4. Python tries to convert the JSON text into a dictionary with `json.loads()`.
5. If the API call fails, the script returns `None` instead of crashing.
6. If the AI returns invalid JSON, the script adds a safe fallback result.
7. If the AI forgets a field, `.get()` provides a default value.
8. The script saves all triage results to `ai_triage_report.json`.

## Project Structure

```text
08-ai-customer-support-triage/
├── main.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── ai_triage_report.json
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
API key is loaded.
AI triage report saved.
```

## Output File

The script creates:

```text
ai_triage_report.json
```

Example result:

```json
{
    "message": "I was charged twice and need a refund.",
    "category": "refund",
    "confidence": "high",
    "priority": "high",
    "suggested_action": "Verify transaction history and process a refund for the duplicate charge."
}
```

Fallback result if AI output cannot be parsed:

```json
{
    "message": "Customer message here",
    "category": "unknown",
    "confidence": "low",
    "priority": "medium",
    "suggested_action": "Needs human review"
}
```

## What I Learned

In this project, I practiced:

- using Gemini API with Python
- creating structured AI prompts
- asking AI to return JSON
- converting JSON text into a Python dictionary
- handling API errors with `try / except`
- handling invalid JSON with `json.JSONDecodeError`
- using `.get()` to protect against missing fields
- keeping failed messages in the final report
- using `.env` for API key safety
- saving AI results to a JSON report
- building a realistic customer support automation workflow

## Business Value

This project shows how AI can help a business organize customer support messages faster.

A larger version could route high-priority messages to support staff, send refund cases to billing, or prepare data for a customer support dashboard.

The reliability handling is important because real AI systems should not silently lose customer messages when an API call fails or the AI response is not perfectly formatted.
