RAG Example - Document Loaders
----------------------------

RAG (Retrieval-Augmented Generation) systems often require loading and processing documents from various sources. This example demonstrates how to use different document loaders to ingest text data for RAG applications.

Using RAG, we can enhance the capabilities of language models by providing them with relevant context from external documents. This is particularly useful for tasks such as question answering, summarization, and information retrieval.

EG: Loading documents from a local text file and a web page. NotebookLLM

4 components of RAG system:
1. Document Loaders: To load documents from various sources into a standardized format(usally as Document objects) (e.g., local files, web pages, databases).
2. Text Splitters: To split large documents into smaller, manageable chunks.
3. Vector Store: To store and index the document embeddings for efficient retrieval.
4. Retriever: To fetch relevant document chunks based on user queries.

In this 12th lesson, we will focus on the first component: Document Loaders.

Document Loaders in LangChain:
LangChain provides several built-in document loaders to facilitate the ingestion of text data from different sources. Some commonly used document loaders include:
They are of many types: but the important ones are:
1. TextLoader: Loads plain text files.
2. PDFLoader: Loads PDF documents.
3. WebBaseLoader: Loads web pages.
4. CSVLoader: Loads CSV files.

Each loader reads the content from its respective source and converts it into a standardized Document object that can be further processed in a RAG system.

Check out https://docs.langchain.com/oss/python/integrations/document_loaders

Also, we can create custom Documetn Loaders. Refer the langchain pafe for more details.