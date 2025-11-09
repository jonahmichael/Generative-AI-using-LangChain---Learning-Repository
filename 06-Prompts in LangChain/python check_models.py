import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Load your .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    print("Models available for generateContent method:")
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(m.name)
else:
    print("ERROR: GOOGLE_API_KEY not found in .env file.")
    