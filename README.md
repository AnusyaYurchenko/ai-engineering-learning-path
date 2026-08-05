# AI Engineering Learning Path

This repository contains my practical AI engineering portfolio projects.

The goal of this repository is to demonstrate my ability to build AI-powered applications with Python, LangChain, Large Language Models, API integrations, and automation tools.

## Projects

### 01 - AI Quiz Generator

A command-line AI application that generates beginner-level quiz content from a user-provided topic.

The application takes a topic as input and produces:

1. A beginner-level quiz question
2. A detailed answer with a clear explanation

Project folder: `01-quiz-generator/`

Main concepts demonstrated:

* Python command-line application development
* LangChain chain composition
* PromptTemplate
* LLMChain
* SequentialChain
* Google Gemini API integration
* Environment variable configuration
* API key security
* Git and GitHub project workflow

### 02 - Agentic Meal Planner

An AI-powered meal planning workflow that creates a weekly dinner plan based on user constraints such as budget, allergens, calorie target, number of people, number of days, and pantry ingredients.

The application drafts a meal plan, critiques it, revises it through an evaluation loop, and then generates a grocery shopping list.

Project folder: `02-agentic-meal-planner/`

Main concepts demonstrated:

* Prompt chaining
* Agentic workflow design
* JSON mode
* Structured output parsing
* Evaluation and revision loops
* Simple rate limiting with `MAX_PASSES`
* OpenAI API integration
* Python orchestration
* Grocery list generation

### 03 - Email Template Generator

A beginner-friendly business automation script that creates a personalized email from a reusable text template.

The script reads an email template, replaces placeholders with customer and order data, and writes the final email to a new text file.

Project folder: `03-email-template-generator/`

Main concepts demonstrated:

* Python functions
* Reading `.txt` files
* Writing `.txt` files
* String replacement with `.replace()`
* Simple business automation workflow
* Beginner-friendly project documentation

### 04 - GitHub User Report Generator

A beginner-friendly API automation script that collects public GitHub profile information for a list of usernames and writes a clean text report.

The script sends requests to the GitHub API, checks response status codes, converts JSON responses into Python dictionaries, and writes profile data to `github_users_report.txt`.

Project folder: `04-github-user-report-generator/`

Main concepts demonstrated:

* Working with APIs using `requests`
* API endpoints and status code checks
* JSON responses as Python dictionaries
* Python functions and loops
* Writing `.txt` report files
* Separating reusable helper functions from main script
* Basic error handling for missing users

### 05 - AI Email Draft Generator

A beginner-friendly AI automation script that generates a professional customer email draft from invoice data using the Gemini API.

The script reads a Gemini API key from `.env`, creates a reusable prompt from invoice data, sends the prompt to Gemini, and saves the generated email draft to `email_draft.txt`.

Project folder: `05-ai-email-draft-generator/`

Main concepts demonstrated:

* Gemini API integration with Python
* Environment variables and `.env` files
* API key protection with `.gitignore`
* Reusable prompt template functions
* Writing AI-generated text to `.txt` files
* Basic error handling with `try / except`

### 06 - Customer Message Classifier

A beginner-friendly business automation script that classifies customer messages into invoice, order, or general categories and creates a structured JSON report.

The script checks each message for important keywords, stores each classified message, counts how many messages belong to each category, and saves the full report to `message_classification_report.json`.

Project folder: `06-customer-message-classifier/`

Main concepts demonstrated:

* Python functions
* Lists and dictionaries
* Loops
* Keyword-based classification
* Counting category totals
* Saving structured JSON reports
* Practical customer support automation logic

### 07 - AI Message Classifier

A beginner-friendly AI automation script that reads customer names and messages from `messages.csv` and uses Gemini to classify each message into invoice, order, or general categories.

The script reads each CSV row as a dictionary, keeps the customer name connected to the message, sends each message to Gemini, counts category totals, and saves reports to both `ai_classification.json` and `ai_classification_report.csv`.

Project folder: `07-ai-message-classifier/`

Main concepts demonstrated:

* Gemini API integration with Python
* Prompt design for AI classification
* Reading input data from `.csv` files
* Using `csv.DictReader`
* Environment variables and `.env` files
* API key protection with `.gitignore`
* Python functions and loops
* Code organization with reusable helper functions
* Using a `main()` function
* Using `if __name__ == "__main__"`
* Keeping customer data connected to AI output
* Cleaning model output with `.strip().lower()`
* Counting category totals
* Saving AI classification results as JSON
* Writing AI results to CSV with `csv.DictWriter`
* Practical customer support automation logic

