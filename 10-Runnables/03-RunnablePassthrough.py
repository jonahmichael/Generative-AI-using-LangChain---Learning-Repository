''' 

03. Runnable Passthrough
The RunnablePassthrough is a simple yet useful Runnable provided by LangChain. It acts as a pass-through component that takes an input and returns it unchanged.
This can be particularly useful in scenarios where you want to include a placeholder or a no-op step in a chain of Runnables.

Check out image.png for example diagram.


'''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

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

joke_generator = RunnableSequence([ prompt, model, parser ])   # Chaining prompt, model, and parser together 
# This will generate a joke based on the topic

parallel_Chain = RunnableParallel({
    'joke': RunnablePassthrough(), # passthrough will just return the joke as it is
    'explanation': RunnableSequence([ prompt2, model, parser ]) # This will explain the joke
})

final_chain = RunnableSequence([ joke_generator, parallel_Chain ])  # First generate the joke, then pass it to the parallel chain
print(final_chain.invoke({"topic":"programming"}))
# First, generate the joke, then pass it to the parallel chain to get both the joke and its explanation