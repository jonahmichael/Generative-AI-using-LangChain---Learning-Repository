from langchain_google_genai import ChatGoogleGenerativeAI # Changed to ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os # Import os to get the API key

load_dotenv() # Load environment variables from a .env file

# Get the Google API key from environment variables
google_api_key = os.getenv("google_api_key")

if not google_api_key:
    print("Error: Google AI Studio API key not found. Please set it in a .env file or as an environment variable (google_api_key).")
    exit() # Exit if the key is missing

# Initialize the Google Gemini model
# Ensure 'model' parameter is used and pass the API key explicitly
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key)

chat_history = [] # Initialize chat history

print("Chatbot initialized. Type 'exit' or 'quit' to end the conversation.")

while True:
  # Syntax Error 1: Variable names cannot contain hyphens. Use underscores.
  user_input = input("You: ") # Get user input
  chat_history.append({"role": "user", "content": user_input}) # Append user message to chat history

  if user_input.lower() in ["exit", "quit"]:
    print("Exiting the chatbot. Goodbye!")
    break

  # Get response from the model
  result = model.invoke(user_input)
  chat_history.append({"role": "Bot", "content": result.content}) # Append model response to chat history

  # Syntax Error 2 & Logical Fix: Access the content of the AIMessage object
  # The invoke method returns an AIMessage object, not directly the string content.
  print("Bot:", result.content) # Print the model's response content
  
print("Chat session ended.")
print("Full chat history:", chat_history) # Print the full chat history at the end