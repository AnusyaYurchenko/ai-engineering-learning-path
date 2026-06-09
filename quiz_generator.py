import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.llm import LLMChain
from langchain_classic.chains.sequential import SequentialChain


# Load variables from .env file
load_dotenv()

# Check if API key exists
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY was not found. Please add it to your .env file.")


# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)


# First prompt: create a beginner-level quiz question
question_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
You are an educational quiz creator.

Create one beginner-level quiz question about the topic: {topic}

Rules:
- The question must be clear.
- The question must be suitable for beginners.
- Return only the question.
"""
)


# Second prompt: answer the generated question
answer_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful teacher.

Answer the following quiz question and explain the answer in simple words.

Question: {question}

Rules:
- Give the correct answer first.
- Then give a beginner-friendly explanation.
- Keep the explanation clear and educational.
"""
)


# Chain 1: topic -> question
question_chain = LLMChain(
    llm=llm,
    prompt=question_prompt,
    output_key="question"
)


# Chain 2: question -> answer
answer_chain = LLMChain(
    llm=llm,
    prompt=answer_prompt,
    output_key="answer"
)


# Sequential chain: connects both chains
quiz_chain = SequentialChain(
    chains=[question_chain, answer_chain],
    input_variables=["topic"],
    output_variables=["question", "answer"],
    verbose=True
)


# Ask user for topic
topic = input("Enter a quiz topic: ")

# Run the full chain
result = quiz_chain.invoke({"topic": topic})


# Display results
print("\nGenerated Question:")
print(result["question"])

print("\nGenerated Answer and Explanation:")
print(result["answer"])
