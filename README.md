# Generative AI using LangChain - Learning Repository

A comprehensive hands-on repository for learning LangChain framework, following the CampusX GenAI course series. This repository contains code implementations, examples, and notes covering LangChain fundamentals to advanced concepts for building intelligent AI applications.

## About This Repository

This is a learning journey through LangChain, documenting practical implementations of various LangChain components and concepts. Each folder contains working code examples, demonstrations, and personal notes from the CampusX course series.

## What is LangChain?

LangChain is a powerful framework for developing applications powered by Large Language Models (LLMs). It provides tools for chaining LLM calls, managing memory, implementing retrieval-augmented generation (RAG), building agents, and creating complex conversational AI systems.

## Course Progress

### Completed Topics

#### 1. Introduction to LangChain (Video 1-2)
- Understanding the LangChain framework and its ecosystem
- Overview of LangChain components and architecture
- Setting up the development environment

#### 2. LangChain Models (Video 3)
**Folder:** `05-Langchain-Models/`
- LLM implementations and demonstrations
- Chat Models integration with multiple providers:
  - OpenAI
  - Google (Gemini)
  - Anthropic (Claude)
  - HuggingFace (API and Local)
- Embedding Models:
  - OpenAI embeddings for documents and queries
  - HuggingFace embeddings (local)
  - Document similarity calculations

#### 3. Prompts in LangChain (Video 4)
**Folder:** `06-Prompts in LangChain/`
- Prompt templates and template management
- Message handling and formatting
- Interactive prompt generators
- Building chatbot interfaces with prompts
- Custom template loading from JSON

#### 4. Structured Output (Video 5)
**Folder:** `07-Structured-Output/`
- JSON schema definitions
- Pydantic models for structured responses
- TypedDict implementations
- Converting LLM outputs to structured formats

#### 5. Output Parsers (Video 6)
**Folder:** `08-Output-Parsers/`
- String output parsers
- JSON output parsers
- Pydantic output parsers
- Structured output parsers with response schemas

#### 6. Chains in LangChain (Video 7)
**Folder:** `09-Chains/`
- Simple chain implementations
- Sequential chains for multi-step processing
- Parallel chains for concurrent execution
- Conditional chains for dynamic workflows

#### 7. Runnables (Video 8-9)
**Folder:** `10-Runnables/`
- Understanding the Runnable interface
- Runnable sequences and composition
- Advanced runnable patterns and use cases

#### 8. Document Loaders (Video 10)
- Loading data from various sources (PDF, CSV, Web, etc.)
- Document processing and ingestion pipelines
- Working with different file formats

#### 9. Text Splitters (Video 11)
- Chunking strategies for large documents
- Character-based and token-based splitting
- Recursive text splitting techniques

#### 10. Vector Stores (Video 12)
- Understanding vector databases
- Storing and indexing embeddings
- Integration with FAISS, Chroma, Pinecone

#### 11. Retrievers (Video 13) _ NOT FULLY DONE BUT CONCEPTS DONE 
- Building retrieval systems
- Similarity search implementations
- Advanced retrieval strategies

#### 12. Retrieval Augmented Generation - RAG (Video 14-15)
- Understanding RAG architecture
- Building RAG systems for document Q&A
- Implementing YouTube chatbot with RAG

### Upcoming Topics

The following topics are planned for future implementation as part of the course progression:

#### 13. Tools in LangChain (Video 16-17)
- Creating custom tools
- Tool integration and management
- Tool calling patterns and best practices

#### 14. AI Agents (Video 18)
- Building autonomous AI agents
- Agent reasoning and decision-making
- End-to-end agent application development

## Repository Structure

```
.
├── 05-Langchain-Models/          # LLM, Chat Models, and Embeddings
│   ├── 1.LLM/
│   ├── 2.CHAT-MODELS/
│   └── 3.EMBEDDED-MODELS/
├── 06-Prompts in LangChain/      # Prompt engineering and templates
├── 07-Structured-Output/         # JSON schemas and Pydantic models
├── 08-Output-Parsers/            # Various output parsing techniques
├── 09-Chains/                    # Chain implementations
├── 10-Runnables/                 # Runnable interface examples
├── notes/                        # Personal learning notes
├── instructions.txt              # Setup instructions
└── .env                          # API keys (not tracked in git)
```

## Prerequisites

- Python 3.8 or higher
- Basic understanding of Python programming
- API keys for LLM providers (OpenAI, Google, Anthropic, HuggingFace) - **Optional for beginners** (see API Keys section for details)

## Setup Instructions

### 1. Clone the Repository

```powershell
git clone https://github.com/jonahmichael/GenAI-using-LangChain---Notes-Code---CampusX.git
cd GenAI-using-LangChain---Notes-Code---CampusX
```

### 2. Create Virtual Environment

For each module/folder you work on, create a dedicated virtual environment:

```powershell
python -m venv venv
```

### 3. Activate Virtual Environment

```powershell
.\venv\Scripts\activate.ps1
```

If you encounter execution policy errors, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Install Dependencies

```powershell
pip install --upgrade langchain langchain-core langchain-google-genai python-dotenv transformers
```

For specific modules, you may need additional packages:

```powershell
# For OpenAI models
pip install langchain-openai

# For Anthropic models
pip install langchain-anthropic

# For HuggingFace
pip install huggingface-hub

# For UI components (Streamlit)
pip install streamlit
```

### 5. Configure API Keys

API keys are unique codes that allow your applications to access external services like language models. They act like passwords that authenticate your requests to these services. For this repository, you'll need API keys from various providers to run the examples.

**Important for Beginners:** If you don't have API keys yet, you can still explore the code structure and learn the concepts. Some examples use local models that don't require API keys. We'll guide you through getting keys step by step.

