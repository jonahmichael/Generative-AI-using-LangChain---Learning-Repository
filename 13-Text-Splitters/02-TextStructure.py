'''
Text Structure Splitter

Here the text structure splitter is used to split the text based on its inherent structure, such as paragraphs or sections.
This is particularly useful for documents that have clear structural elements, allowing for more meaningful and context-aware splitting.

Example: in paragraphs,list items etc.

para -> lines -> words -> characters

which means that it will chunk the text first by paragraphs, then by lines within those paragraphs, then by words within those lines, and finally by characters within those words. but all this chunking is based on the number that we provide.

eg; I live in India.
chunk_size = 2
The above text will be chunked as:
1. I live
2. in India.

'''

from langchain_text_splitters import RecursiveCharacterTextSplitter

text="In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available."

splitter=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0 # no overlapping text between chunks check below for more details
    
)

result=splitter.split_text(text)
print(result)