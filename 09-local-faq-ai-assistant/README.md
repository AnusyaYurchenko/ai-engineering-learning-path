# Local FAQ AI Assistant

## Problem

Businesses often answer the same customer questions many times: returns, shipping, invoices, and refunds.

This project shows how an AI assistant can answer customer questions using a local FAQ file as business context.

## What This Project Does

This project has two modes:

- `main.py` reads multiple customer questions from `questions.txt` and saves all answers to `faq_answers_report.json`.
- `interactive_faq_assistant.py` lets a user type one question in the terminal and prints the answer immediately.

Both scripts use `faq.txt` as the local business knowledge file.

The AI is instructed to answer only from the FAQ. If the answer is not available in the FAQ, it should say:

```text
I do not know based on the FAQ.
```

## How It Works

Batch mode with `main.py`:

1. The script loads the Gemini API key from `.env`.
2. The FAQ content is loaded from `faq.txt`.
3. Customer questions are loaded from `questions.txt`.
4. Python cleans empty lines from the questions file.
5. A prompt is created for each question.
6. Gemini answers each question using the FAQ context.
7. The answers are saved to `faq_answers_report.json`.

Interactive mode with `interactive_faq_assistant.py`:

1. The script loads the Gemini API key from `.env`.
2. The FAQ content is loaded from `faq.txt`.
3. The user types one question in the terminal.
4. Gemini answers using the FAQ context.
5. The answer is printed in the terminal.

## Code Structure

The batch script is organized into reusable functions:

```text
load_text_file()
load_questions()
create_faq_prompt()
ask_gemini()
save_json_report()
main()
```

The interactive script reuses the same basic pattern:

```text
load_text_file()
create_faq_prompt()
ask_gemini()
main()
```

The `main()` function controls the workflow, and this block runs each script only when the file is executed directly:

```python
if __name__ == "__main__":
    main()
```

## Project Structure

```text
09-local-faq-ai-assistant/
├── main.py
├── interactive_faq_assistant.py
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

The batch questions file is:

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

Run batch mode:

```powershell
python main.py
```

Run interactive mode:

```powershell
python interactive_faq_assistant.py
```

## Example Output

Batch mode:

```text
FAQ answers report saved.
```

Interactive mode:

```text
Ask a question: When will I get my refund?
Refunds are processed within 7 business days after approval.
```

## Output File

Batch mode creates:

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
- using `input()` for interactive terminal questions
- saving AI answers as JSON
- organizing code into reusable functions
- using a `main()` function
- protecting API keys with `.env` and `.gitignore`

## Business Value

This project is the beginner version of a local FAQ assistant.

A larger version could answer customer questions from company documents, help support teams respond faster, reduce repeated manual work, and become the base for a future document Q&A or RAG-style assistant.
