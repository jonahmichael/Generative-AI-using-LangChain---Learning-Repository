# Text Splitting in Langchain

Text Splitting is basically breaking down large chunks of texts into smaller portions. This is useful for various applications such as document processing, information retrieval, and natural language processing tasks.

 In Langchain, text splitters are used to divide text into manageable pieces. This is particularly useful when dealing with large documents or datasets, as it allows for more efficient processing and analysis.

## Text Spliiters are of 4 types:

 ### 1. Character Text Splitter:
They split text based on a specified number of characters. This is useful when you want to ensure that each chunk of text does not exceed a certain length.

### 2. Recursive Character Text Splitter:
This splitter recursively breaks down text into smaller chunks based on character limits, while also considering sentence and paragraph boundaries to maintain context.

### 3. Token Text Splitter:
This splitter divides text based on token counts, which is particularly useful when working with language models that have token limits.

### 4. Recursive Token Text Splitter:
Similar to the Recursive Character Text Splitter, this one breaks down text into smaller chunks based on token limits, while also considering sentence and paragraph boundaries.

But here were are goig to see for 4 types;

### 1. LEngth Based Text Splitter:
This splitter divides text into chunks based on a specified length. It ensures that each chunk does not exceed the defined length, making it easier to process large texts.

### 2. Text Structure Based Text Splitter:
This splitter takes into account the structure of the text, such as paragraphs and sentences, to create more meaningful chunks. It helps preserve context and coherence in the split text.

### 3. Document Structure Based Text Splitter:
This splitter focuses on the overall structure of the document, such as sections and headings, to create chunks that align with the document's organization. This is particularly useful for processing structured documents like reports or articles.

### 4. Semantic Text Splitter:
This splitter uses semantic understanding to divide text into chunks based on meaning and context. It aims to create more relevant and coherent pieces of text for analysis or processing.






