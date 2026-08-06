# GitHub User Report Generator

## Problem

Businesses and teams sometimes need to collect basic public profile information from GitHub users. Doing this manually is slow if there are many usernames to check.

This script automates that task by getting public GitHub user data from the GitHub API and creating a clean text report.

## How It Works

The project uses two Python files:

- `main.py` controls the script.
- `helpers.py` stores reusable functions.

The script follows this automation pattern:

```text
list of usernames -> API request -> JSON data -> text report
```

For each username, the script:

1. Builds a GitHub API URL.
2. Sends a request with `requests.get()`.
3. Uses a timeout so the request does not hang forever.
4. Handles connection errors safely with `try / except`.
5. Checks if the response status code is `200`.
6. Converts the JSON response into a Python dictionary.
7. Writes the user data into `github_users_report.txt`.
8. Writes a safe error message if the user does not exist or the request fails.

## Project Files

```text
02-github-user-report-generator/
  main.py
  helpers.py
  requirements.txt
  github_users_report.txt
  README.md
```

## How To Run

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate
```

Install the required package:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python main.py
```

## Example Console Output

```text
Report generated: github_users_report.txt
```

## Example Report Output

```text
GitHub Users Report

Username: github
Public repos: 554
Profile URL: https://github.com/github

Username: octocat
Public repos: 8
Profile URL: https://github.com/octocat

Username: AnusyaYurchenko
Public repos: 8
Profile URL: https://github.com/AnusyaYurchenko

Could not get data for fake-user-123456789.
```

## What I Learned

In this project, I practiced:

- Using APIs with Python
- Installing and using the `requests` package
- Building API URLs with f-strings
- Checking API status codes
- Using request timeouts
- Handling request errors safely
- Converting JSON responses into Python dictionaries
- Using functions to organize code
- Looping through a list of usernames
- Writing a clean `.txt` report file
- Handling missing or invalid API data safely
- Separating reusable logic into `helpers.py`

## Future Improvements

Possible next steps:

- Read usernames from a CSV file
- Save the report as CSV or JSON
- Add user input for custom usernames
- Add better error messages for API limits or connection problems
- Turn the script into a small command-line tool
