'''
Length Based Text Splitter Example
-------------------------------

This example demonstrates how to use a length-based text splitter to divide a large text into smaller chunks based on a specified maximum length.

Advantages of Length-Based Splitting:
- Simple and straightforward to implement.
- Effective for texts where logical breaks are not necessary.

Disadvantages:
- May split sentences or paragraphs inappropriately.
- Does not consider semantic meaning or context.


'''

from langchain_text_splitters import CharacterTextSplitter
text="In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available."

splitter=CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0, # no overlapping text between chunks check below for more details
    separator=" "
)

result=splitter.split_text(text)
print(result)

'''
chunk over lap is set to 0, meaning there will be no overlapping text between chunks i.e each chunk will be distinct and separate from the others and the separator is set to a space character, ensuring that the text is split at word boundaries rather than in the middle of words.
'''