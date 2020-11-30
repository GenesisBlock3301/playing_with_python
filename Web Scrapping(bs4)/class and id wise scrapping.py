import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
p = soup.find_all('p',class_="outer-text")
print(p)