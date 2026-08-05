# Local FAQ AI Assistant

## Problem

Businesses often answer the same customer questions many times: returns, shipping, invoices, and refunds.

This project shows how an AI assistant can answer customer questions using a local FAQ file as business context.

## What This Project Does

This project has two modes:

- `main.py` reads multiple customer questions from `questions.txt` and saves all answers to `faq_answers_report.json`.
- `interactive_faq_assistant.py` lets a user type one question in the terminal, asks Gemini for a structured JSON answer, and routes the result into the correct workflow file.

Both scripts use `faq.txt` as the local business knowledge file.

The AI is instructed to answer only from the FAQ. If the answer is not available in the FAQ, it should say:

```text
I do not know based on the FAQ.
```

If the source is `unknown`, Python marks the answer for human review and saves it to:

```text
human_review_queue.json
```

If the source is known, Python saves the answer to:

```text
resolved_faq_answers.json
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

Interactive routing mode with `interactive_faq_assistant.py`:

1. The script loads the Gemini API key from `.env`.
2. The FAQ content is loaded from `faq.txt`.
3. The user types one question in the terminal.
4. Gemini is asked to return only valid JSON with `answer`, `source`, and `confidence`.
5. Python converts the JSON text into a dictionary with `json.loads()`.
6. If JSON parsing fails, the script prints the raw AI answer for debugging.
7. The script uses `.get()` fallback values in case one key is missing.
8. Python adds `needs_human_review` based on whether the source is `unknown`.
9. The result is routed to `human_review_queue.json` or `resolved_faq_answers.json`.

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

The interactive routing script uses:

```text
load_text_file()
create_faq_prompt()
ask_gemini()
parse_ai_json()
save_json_file()
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
├── faq_answers_report.json
├── human_review_queue.json
└── resolved_faq_answers.json
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

Run interactive routing mode:

```powershell
python interactive_faq_assistant.py
```

## Example Output

Batch mode:

```text
FAQ answers report saved.
```

Interactive routing mode for an unknown answer:

```text
Ask a question: Do you offer birthday discounts?
Interactive FAQ answer saved to human_review_queue.json.
```

Interactive routing mode for a known answer:

```text
Ask a question: When will I get my refund?
Interactive FAQ answer saved to resolved_faq_answers.json.
```

## Output Files

Batch mode creates:

```text
faq_answers_report.json
```

Interactive routing mode creates one of these files:

```text
human_review_queue.json
resolved_faq_answers.json
```

Example human review result:

```json
{
    "question": "Do you offer birthday discounts?",
    "answer": "I do not know based on the FAQ.",
    "source": "unknown",
    "confidence": "low",
    "needs_human_review": true
}
```

Example resolved result:

```json
{
    "question": "When will I get my refund?",
    "answer": "Refunds are processed within 7 business days after approval.",
    "source": "Refunds",
    "confidence": "high",
    "needs_human_review": false
}
```

## What I Learned

In this project, I practiced:

- reading local `.txt` files with Python
- using a local file as AI context
- creating prompt templates with variables
- escaping literal JSON braces inside f-strings with `{{` and `}}`
- sending prompts to Gemini
- looping through multiple customer questions
- using `input()` for interactive terminal questions
- asking AI for structured JSON output
- converting JSON text with `json.loads()`
- handling invalid JSON with `json.JSONDecodeError`
- printing raw AI output for debugging
- using `.get()` fallback values for safer dictionary access
- adding a `needs_human_review` flag for unknown answers
- routing AI results into separate workflow files
- saving AI answers as JSON
- organizing code into reusable functions
- using a `main()` function
- protecting API keys with `.env` and `.gitignore`

## Business Value

This project is the beginner version of a local FAQ assistant with workflow routing.

A larger version could answer customer questions from company documents, help support teams respond faster, reduce repeated manual work, and route unknown answers to a human instead of guessing.
