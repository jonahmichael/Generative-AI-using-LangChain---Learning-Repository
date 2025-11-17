from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader=DirectoryLoader(
    path='books',  # Path to the directory containing PDF files
    glob='**/*.pdf',  # Pattern to match all PDF files recursively
    loader_cls=PyPDFLoader  # Specify the loader class for PDF files
)

docs = loader.load()  # Load all the documents at once
docs1=loader.lazy_load()  # Lazy load(loads as when needed instead of at once) the documents
print(len(docs))  # Print the number of documents loaded  
print(len(list(docs1)))  # Print the number of documents loaded lazily



