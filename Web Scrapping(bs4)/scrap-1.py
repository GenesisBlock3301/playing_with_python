import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
html = list(soup.children)[2]
# print(html)
body = list(html.children)[3]
p = list(body.children)[1]
print(p.get_text())