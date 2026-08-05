import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def load_text_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()


def load_questions(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    questions = []

    for line in lines:
        question = line.strip()

        if question:
            questions.append(question)

    return questions


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
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    answer = response.text.strip()
    return answer


def save_json_report(file_name, report):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)


def main():
    faq_text = load_text_file("faq.txt")
    questions = load_questions("questions.txt")
    file_name = "faq_answers_report.json"

    if api_key:
        client = genai.Client(api_key=api_key)

        answers_report = []

        for question in questions:
            prompt = create_faq_prompt(faq_text, question)
            answer = ask_gemini(client, prompt)

            answers_report.append({
                "question": question,
                "answer": answer
            })

        save_json_report(file_name, answers_report)

        print("FAQ answers report saved.")
    else:
        print("Gemini API key is missing.")


if __name__ == "__main__":
    main()
