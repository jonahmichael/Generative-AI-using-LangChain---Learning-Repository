#from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint  
# we are using hugging face's opensource models as they usually give unstructured text outputs than the google models so that we can demonstrate output parsers better 
from langchain_google_genai import ChatGoogleGenerativeAI # there is some issue with langchain_huggingface package currently
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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


# we will chain these two prompts together using the same model
# the output of the first prompt (detailed report) will be passed as input to the second prompt (short summary)


prompt1= template1.invoke({"topic":"Generative AI"})
result1=model.invoke(prompt1)
print("detailed report output:\n",result1)
prompt2= template2.invoke({"text":result1})
result2=model.invoke(prompt2)
print("short summary output:\n",result2)