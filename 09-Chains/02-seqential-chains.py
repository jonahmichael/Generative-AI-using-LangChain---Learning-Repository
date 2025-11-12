from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

prompt1=PromptTemplate(
    template="write a detailed report on the topic '{topic}' including introduction, main content and conclusion.",
    input_variables=["topic"])

prompt2=PromptTemplate(
    template="write a 3 line summary on the topic '{text}'.",
    input_variables=["text"])

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)

parser= StrOutputParser()

chain = prompt1 | model |parser| prompt2 | model | parser
result=chain.invoke({"topic":"Artificial Intelligence in Healthcare"})
print(result)
# Expected output: A 3 line summary of the detailed report on "Artificial Intelligence in Healthcare".
# chain.get_graph.print_ascii()   -- Uncomment to visualize the chain graphically
