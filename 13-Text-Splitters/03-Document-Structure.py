'''
Document Structure Splitter

This example demonstrates how to use a document structure-based text splitter to divide a large text into smaller chunks based on its inherent structure, such as paragraphs or sections. This method is particularly useful for documents that have clear structural elements, allowing for more meaningful and context-aware splitting.

For example; we need to spliit a content of a markdown file based on its headings, subheadings, and paragraphs.
 or based on sections in a legal document.
 
 or based on functions and classes in a code file. 
'''

from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_summary(self):
        return self.content[:100]  # Return the first 100 characters as a summary
    
    def get_word_count(self):
        return len(self.content.split())

"""


splitter=RecursiveCharacterTextSplitter(
    Language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0 # no overlapping text between chunks check below for more details
    
)

result=splitter.split_text(text)
print(result)
print(f"Total Chunks: {len(result)}")