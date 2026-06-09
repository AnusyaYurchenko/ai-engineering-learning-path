# AI Quiz Generator

AI Quiz Generator is a command-line Python application that creates beginner-level educational quiz content using LangChain and Google Gemini.

The project demonstrates a simple but practical AI workflow where one model chain generates a quiz question and another model chain generates the answer and explanation.

## Project Overview

The application asks the user to enter a topic.

Based on that topic, the program generates:

1. A beginner-level quiz question
2. A detailed answer
3. A simple explanation of the answer

Example topic:

`Python variables`

Example output:

Question:

`What is a variable in Python?`

Answer:

`A variable is a named place to store data. It allows a program to save information and use it later.`

## Problem This Project Solves

Creating educational content manually can take a lot of time.

This project shows how AI can support content creation by automatically generating quiz questions and explanations from a topic.

This type of workflow can be useful for:

* educational platforms
* online courses
* study assistants
* training materials
* internal company learning tools

## Technologies Used

* Python
* LangChain
* Google Gemini API
* python-dotenv
* PromptTemplate
* LLMChain
* SequentialChain

## Project Architecture

The application uses a sequential chain workflow:

`topic -> question_chain -> question -> answer_chain -> answer`

### Step 1: Question Generation

The first chain receives the user topic and generates one beginner-level quiz question.

Input:

`topic`

Output:

`question`

### Step 2: Answer Generation

The second chain receives the generated question and creates a detailed answer with an explanation.

Input:

`question`

Output:

`answer`

## LangChain Components

### PromptTemplate

Used to create reusable prompts with variables.

In this project, prompt templates are used for:

* creating a quiz question from a topic
* creating an answer from the generated question

### LLMChain

Used to connect a prompt template with the Gemini language model.

This project uses two LLMChain objects:

* `question_chain`
* `answer_chain`

### SequentialChain

Used to connect both chains together.

SequentialChain automatically passes the output from the first chain into the second chain.

## Security

The project uses a `.env` file to store the Google Gemini API key locally.

The real `.env` file is not uploaded to GitHub.

The repository includes `.env.example` to show the required environment variable format:

`GOOGLE_API_KEY=your_google_gemini_api_key_here`

## How to Run the Project

### 1. Go to the project folder

`cd 01-quiz-generator`

### 2. Create a virtual environment

`python3 -m venv venv`

### 3. Activate the virtual environment

`source venv/bin/activate`

### 4. Install dependencies

`pip install -r requirements.txt`

### 5. Create a .env file

`nano .env`

Add your Gemini API key:

`GOOGLE_API_KEY=your_google_gemini_api_key_here`

### 6. Run the application

`python quiz_generator.py`

### 7. Enter a topic

Example:

`Python variables`

The application will generate a quiz question and answer in the terminal.

## Skills Demonstrated

* Building a Python command-line application
* Creating and using a virtual environment
* Managing dependencies with requirements.txt
* Working with environment variables
* Protecting API keys
* Using Google Gemini API
* Creating reusable prompt templates
* Building LangChain chains
* Passing data between chains
* Organizing a project for GitHub

## Future Improvements

* Generate multiple quiz questions
* Add difficulty levels
* Add multiple-choice answers
* Save generated quizzes to a file
* Add scoring for users
* Add a simple web interface
* Improve error handling
* Add automated tests
