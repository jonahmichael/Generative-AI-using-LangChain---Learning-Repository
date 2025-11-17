'''
4. Runnable with Lambda Expressions
In addition to using predefined Runnables, LangChain allows you to create custom Runnables using lambda expressions or regular functions. This provides flexibility to define specific behaviors that may not be covered by existing Runnables.

eg: You want to find the emotion of a review. But what if there are a lot of emojis,icons etc.. ?

so we can create a custom Runnable that first cleans the text by removing emojis and then analyzes the sentiment.

'''

# i am going to take the output and count the number of words in it 
# from langchain_core.runnables import RunnableLambda

# def word_counter(text):
#     return len(text.split())
  
# runnable_word_counter = RunnableLambda(word_counter)
# print(runnable_word_counter.invoke("This is a sample text with several words."))  # Output: 8

# -------------------------------------------


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

prompt=PromptTemplate(
    template="write a joke on the topic '{topic}'",
    input_variables=["topic"]
)

def word_counter(text):
     return len(text.split())


model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)

parser= StrOutputParser()

joke_generator = RunnableSequence([ prompt, model, parser ])   # Chaining prompt, model, and parser together 
# This will generate a joke based on the topic

parallel_Chain = RunnableParallel({
    'joke': RunnablePassthrough(), 
    'explanation': RunnableLambda(word_counter) # This will count the number of words in the joke
})

final_chain = RunnableSequence([ joke_generator, parallel_Chain ])  # First generate the joke, then pass it to the parallel chain
print(final_chain.invoke({"topic":"programming"}))
# First, generate the joke, then pass it to the parallel chain to get both the joke and its explanation