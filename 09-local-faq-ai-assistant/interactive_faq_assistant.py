import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def load_text_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


def create_faq_prompt(faq_text, question):
    return f"""
Use only this FAQ to answer the customer question.
If the answer is not in the FAQ, say: I do not know based on the FAQ.

FAQ:
{faq_text}

Customer question:
{question}

Return one short and clear answer.
"""


def ask_gemini(client, prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        answer = response.text.strip()
        return answer

    except Exception as error:
        print("Gemini API error.")
        print(error)
        return "Could not generate answer."


def main():
    faq_text = load_text_file("faq.txt")
    question = input("Ask a question: ")

    if not question.strip():
        print("No question provided.")
        return

    if api_key:
        client = genai.Client(api_key=api_key)

        prompt = create_faq_prompt(faq_text, question)
        answer = ask_gemini(client, prompt)

        print(answer)
    else:
        print("Gemini API key is missing.")


if __name__ == "__main__":
    main()
