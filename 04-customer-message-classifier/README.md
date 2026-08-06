# Customer Message Classifier

## Problem

Businesses often receive many customer messages. It can take time to sort them manually.

This project classifies customer messages into simple categories:

- invoice
- order
- general

## How It Works

The script checks each customer message for important keywords.

Examples:

- Messages with `invoice`, `receipt`, or `bill` are classified as `invoice`.
- Messages with `order` or `package` are classified as `order`.
- Other messages are classified as `general`.

The script creates a JSON report with:

- each message and its category
- total count for each category

## How To Run

```powershell
python main.py
```

## Example Output

```text
Message classification report saved.
```

## Output File

The script creates:

```text
message_classification_report.json
```

## What I Learned

In this project, I practiced:

- functions
- loops
- dictionaries
- lists
- keyword-based classification
- counting categories
- saving reports as JSON
