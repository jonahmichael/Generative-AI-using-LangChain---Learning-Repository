from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

prompt=PromptTemplate(
    template="What is a good name for a company that makes {product}?",
    input_variables=["product"])
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)
parser = StrOutputParser()

chain = prompt | model | parser  # Creating a simple chain by linking prompt, model, and parser
# Running the chain with an input
result = chain.invoke({"product": "colorful socks"})
#print(result)  # Output the result

chain.get_graph().print_ascii()