# AI Email Draft Generator

## Problem

Small businesses often need to write similar customer emails, such as unpaid invoice reminders. Writing these messages manually can take time and lead to inconsistent communication.

This project uses Python and the Gemini API to generate a polite email draft from invoice data.

## What This Script Does

The script:

1. Loads a Gemini API key from a `.env` file
2. Creates an invoice prompt using customer data
3. Sends the prompt to Gemini
4. Saves the generated email draft to `email_draft.txt`

## Project Structure

```text
ai-email-draft-generator/
  main.py
  .env
  .env.example
  .gitignore
  requirements.txt
  README.md
  email_draft.txt
```

## Setup

Install the required packages:

```powershell
pip install -r requirements.txt
```

Create a file called `.env`:

```text
GEMINI_API_KEY=your-real-gemini-api-key
```

Important: `.env` contains the real API key and should not be uploaded to GitHub.

Create a file called `.env.example`:

```text
GEMINI_API_KEY=your-gemini-api-key-here
```

This file shows which environment variable the project needs.

## How To Run

Run the script:

```powershell
python main.py
```

Read the generated email draft:

```powershell
Get-Content email_draft.txt -Encoding UTF8
```

## Example Output

```text
Subject: Follow-up: Invoice [Invoice Number]

Hi Maria,

I hope you're having a good week.

I am writing to kindly follow up on the status of invoice [Invoice Number] for 300 NOK.

Best regards,

[Your Name]
```

## What I Learned

```text
- How to read secrets from a .env file
- How to protect API keys with .gitignore
- How to use the Gemini API from Python
- How to create reusable prompt templates
- How to save AI-generated output to a text file
- How to handle API errors with try / except
```

## Business Value

```text
This script can help a small business quickly create professional customer email drafts.

It reduces repetitive writing work and makes customer communication more consistent.
```