### 08 - AI Customer Support Triage

A beginner-friendly AI automation script that uses Gemini to triage customer support messages with category, confidence, priority, and suggested action.

The script asks Gemini to return structured JSON, converts the AI response into Python dictionaries, handles API or JSON parsing failures safely, and saves a full support triage report to `ai_triage_report.json`.

Project folder: `08-ai-customer-support-triage/`

Main concepts demonstrated:

* Gemini API integration with Python
* Structured prompt design
* JSON output from an AI model
* Converting JSON text with `json.loads()`
* API error handling with `try / except`
* Invalid JSON handling with `json.JSONDecodeError`
* Safe dictionary access with `.get()`
* Environment variables and `.env` files
* API key protection with `.gitignore`
* Saving AI triage reports as JSON
* Practical customer support automation logic

### 09 - Local FAQ AI Assistant

A beginner-friendly local-file AI assistant that answers customer questions using a local FAQ file as business context.

The project includes batch and interactive routing modes. Known FAQ answers are saved to `resolved_faq_answers.json`, and unknown answers are saved to `human_review_queue.json` for human review.

Project folder: `09-local-faq-ai-assistant/`

Main concepts demonstrated:

* Gemini API integration with Python
* Using a local file as AI context
* Reading `.txt` files
* Loading multiple customer questions from a file
* Prompt templates with FAQ context
* Looping through customer questions
* Using `input()` for interactive questions
* Asking AI for structured JSON output
* Converting JSON text with `json.loads()`
* Handling invalid JSON with `json.JSONDecodeError`
* Printing raw AI output for debugging
* Using `.get()` fallback values
* Adding a human-review flag for unknown answers
* Routing AI results into separate workflow files
* Saving AI answers as JSON
* Code organization with reusable functions
* Using a `main()` function
* Using `if __name__ == "__main__"`
* Beginner RAG-style thinking
* Practical FAQ automation logic

## Technical Focus

This portfolio is focused on:

* AI engineering
* Python development
* Large Language Model integration
* LangChain workflows
* Prompt engineering
* Secure API configuration
* Git and GitHub project organization
* Practical AI automation projects

## Repository Structure

ai-engineering-learning-path/

* README.md
* 01-quiz-generator/

  * README.md
  * quiz_generator.py
  * requirements.txt
  * .env.example
  * .gitignore

* 02-agentic-meal-planner/

  * README.md
  * agentic_meal_planner.py
  * requirements.txt
  * .env.example
  * .gitignore

* 03-email-template-generator/

  * README.md
  * main.py
  * email_template.txt
  * email_to_send.txt

* 04-github-user-report-generator/

  * README.md
  * main.py
  * helpers.py
  * requirements.txt
  * github_users_report.txt

* 05-ai-email-draft-generator/

  * README.md
  * main.py
  * requirements.txt
  * .env.example
  * .gitignore
  * email_draft.txt

* 06-customer-message-classifier/

  * README.md
  * main.py
  * .gitignore
  * message_classification_report.json

* 07-ai-message-classifier/

  * README.md
  * main.py
  * requirements.txt
  * .env.example
  * .gitignore
  * messages.csv
  * messages.txt
  * ai_classification.json
  * ai_classification_report.csv

* 08-ai-customer-support-triage/

  * README.md
  * main.py
  * requirements.txt
  * .env.example
  * .gitignore
  * ai_triage_report.json

* 09-local-faq-ai-assistant/

  * README.md
  * main.py
  * interactive_faq_assistant.py
  * requirements.txt
  * .env.example
  * .gitignore
  * faq.txt
  * questions.txt
  * human_review_queue.json
  * resolved_faq_answers.json

## Future Projects

Planned project areas:

* AI agents
* RAG applications
* Business automation tools
* AI assistants
* Workflow automation
* Cybersecurity-related AI tools
* AI portfolio applications

## Purpose

This repository is part of my transition into AI engineering.

It shows my practical progress through real projects, not only theory. Each project is structured to demonstrate a specific technical skill and can be expanded into more advanced applications in the future.
