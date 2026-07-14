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
- Do not give multiple options.
- Do not include tips.
- Keep it short and professional.
"""


invoice = {
    "customer": "Maria",
    "total": 300
}

prompt = create_invoice_prompt(invoice)

if not api_key:
    print("Gemini API key missing")
else:
    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        with open("email_draft.txt", "w", encoding="utf-8") as file:
            file.write(response.text)

        print("Email draft saved to email_draft.txt")

    except Exception as error:
        print("Could not generate email draft.")
        print(error)
