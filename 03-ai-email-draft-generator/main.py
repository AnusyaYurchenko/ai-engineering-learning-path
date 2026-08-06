import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def create_invoice_prompt(invoice):
    return f"""
Write one polite follow-up email to {invoice['customer']} about an unpaid invoice of {invoice['total']} NOK.

Rules:
- Write only the email draft.
- Use [Invoice Number] as the invoice number placeholder.
- Use [Your Name] as the sender name placeholder.
- Do not give multiple options.
- Do not include tips.
- Keep it short and professional.
"""


def fill_email_placeholders(email_text, invoice, sender_name):
    email_text = email_text.replace("[Invoice Number]", invoice["invoice_number"])
    email_text = email_text.replace("[Your Name]", sender_name)
    return email_text


def main():
    invoice = {
        "customer": "Maria",
        "total": 300,
        "invoice_number": "INV-1001"
    }
    sender_name = "Ana"

    prompt = create_invoice_prompt(invoice)

    if not api_key:
        print("Gemini API key missing")
        return

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        final_email = fill_email_placeholders(response.text, invoice, sender_name)

        with open("email_draft.txt", "w", encoding="utf-8") as file:
            file.write(final_email)

        print("Email draft saved to email_draft.txt")

    except Exception as error:
        print("Could not generate email draft.")
        print(error)


if __name__ == "__main__":
    main()
