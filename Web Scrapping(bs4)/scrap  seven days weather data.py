import requests
from bs4 import BeautifulSoup


page = requests.get("http://127.0.0.1:8000/shop/")
# print(page.content)
soup = BeautifulSoup(page.content,'html.parser')

# docType = soup.children
# print(list(docType))
a = soup.find_all('a')

for i in a:
    print(i.get_text())