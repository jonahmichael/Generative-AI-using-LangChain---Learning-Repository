# 2. RunnableParallel: This Runnable allows you to execute multiple Runnables in parallel.
# It takes a list of Runnables as input and runs them simultaneously, collecting their outputs.
# This is useful for tasks that can be performed independently and concurrently, such as querying multiple models 

#   eg;          AI (topic)
#              /   \
#           LLM1     LLM2
#             |        |
#           Parser1   Parser2 
#             |          |
#            op1        op2


# _________________________________________________________________________

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

# Our task is to generate 2 different content and post one in X and another in Linkedin

prompt1=PromptTemplate(        # for X ( twitter)
    template="write a tweet on the topic '{topic}'",
    input_variables=["topic"])

prompt2=PromptTemplate(        # for Linkedin
    template="write a linkedin post on the topic '{topic}'", 
    input_variables=["topic"])

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)

parser= StrOutputParser()

parallel_chain = RunnableParallel([
    tweet_chain := RunnableSequence([prompt1, model, parser]),
    linkedin_chain := RunnableSequence([prompt2, model, parser])
])

# This will be our main chain which will run both the tweet and linkedin chains in parallel in the form of a dictionary where the keys are the chain names and the values are the outputs of the respective chains.
result=parallel_chain.invoke({"topic":"artificial intelligence advancements in 2025"})

print(result[tweet_chain])
print(result[linkedin_chain])