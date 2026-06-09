# AI Engineering Learning Path

This repository contains my practical AI engineering projects focused on building real applications with Python, LangChain, Large Language Models, and API integrations.

The goal of this repository is to demonstrate my progress, technical skills, and ability to build AI-powered tools that can be used in real-world workflows.

## About This Repository

This repository is organized as a growing portfolio of AI projects. Each project focuses on a specific AI engineering concept and includes source code, documentation, dependencies, and setup instructions.

Current focus areas:

* Python development
* LangChain applications
* Large Language Model integration
* Prompt engineering
* Chain composition
* API key management
* Secure environment configuration
* Git and GitHub workflow

## Projects

### 01 - AI Quiz Generator

A command-line AI application that generates educational quiz content from a user-provided topic.

The application takes a topic as input and produces:

1. A beginner-level quiz question
2. A detailed answer with a clear explanation

This project demonstrates how to build a multi-step AI workflow using LangChain chain composition.

## Technologies Used

* Python
* LangChain
* Google Gemini API
* PromptTemplate
* LLMChain
* SequentialChain
* python-dotenv
* Git
* GitHub

## Project Architecture

The AI Quiz Generator uses a sequential chain structure:

```text
topic -> question_chain -> question -> answer_chain -> answer
```

### Workflow

1. The user enters a topic.
2. The first chain generates a beginner-level quiz question.
3. The second chain receives the generated question.
4. The second chain generates a detailed answer and explanation.
5. The final output is displayed in the terminal.

## LangChain Components

### PromptTemplate

Used to define reusable prompt structures with input variables.

In this project, prompt templates are used for:

* generating a quiz question from a topic
* generating an answer from the quiz question

### LLMChain

Used to connect each prompt template with the Google Gemini language model.

The project includes two chains:

* `question_chain`
* `answer_chain`

### SequentialChain

Used to connect both chains and automatically pass data from the first chain to the second chain.

The output key from the first chain is used as the input for the second chain.

## Security

The project uses environment variables to protect the Google Gemini API key.

The real `.env` file is excluded from GitHub using `.gitignore`.

A sample `.env.example` file is included to show the required environment variable structure:

```text
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Go to the project folder

```bash
cd ai-engineering-learning-path/01-quiz-generator
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```bash
nano .env
```

Add the Gemini API key:

```text
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### 7. Run the application

```bash
python quiz_generator.py
```

## Example Use Case

Input topic:

```text
Python variables
```

Example output:

```text
Generated Question:
What is a variable in Python?

Generated Answer and Explanation:
A variable is a named place to store data. It allows a program to keep information and use it later.
```

## Skills Demonstrated

* Building command-line Python applications
* Working with virtual environments
* Managing project dependencies
* Using environment variables for sensitive data
* Integrating Google Gemini API
* Creating reusable prompt templates
* Building LangChain chains
* Connecting multiple chains with SequentialChain
* Structuring an AI project for GitHub
* Writing project documentation

## Future Improvements

* Add multiple quiz questions instead of one
* Add difficulty levels: beginner, intermediate, advanced
* Save generated quizzes to a file
* Add multiple-choice answers
* Add scoring for users
* Add a simple web interface
* Add project tests
* Improve error handling
