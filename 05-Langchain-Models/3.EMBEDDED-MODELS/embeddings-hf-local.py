from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=["Delhi is the capital of India", "Paris is the capital of France", "Tokyo is the capital of Japan", "Canberra is the capital of Australia", "Ottawa is the capital of Canada", "Berlin is the capital of Germany"]
result=embedding.embed_documents(documents)
print(str(result))