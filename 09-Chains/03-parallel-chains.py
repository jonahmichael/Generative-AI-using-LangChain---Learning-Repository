from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel  # Importing RunnableParallel for parallel chains
import os

load_dotenv()
# Chains in LangChain are a way to link together multiple components (like prompts, models, and tools)

# to create more complex workflows. They allow you to pass the output of one component as the input to another,
# enabling you to build sophisticated applications with ease.

# They are of various types, including
# 1. Simple Chains, 
# 2. Sequential Chains, 
# 3. Complex ones like Router Chains.
# Parallel Chains,
prompt1=PromptTemplate(
    template="write a short in 20 words report on the topic '{topic}'.",
    input_variables=["topic"])

prompt2=PromptTemplate(
    template="write a 1 line heading and theme on the topic '{text}'.",
    input_variables=["text"])

prompt3=PromptTemplate(
    template="give a question based on the heading and theme '{heading_theme}'.",
    input_variables=["heading_theme"])
model1= ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("google_api_key")
)

model2= ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite", 
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

parser= StrOutputParser()

parallel_chain= RunnableParallel(
      'short_report', prompt1 | model1 | parser,   # we are giving 3 inputs to the parallel chain
      'heading_theme', prompt2 | model2 | parser,
      'question', prompt3 | model2 | parser,
)

# Now, we can run the parallel chain with a single input dictionary
merge_chain= prompt3 | model2 | parser
chain= parallel_chain | merge_chain
# allow multiple chains to run simultaneously, each processing different inputs and producing outputs that can be combined later.

text_input= "Artificial Intelligence in Healthcare"
result= chain.invoke({
    'topic': text_input
})
    # The output will be a dictionary with results from all parallel chains allow multiple chains to run simultaneously, each processing different inputs and producing outputs that can be combined later.
print("Final Result:", result)