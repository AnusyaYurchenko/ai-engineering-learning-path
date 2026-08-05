# Local FAQ AI Assistant

## Problem

Businesses often answer the same customer questions many times: returns, shipping, invoices, and refunds.

This project shows how an AI assistant can answer customer questions using a local FAQ file as business context.

## What This Project Does

The script reads a local FAQ from `faq.txt`, reads customer questions from `questions.txt`, sends each question to Gemini together with the FAQ context, and saves the answers to `faq_answers_report.json`.

The AI is instructed to answer only from the FAQ. If the answer is not available in the FAQ, it should say:

```text
I do not know based on the FAQ.
```

## How It Works

1. The script loads the Gemini API key from `.env`.
2. The FAQ content is loaded from `faq.txt`.
3. Customer questions are loaded from `questions.txt`.
4. Python cleans empty lines from the questions file.
5. A prompt is created for each question.
6. Gemini answers each question using the FAQ context.
7. The answers are saved to `faq_answers_report.json`.

## Code Structure

The code is organized into reusable functions:

```text
load_text_file()
load_questions()
create_faq_prompt()
ask_gemini()
save_json_report()
main()
```

The `main()` function controls the full workflow, and this block runs the project only when the file is executed directly:

```python
if __name__ == "__main__":
    main()
```

## Project Structure

```text
09-local-faq-ai-assistant/
├── main.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── faq.txt
├── questions.txt
└── faq_answers_report.json
```

## Setup

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_real_gemini_api_key_here
```

Do not upload your real `.env` file to GitHub.

## Input Files

The FAQ file is:

```text
faq.txt
```

Example FAQ content:

```text
Returns: Customers can return items within 14 days.
Shipping: Delivery usually takes 3-5 business days.
Invoices: Customers receive invoices by email.
Refunds: Refunds are processed within 7 business days after approval.
```

The questions file is:

```text
questions.txt
```

Example questions:

```text
When will I get my refund?
How long does delivery take?
Where can I find my invoice?
Can I return my order after 30 days?
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
FAQ answers report saved.
```

## Output File

The script creates:

```text
faq_answers_report.json
```

Example result:

```json
[
    {
        "question": "When will I get my refund?",
        "answer": "Refunds are processed within 7 business days after approval."
    },
    {
        "question": "Can I return my order after 30 days?",
        "answer": "I do not know based on the FAQ."
    }
]
```

## What I Learned

In this project, I practiced:

- reading local `.txt` files with Python
- using a local file as AI context
- creating prompt templates with variables
- sending prompts to Gemini
- looping through multiple customer questions
- saving AI answers as JSON
- organizing code into reusable functions
- using a `main()` function
- protecting API keys with `.env` and `.gitignore`

## Business Value

This project is the beginner version of a local FAQ assistant.

A larger version could answer customer questions from company documents, help support teams respond faster, reduce repeated manual work, and become the base for a future document Q&A or RAG-style assistant.
