# AI Engineering Learning Path

This repository contains my practical AI engineering and business automation portfolio projects.

The goal of this repository is to demonstrate my ability to build useful automation tools with Python, APIs, Large Language Models, Gemini API integrations, structured outputs, and clear project documentation.

## Projects

### 01 - Email Template Generator

A beginner-friendly business automation script that creates a personalized email from a reusable text template.

The script reads an email template, replaces placeholders with customer and order data, and writes the final email to a new text file.

Project folder: `01-email-template-generator/`

Main concepts demonstrated:

* Python functions
* Reading `.txt` files
* Writing `.txt` files
* String replacement with `.replace()`
* Simple business automation workflow
* Beginner-friendly project documentation

### 02 - GitHub User Report Generator

A beginner-friendly API automation script that collects public GitHub profile information for a list of usernames and writes a clean text report.

The script sends requests to the GitHub API, checks response status codes, converts JSON responses into Python dictionaries, and writes profile data to `github_users_report.txt`.

Project folder: `02-github-user-report-generator/`

Main concepts demonstrated:

* Working with APIs using `requests`
* API endpoints and status code checks
* JSON responses as Python dictionaries
* Python functions and loops
* Writing `.txt` report files
* Separating reusable helper functions from main script
* Basic error handling for missing users

### 03 - AI Email Draft Generator

A beginner-friendly AI automation script that generates a professional customer email draft from invoice data using the Gemini API.

The script reads a Gemini API key from `.env`, creates a reusable prompt from invoice data, sends the prompt to Gemini, and saves the generated email draft to `email_draft.txt`.

Project folder: `03-ai-email-draft-generator/`

Main concepts demonstrated:

* Gemini API integration with Python
* Environment variables and `.env` files
* API key protection with `.gitignore`
* Reusable prompt template functions
* Writing AI-generated text to `.txt` files
* Basic error handling with `try / except`

### 04 - Customer Message Classifier

A beginner-friendly business automation script that classifies customer messages into invoice, order, or general categories and creates a structured JSON report.

The script checks each message for important keywords, stores each classified message, counts how many messages belong to each category, and saves the full report to `message_classification_report.json`.

Project folder: `04-customer-message-classifier/`

Main concepts demonstrated:

* Python functions
* Lists and dictionaries
* Loops
* Keyword-based classification
* Counting category totals
* Saving structured JSON reports
* Practical customer support automation logic

### 05 - AI Message Classifier

A beginner-friendly AI automation script that reads customer names and messages from `messages.csv` and uses Gemini to classify each message into invoice, order, or general categories.

The script reads each CSV row as a dictionary, keeps the customer name connected to the message, sends each message to Gemini, counts category totals, and saves reports to both `ai_classification.json` and `ai_classification_report.csv`.

Project folder: `05-ai-message-classifier/`

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

### 06 - AI Customer Support Triage

A beginner-friendly AI automation script that uses Gemini to triage customer support messages with category, confidence, priority, and suggested action.

The script asks Gemini to return structured JSON, converts the AI response into Python dictionaries, handles API or JSON parsing failures safely, and saves a full support triage report to `ai_triage_report.json`.

Project folder: `06-ai-customer-support-triage/`

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

### 07 - Local FAQ AI Assistant

A beginner-friendly local-file AI assistant that answers customer questions using a local FAQ file as business context.

The project includes batch and interactive routing modes. Known FAQ answers are saved to `resolved_faq_answers.json`, and unknown answers are saved to `human_review_queue.json` for human review.

Project folder: `07-local-faq-ai-assistant/`

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

### 08 - Product Lookup API

A beginner-friendly API automation script that looks up product information from UPC barcode numbers and saves a structured product report.

The script sends UPC codes as API request parameters, checks whether the request worked, reads JSON data from the API response, extracts product title and brand, and saves the result to `product_lookup_report.json`.

Project folder: `08-product-lookup-api/`

Main concepts demonstrated:

* External API requests with `requests`
* Sending query parameters with `params=`
* Using `timeout=10` for safer API calls
* Checking API response status codes
* Reading JSON responses as Python dictionaries
* Working with nested API data
* Using `.get()` fallback values
* Saving API results as JSON
* Practical product data automation logic

### 09 - Weather API Report

A beginner-friendly API automation script that gets weather forecast data from OpenWeather and saves a structured weather report.

The script loads the API key from `.env`, sends city and unit parameters to the API, checks whether the request worked, reads nested forecast data, and saves a short report to `weather_report.json`.

Project folder: `09-weather-api-report/`

Main concepts demonstrated:

* External API requests with `requests`
* Protecting API keys with `.env`
* Loading environment variables with `python-dotenv`
* Sending query parameters with `params=`
* Using `timeout=10` for safer API calls
* Checking API response status codes
* Reading nested JSON forecast data
* Using `.get()` fallback values
* Saving API results as JSON
* Practical weather report automation logic

## Technical Focus

This portfolio is focused on:

* AI engineering
* Python development
* External API requests
* JSON and CSV report generation
* Large Language Model integration
* Gemini API usage
* Prompt engineering
* Structured AI outputs
* Secure API configuration
* Git and GitHub project organization
* Practical AI automation projects

## Repository Structure

```text
ai-engineering-learning-path/
├── README.md
├── 01-email-template-generator/
│   ├── README.md
│   ├── main.py
│   ├── email_template.txt
│   └── email_to_send.txt
├── 02-github-user-report-generator/
│   ├── README.md
│   ├── main.py
│   ├── helpers.py
│   ├── requirements.txt
│   └── github_users_report.txt
├── 03-ai-email-draft-generator/
│   ├── README.md
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   └── email_draft.txt
├── 04-customer-message-classifier/
│   ├── README.md
│   ├── main.py
│   ├── .gitignore
│   └── message_classification_report.json
├── 05-ai-message-classifier/
│   ├── README.md
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   ├── messages.csv
│   ├── messages.txt
│   ├── ai_classification.json
│   └── ai_classification_report.csv
├── 06-ai-customer-support-triage/
│   ├── README.md
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   └── ai_triage_report.json
├── 07-local-faq-ai-assistant/
│   ├── README.md
│   ├── main.py
│   ├── interactive_faq_assistant.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   ├── faq.txt
│   ├── questions.txt
│   ├── human_review_queue.json
│   └── resolved_faq_answers.json
├── 08-product-lookup-api/
│   ├── README.md
│   ├── main.py
│   ├── requirements.txt
│   ├── .gitignore
│   └── product_lookup_report.json
└── 09-weather-api-report/
    ├── README.md
    ├── main.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── weather_report.json
```

## Future Projects

Planned project areas:

* Web scraping reports
* Browser automation with Selenium
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