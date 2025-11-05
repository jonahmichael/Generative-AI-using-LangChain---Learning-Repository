# Before: from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate # CORRECTED IMPORT for PromptTemplate as we are using langchain_core

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
# No need to import 'langchain.prompts' here anymore BECAUSE we already imported PromptTemplate from langchain_core.prompts
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    st.error("Google AI Studio API key not found. Please set it in a .env file or as an environment variable (GOOGLE_API_KEY).")
    st.stop()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=google_api_key)

st.header("Research Tool (Powered by Google Gemini)")

paper_input = st.selectbox(
    "Select Research Paper Name",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = PromptTemplate(
  template="Explain the research paper titled '{paper_name}' in a {explanation_style} style with a {explanation_length} length.",
  input_variables=["paper_name", "explanation_style", "explanation_length"]
)

if st.button("Generate Explanation"):
    st.write("Generating explanation...")
    prompt_text = template.format(
        paper_name=paper_input,
        explanation_style=style_input,
        explanation_length=length_input
    )

    try:
        with st.spinner("Fetching explanation from Google Gemini..."):
            response = model.invoke(prompt_text)
        st.subheader("Explanation:")
        st.write(response.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")