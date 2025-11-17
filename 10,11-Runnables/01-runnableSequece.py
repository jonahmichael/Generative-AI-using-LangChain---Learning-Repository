# 1. RunnaleSequence: This Runnable allows you to chain together multiple Runnables in a sequence.
# It takes a list of Runnables as input and executes them one after the other, passing the output of one Runnable as the input to the next.
# This is useful for creating complex workflows that involve multiple steps, such as data preprocessing, model inference, and post-processing.

# R1 -> R2 -> R3 -> ... -> Rn

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt=PromptTemplate(
    template="write a joke on the topic '{topic}'",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Explain this joke to a 5 year old: {joke}",
    input_variables=["joke"])

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)

parser= StrOutputParser()

chain = RunnableSequence([ prompt, model, parser, prompt2, model, parser ])   # Chaining prompt, model, and parser together multiple times

print(chain.invoke({"topic":"programming"}))