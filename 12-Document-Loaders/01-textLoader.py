'''  
Text Loader is a simple document loader in LangChain that is used to load plain text files. It reads the content of a text file and converts it into a standardized Document object that can be further processed in a RAG system.

'''
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from langchain_community.document_loaders import TextLoader

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)

prompt=PromptTemplate(
    template="Extract the key points from the following text:\n{poem}",
    input_variables=["poem"])

parser= StrOutputParser()
loader = TextLoader(r'D:\Learning Stuffs\Langchain\12-Document-Loaders\story.txt', encoding='utf8')

docs=loader.load()  # returns a list of Document objects
# print(docs)

chain=prompt | model | parser  # Using the pipe operator to chain prompt, model, and parser together

print(chain.invoke({"poem":docs[0].page_content}))  # Accessing the content of the first Document object