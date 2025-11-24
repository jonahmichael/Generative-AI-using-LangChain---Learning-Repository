# What are Retrievers?

A retriver is a component in a machine learning or information retrieval system that is responsible for fetching relevant documents or data based on a given query. Retrievers are commonly used in applications such as search engines, question-answering systems, and recommendation systems.

Data Sources --> [Retriever] --> Retrieved Documents --> [Reader/Ranker] --> Final Output

Retrievers typically work by indexing a large corpus of documents and then using various algorithms to match the query against this index. Common techniques used in retrievers include:
- **Keyword Matching**: Finding documents that contain specific keywords from the query.
- **Vector Space Models**: Representing documents and queries as vectors in a multi-dimensional space and measuring similarity using metrics like cosine similarity.
- **Neural Retrieval Models**: Using deep learning techniques to learn representations of documents and queries for more effective retrieval.


We can categories based on their approach:
  ###1. Search Engine Based Retrievers:
  These retrievers leverage traditional search engine technologies like Elasticsearch or Apache Solr to index and retrieve documents based on keyword matching and other search algorithms.
  
  ###2. Embedding Based Retrievers: 
  These retrievers use vector embeddings to represent documents and queries in a high-dimensional space. They utilize techniques like cosine similarity or nearest neighbor search to find relevant documents based on their vector representations.
  
## Here we are some popular retriever implementations:
  
  ### 1. WikiRetriever
  A retriever that fetches documents from a Wikipedia corpus.
  