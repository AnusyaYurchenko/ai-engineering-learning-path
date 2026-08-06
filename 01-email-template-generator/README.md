# Email Template Generator

## Problem

Businesses often need to send similar emails to many customers.

Writing each email manually takes time and can lead to mistakes. This project automates a small part of that work by using an email template with placeholders.

## How It Works

The project reads an email template from `email_template.txt`.

The template contains placeholders:

```text
CUSTOMER_NAME
ORDER_ID
```

The Python script replaces those placeholders with real customer data.

Then it saves the final email into `email_to_send.txt`.

## Project Files

```text
01-email-template-generator/
    main.py
    email_template.txt
    email_to_send.txt
    README.md
```

## How To Run

1. Open the project folder in the terminal.
2. Make sure `email_template.txt` contains this text:

```text
Hello CUSTOMER_NAME, your order ORDER_ID is ready.
```

3. Run the Python script:

```bash
python main.py
```

4. Open `email_to_send.txt` to see the generated email.

## Example Input

`email_template.txt`

```text
Hello CUSTOMER_NAME, your order ORDER_ID is ready.
```

## Example Output

`email_to_send.txt`

```text
Hello Ana, your order A1001 is ready.
```

## What I Learned

In this project, I practiced:

- reading text from a `.txt` file
- replacing placeholders with real data
- writing processed text into a new file
- creating a reusable Python function
- organizing a small project for GitHub
- explaining a project with a `README.md`

## Future Improvements

Possible future improvements:

- ask the user for customer name and order ID with `input()`
- generate emails for many customers
- read customer data from a CSV file
- create different templates for orders, invoices, and follow-ups
