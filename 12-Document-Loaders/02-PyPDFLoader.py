'''
PyPDFLoader Example
--------------------
This script demonstrates how to use the PyPDFLoader from the langchain_community package to load and process PDF documents. The loader reads the content of a PDF file and converts it into a standardized Document object that can be further processed in a RAG system.

syntax:

Document(
    page_content: str,
    metadata: dict = None
)

Simple, clean PDFs - PyPDFLoader

PDFs with tables/columns - PDFPlumberLoader

Scanned/image PDFs - UnstructuredPDFLoader, AmazonTextractPDFLoader

Need layout and image data - PyMuPDFLoader

Want best structure extraction - UnstructuredPDFLoader


'''

from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('Cyber_Security_-_Report.pdf')
docs=loader.load()  # returns a list of Document objects
print(docs)
# Accessing content and metadata of the first document
print(docs[0].page_content)
print(docs[0].metadata)