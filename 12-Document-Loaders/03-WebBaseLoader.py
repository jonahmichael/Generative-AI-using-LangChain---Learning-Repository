'''
In WebBaseLoader, we can load documents from a list of URLs.

it uses beautifulsoup4 and requests libraries to fetch and parse web pages. (web scrapping libraries) + Requests is used to make HTTP requests to fetch the web pages, and BeautifulSoup is used to parse the HTML content of those pages.

When to use WebBaseLoader:
- When you need to extract text content from web pages for further processing.
- for blogs, news articles, or any web-based content that are static in nature.

Limitations:
- It may not handle dynamic content loaded via JavaScript.
- for that we can use other loaders like SeleniumLoader or PlaywrightLoader.



'''

from langchain_community.document_loaders import WebBaseLoader
url="https://www.flipkart.com/samsung-galaxy-f07-green-64-gb/p/itm294cbb65839e6?pid=MOBHDVFKSF3YZQNK&lid=LSTMOBHDVFKSF3YZQNKT3DGZG&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=CLP_Filters&fm=organic&iid=en_0m_hKp3yqjyIT_fONiGx49orA3fnpfU3EFK-IPTueKkH0TNiPkXY8e_19Wl2jqejxHRr1_EPcPoNj7rAHW7WPA%3D%3D&ppt=clp&ppn=mobile-phones-store&ssid=ot4f8gfe0g0000001763385145700"   # we can also provide list of urls here adn also every url is considered as separate document
loader=WebBaseLoader(url)

docs=loader.load()
print(docs[0].page_content)