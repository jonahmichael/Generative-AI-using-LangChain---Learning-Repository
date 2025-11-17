from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader=DirectoryLoader(
    path='books',  # Path to the directory containing PDF files
    glob='**/*.pdf',  # Pattern to match all PDF files recursively
    loader_cls=PyPDFLoader  # Specify the loader class for PDF files
)

docs = loader.load()  # Load the documents
print(len(docs))  # Print the number of documents loaded  