#### Step-by-Step Guide to Get Google API Key

Google provides access to their Gemini models through the Google AI Studio. Here's how to get your API key:

1. **Visit Google AI Studio:**
   - Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey) in your web browser
   - Sign in with your Google account (Gmail account)

2. **Create a New API Key:**
   - Click on "Create API key" button
   - Choose a name for your API key (e.g., "LangChain-Learning")
   - Click "Create API key in new project" or select an existing project

3. **Copy Your API Key:**
   - Once created, you'll see your API key displayed
   - **Important:** Copy the key immediately and store it securely
   - You won't be able to see the full key again for security reasons

4. **Understand Usage Limits:**
   - Google provides a generous free tier (around $300 in credits for new users)
   - This is usually enough for learning and small projects

#### Setting Up Your .env File

The `.env` file stores your API keys securely and keeps them separate from your code.

1. **Create the .env File:**
   - In your project root directory (`D:\Learning Stuffs\Langchain\`), create a new file named `.env`
   - Make sure it has no file extension (just `.env`)

2. **Add Your API Keys:**
   - Open the `.env` file in a text editor (like Notepad or VS Code)
   - Copy and paste the following template, replacing the placeholders with your actual keys:

   ```env
   # Google API Key (required for Google Gemini models)
   google_api_key=your_google_api_key_here

   # Optional: Add other API keys as you need them
   # OPENAI_API_KEY=your_openai_api_key_here
   # ANTHROPIC_API_KEY=your_anthropic_api_key_here
   # HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
   ```

   **Example with a real key:**
   ```env
   google_api_key=AIzaSyD1234567890abcdefghijklmnopqrstuvw
   ```

3. **Save the File:**
   - Save the file as `.env` (make sure it's not `.env.txt`)
   - The file should be in the same directory as your Python scripts

4. **Security Notes:**
   - Never share your `.env` file or commit it to version control
   - The `.gitignore` file in this repository already excludes `.env` files

#### Getting API Keys for Other Providers (Optional)

**OpenAI API Key:**
- Visit [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Sign up or log in
- Create a new API key
- Add to `.env` as `OPENAI_API_KEY=your_key_here`
- Free tier available with $5 credit for new users

**Anthropic API Key:**
- Visit [https://console.anthropic.com/](https://console.anthropic.com/)
- Sign up and create an API key
- Add to `.env` as `ANTHROPIC_API_KEY=your_key_here`
- Free tier available

**HuggingFace Token:**
- Visit [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- Create a new token
- Add to `.env` as `HUGGINGFACEHUB_API_TOKEN=your_token_here`
- Free to use

#### For Beginners: Getting Started Without API Keys

If you're just starting out and don't want to set up API keys immediately:

1. **Explore Local Models:** Some examples in the `05-Langchain-Models/3.EMBEDDED-MODELS/` folder use local HuggingFace models that don't require API keys.

2. **Focus on Concepts:** Read through the code to understand LangChain patterns, even if you can't run all examples.

3. **Start Small:** Begin with the Google API key (easiest to set up) and expand as you progress.

4. **Free Alternatives:** All major providers offer free tiers or credits for learning purposes.

#### Testing Your Setup

After setting up your `.env` file, test it by running a simple script:

```powershell
python 05-Langchain-Models/2.CHAT-MODELS/chatmodel-google.py
```

If it runs without API key errors, your setup is correct!

### 6. Run Examples

Navigate to any folder and run the Python scripts:

```powershell
python filename.py
```

For Streamlit applications:

```powershell
streamlit run prompt-ui.py
```

## Key Learning Outcomes

By working through this repository, you will learn:

- How to integrate multiple LLM providers (OpenAI, Google, Anthropic, HuggingFace)
- Building and chaining prompts for complex conversations
- Parsing and structuring LLM outputs
- Creating sequential and parallel processing workflows
- Using the Runnable interface for composable components
- Best practices for prompt engineering and model interaction

## Technologies Used

- **LangChain**: Core framework for LLM applications
- **LangChain Core**: Fundamental abstractions and interfaces
- **OpenAI API**: GPT models integration
- **Google Generative AI**: Gemini models
- **Anthropic API**: Claude models
- **HuggingFace**: Open-source models and embeddings
- **Python dotenv**: Environment variable management
- **Streamlit**: Interactive UI for demos

## Troubleshooting

### Common Issues

**Import Errors with StructuredOutputParser:**
If you encounter import errors with `StructuredOutputParser` from `langchain_core.output_parsers`, this class may have been moved or deprecated in newer versions. Use alternative parsers like `PydanticOutputParser` or `JsonOutputParser`.

**Torch DLL Errors on Windows:**
If you see Win32 application errors related to PyTorch, you may need to reinstall PyTorch:

```powershell
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**API Key Issues:**
Ensure your `.env` file is in the correct location and keys are properly formatted without quotes.

## Resources

- **Course Playlist**: [CampusX GenAI using LangChain](https://www.youtube.com/@campusx-official)
- **LangChain Documentation**: [https://python.langchain.com/](https://python.langchain.com/)
- **LangChain GitHub**: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)

## Course Information

This repository follows the **"Generative AI using LangChain"** course series by CampusX, which covers:

- LLM chaining and composition
- Building AI-powered chatbots and applications
- Retrieval-Augmented Generation (RAG) for smarter AI
- Integrating external data and APIs for real-world use cases
- Creating autonomous AI agents

## Contributing

This is a personal learning repository. Feel free to fork and use it for your own learning journey.

## License

This repository is for educational purposes. Please respect the terms of service of all API providers used in the examples.

## Acknowledgments

Special thanks to CampusX for creating this comprehensive GenAI course series that makes learning LangChain accessible and practical.
