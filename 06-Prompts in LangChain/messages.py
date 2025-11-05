# There are 3 types of messages in LangChain:
# 1. HumanMessage: Represents a message from a human user.
# 2. AIMessage: Represents a message from an AI model.
# 3. SystemMessage: Represents a system-level message that can provide context or instructions to the AI model.


from pyexpat import model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("google_api_key"))

messages=[
    SystemMessage(content="You are a tech expert assistant."),
    HumanMessage(content="tell me a joke about computers."),
    ]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)