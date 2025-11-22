# Vector Stores

Let's understand what Vector Stores are and why they are important in the context of language models and AI.

Let us say i want to add a movie recommendation feature to my application. I have a large collection of movie descriptions, reviews, and metadata. When a user asks for a recommendation, I need to quickly find movies that are similar to their preferences.

So i want to suggest matches based on the user's input. This is where Vector Stores come into play.

For eg: User says "I love Taare Zameen Par because of its emotional depth and portrayal of childhood struggles." . It is stupid to recommend movies based on keyword matching like "childhood" or "emotional" because many movies may contain these words but not capture the essence of what the user is looking for.

It may match based on keywords like director name, actor name, genre etc. but that is not what user wants. User wants movies that evoke similar feelings or explore similar themes. Which the keyword matching will fail to capture.  

So what we can do is Create  movie-ID and its entire plot as summary and now we can compare two movies as they could have better semantic similarity.

Talking about this feature may seem simple but under the hood it is very complex. This is where Vector Stores come into play.

So we use Embeddings to convert the movie descriptions into high-dimensional vectors. These vectors capture the semantic meaning of the text, allowing us to compare movies based on their content rather than just keywords. THis is made simple using Deep Learning models.This is where Vector Stores come into play and make it easy to store and retrieve these high-dimensional vectors efficiently.

So these embeddings:
  1. Every vector has 512 dimensions (for example)
  2. Each dimension represents a specific feature or aspect of the movie's content.
  3. So we plot these vectors in a 512-dimensional space.
  4. First we plot for movie 1, then movie 2 and so on.
  5. Then we find the angular distance or cosine similarity between these vectors to find how similar they are.
  6. In ground level, this is basically mathematical calculations but it is made simple using Vector Stores.
  
  
  ## Challenges we face without vector store:
  
  1. To generate embeddings for large datasets can be computationally expensive.
  
  2. Storing high-dimensional vectors requires efficient data structures to ensure quick retrieval. We can store in relational databases but they are not optimized for high-dimensional data.
  
  3. We need to perform similarity searches(Semantic Search) quickly, especially when dealing with large datasets. Linear search methods can be slow and inefficient.SO we need a intelligent system that compare in such a way we dont waste too much time.
  
  ## This is where Vector Stores come into play.
  
  # What are Vector Stores?
  Vector Stores are specialized databases designed to store, index, and retrieve high-dimensional vectors(in form of numerical vectors)efficiently. They are optimized for operations like similarity searches, making them ideal for applications involving embeddings and semantic search.
  
  ## Key Features of Vector Stores:
  
  ###1. Efficient Storage:
  Vector Stores use data structures that optimize the storage of high-dimensional. Ensures vectors and their meta data are stored, wheather for qucik lookups(RAM-volatile) or on disk storage(harddisk-Permanent).
  
  ### Similarity Search:
  They implement algorithms that allow for fast similarity searches, such as Approximate Nearest Neighbors (ANN) algorithms. This enables quick retrieval of vectors that are similar to a given query vector.
  
  ### Indexing:
  Vector Stores create indexes that facilitate rapid searching and retrieval of vectors based on their similarity. These indexes are designed to handle the complexities of high-dimensional data.
  eg: Approximate Nearest Neighbor (ANN) algorithms like HNSW, Faiss, Annoy etc.
  
  ### CRUD Operations:
  They provide Create, Read, Update, and Delete operations for managing vectors and their associated metadata. This makes it easy to maintain and update the vector database as needed.
  
  
  ## USE CASES OF VECTOR STORES:
  
  ### 1. Semantic Search: 
  Enabling search engines to retrieve documents based on meaning rather than exact keyword matches.
  
  ### 2. Recommendation Systems:
  Powering recommendation engines that suggest items based on user preferences and behavior.
  
  ### 3. Image and Video Retrieval:
  Facilitating the retrieval of images and videos based on visual similarity. 
  
  ### 4. RAG (Retrieval Augmented Generation):
  Enhancing language models by providing them with relevant context from a vector store during generation.
  
  
  _________________________________________________
  
  
  # Vector Store vs Vector Database:
  
  While the terms "Vector Store" and "Vector Database" are often used interchangeably, there is a subtle distinction between the two.
  
  
  
  - Vector Store: Refers to the broader concept of storing and managing high-dimensional vectors. It encompasses the methods, algorithms, and data structures used to handle vector data efficiently.
  
  Vtctor Store has features like:
    1. STorage of high-dimensional vectors
    2. Similarity Search ( retrieving similar vectors)
    
  - Vector Database: Specifically refers to a database system that is designed to store and manage vector data. It is a concrete implementation of the Vector Store concept, often providing additional database functionalities such as transactions, concurrency control, and data integrity.
  
  Features of Vector Database:
    1. All features of Vector Store
    2. Database functionalities (transactions, concurrency control, data integrity)
    3. Scalability and distributed storage
    4. Integration with other database systems
    5. Advanced querying capabilities
    + more stuffs.
        
    ## Vector Database = Vector Store + Database Functionalities
    
    __________________________________________________
    
    # Vector Stores in LangChain:
    
    1. LangChain provides a unified interface to work with various vector stores, making it easy to integrate them into your applications.
    2. It supports multiple vector store implementations, allowing developers to choose the one that best fits their needs.
    3. LangChain abstracts the complexities of working with different vector stores, providing a consistent API for storing, retrieving, and managing vectors.
    4. It also offers tools for indexing and searching vectors, enabling efficient similarity searches and retrieval operations.
    5. LangChain's vector store integration is designed to work seamlessly with other components of the LangChain ecosystem, such as language models and document loaders.
    
      
  ## Popular Vector Stores supported in LangChain:
  
    1. FAISS (Facebook AI Similarity Search)
    2. Pinecone
    3. Weaviate
    4. Milvus
    5. Chroma
    6. Qdrant
    7. Supabase
    8. Elasticsearch
    9. Annoy
    10. HNSWLib
    
    We are going to explore some of these vector stores in upcoming lessons.
    
# 1. Chroma Vector Store:
Chroma is an open-source vector database that is designed to handle high-dimensional vector data efficiently. It provides a simple and intuitive interface for storing, indexing, and retrieving vectors, making it ideal for applications involving embeddings and semantic search. It is lightweight and easy to set up, making it a popular choice for developers looking to integrate vector storage capabilities into their applications.

It has features of Vector Store + some Database functionalities. RDBMS features are also present.

Check code in google colab : 

    
    