'''
A wiki retriever is a specialized information retrieval system designed to fetch relevant articles or documents from a Wikipedia corpus based on user queries. It leverages the structured and extensive content available on Wikipedia to provide accurate and contextually relevant information.

How it Works:
1. You give us a query or a topic of interest.
2. The wiki retriever searches through the Wikipedia corpus(API) to find articles that match the query.
3. It uses techniques such as keyword matching, semantic search, or embedding-based retrieval to identify the most relevant articles.
4. The retriever then returns a list of relevant Wikipedia articles or excerpts that best address the user's query.
'''

from langchain_community.retrievers import WikiRetriever