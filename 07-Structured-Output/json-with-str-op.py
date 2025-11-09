import os
from langchain_google_genai import ChatGoogleGenerativeAI # Use ChatGoogleGenerativeAI for chat models
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from pydantic import BaseModel, Field

# Load environment variables from a .env file
load_dotenv()

# Get the Google API key from environment variables
google_api_key = os.getenv("google_api_key")

if not google_api_key:
    print("Error: Google AI Studio API key (google_api_key) not found in environment variables.")
    # You might want to exit here if the key is mandatory for your script
    exit()

# Initialize the Google Gemini model
# Use ChatGoogleGenerativeAI and pass the API key explicitly
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Corrected model name to "gemini-2.0-flash"
    temperature=0, # It's good practice to set temperature for consistent output
    google_api_key=google_api_key
)

# we are doing for JSON schema here
json_schema_example={
  "properties": {
    "key_themes": {
      "description": "List of key themes mentioned in the review, e.g., ['Camera', 'Battery Life', 'Design']",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "summary": {
      "description": "Concise summary of the review, e.g., 'The iPhone 15 offers significant camera improvements and USB-C support, but design changes are minimal.'",
      "type": "string"
    },
    "sentiment": {
      "description": "Overall sentiment of the review, e.g., 'Positive', 'Negative', 'Neutral'",
      "type": "string"
    },
    "recommendation": {
      "description": "Whether the reviewer recommends the product, e.g., 'Yes', 'No', 'N/A'",
      "type": "string"
    },
    "pros": {
      "description": "List of pros mentioned in the review, e.g., ['Fast shipping', 'Good quality']",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "cons": {
      "description": "List of cons mentioned in the review, e.g., ['Poor customer service', 'Expensive']",
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [
    "key_themes",
    "summary",
    "sentiment",
    "recommendation",
    "pros",
    "cons"
  ],
  "title": "ReviewAnalysisSchema",
  "type": "object"
}

# Get the structured model
# You need to pass the Pydantic model (or TypedDict) directly
structured_model = model.with_structured_output(json_schema_example)

# Define the input review
review_input = """I recently upgraded to the iPhone 15 after holding onto my iPhone 12 for a few years, and honestly, it's a bit of a mixed bag – mostly positive, but with some lingering thoughts.
Pros:
Camera System: This is probably the biggest jump for me. The photos, especially in low light, are noticeably sharper and more vibrant. The new Photonic Engine really makes a difference, and having 2x optical zoom on the main lens is incredibly handy for everyday shots without losing quality. If you're coming from an older iPhone, this alone could be worth it.
Dynamic Island: I thought this would be a gimmick, but it's actually incredibly intuitive and useful. Seeing live activities like my timer, music, or Uber status discreetly at the top of the screen without interrupting what I'm doing is a game-changer. It feels genuinely futuristic.
USB-C: Finally! Being able to use one charger for my phone, iPad, and MacBook is fantastic. It's a small quality-of-life improvement but a very welcome one. Data transfer speeds seem zippier too, though I don't move large files often.
Brightness: The display gets incredibly bright outdoors, which is perfect for sunny days. Content looks stunning, as always, but now it's even more usable in direct sunlight.
Battery Life: It's solid. Not mind-blowing, but I comfortably get through a full day of moderate to heavy use without needing to top up. That's a definite improvement over my old phone.
Cons:
Design Stagnation (Slightly): While the rounded edges feel great in the hand, the overall design language hasn't changed drastically. It still looks very much like an iPhone, which isn't necessarily bad, but for a "new" numbered generation, it lacks a certain visual pizzazz.
Base Model Refresh Rate: Still sticking with 60Hz. Coming from a 120Hz iPad, scrolling on the iPhone 15 sometimes feels a little less fluid. It's not a dealbreaker, but at this price point, ProMotion should really be standard across the board.
Performance (Marginal Upgrade for Most): The A16 Bionic chip is undoubtedly fast, but for my everyday tasks (browsing, social media, light gaming), I don't feel a massive leap over my older A15-powered phone. If you're not doing intensive video editing or hardcore gaming, you might not notice the raw power difference as much.
Price: It's an iPhone, so it's expensive. While you get premium hardware and software, the incremental upgrades year-over-year sometimes make you pause and consider if it's truly worth the full price without significant trade-ins.
Verdict:
The iPhone 15 is a highly capable smartphone that refines the iPhone experience rather than revolutionizing it. The camera, Dynamic Island, and USB-C are genuine improvements that enhance daily use. If you're coming from an iPhone 12 or older, it's a very compelling upgrade. If you have an iPhone 13 or 14, you might find the changes less impactful unless the camera or Dynamic Island are absolute must-haves for you. It's an excellent phone, just not a radical departure."""

# Invoke the structured model with the review input
result = structured_model.invoke(review_input)

# Print the structured result
print(result)
print(f"Summary: {result['summary']}")
print(f"Sentiment: {result['sentiment']}")
print(f"Recommendation: {result['recommendation']}")