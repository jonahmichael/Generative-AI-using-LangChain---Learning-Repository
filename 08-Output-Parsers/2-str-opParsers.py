#from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint  
# we are using hugging face's opensource models as they usually give unstructured text outputs than the google models so that we can demonstrate output parsers better 
from langchain_google_genai import ChatGoogleGenerativeAI # there is some issue with langchain_huggingface package currently
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)

#1st prompt - detailed report
template1=PromptTemplate(
  template="write a detailed report on the topic '{topic}' including introduction, main content and conclusion.",
  input_variables=["topic"]
)

##2nd prompt - short summary
template2=PromptTemplate(
  template="write a 3 line summary on the topic '{text}'.",
  input_variables=["text"]
)

# from here we will create a custom output parser

# A parser is responsible for taking the raw output from the model and transforming it into a structured format
parser= StrOutputParser()

# A chain is responsible for taking the output from one step and passing it as input to the next step
# The chain will first use template1 to generate a detailed report, then pass that report to template2 to generate a summary, and finally use the parser to format the output correctly.

# | operator is used to chain together different components in LangChain
chain =  template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"Dogs as pets"})
print(result)

