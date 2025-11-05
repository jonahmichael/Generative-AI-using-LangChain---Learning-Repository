from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file


# to know whtat temperature does, refer notion notes (05)
model=ChatOpenAI(model_name="gpt-4",temperature=0,max_completions_tokens=10)
result = model.invoke("what is the capital of France?")
print(result)

# Expected output: "The capital of France is Paris."