from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='D:\\Learning Stuffs\\Langchain\\12-Document-Loaders\\titanic.csv')  # Path to the CSV file
docs=loader.load()  # Load the documents from the CSV file
print(docs[0].page_content)   