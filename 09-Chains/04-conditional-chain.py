# for example, if check if a review is positive or negative and then respond accordingly
# we can use a conditional chain to handle this logic
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch # Importing RunnableBranch for conditional chains
import os
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field # Importing BaseModel and Field for defining structured outputs
from typing import Literal # Importing Literal for fixed string values

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("google_api_key")
)

# Define the Pydantic model for sentiment output
class SentimentOutput(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(..., description="The sentiment of the review")

# Create a Pydantic output parser
parser_pydantic = PydanticOutputParser(pydantic_object=SentimentOutput)

# Prompt for sentiment classification
prompt_classifier = PromptTemplate(
    template="""Give a sentiment analysis of the following review as Positive or Negative.
Return the output in JSON format, strictly adhering to the schema: {format_instructions}
Review: '{review}'
""",
    input_variables=["review"],
    partial_variables={"format_instructions": parser_pydantic.get_format_instructions()}
)

# Chain to classify the sentiment
# The model should output a string that can be parsed by parser_pydantic
classifier_chain = prompt_classifier | model | StrOutputParser() | parser_pydantic

# Branching chain to respond based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x['sentiment'].sentiment == 'Positive', PromptTemplate(template="Write a positive response to the review: '{review}'", input_variables=["review"]) | model | StrOutputParser()),
    (lambda x: x['sentiment'].sentiment == 'Negative', PromptTemplate(template="Write a negative response to the review: '{review}'", input_variables=["review"]) | model | StrOutputParser()),
    lambda x: f"Sentiment '{x['sentiment'].sentiment}' not recognized."  # default case
)

# Overall chain combining sentiment classification and response generation
overall_chain = RunnableParallel(
    review=lambda x: x,
    sentiment=classifier_chain
) | branch_chain

# --- Test cases ---
positive_review = "This product is amazing! I love it so much."
print("Positive Review Response:", overall_chain.invoke(positive_review))

negative_review = "This product is terrible. I'm very disappointed."
print("Negative Review Response:", overall_chain.invoke(negative_review))

neutral_review = "The product arrived on time, and the packaging was adequate."
print("Neutral Review Response (expected default or error as only pos/neg defined):", overall_chain.invoke(neutral_review))