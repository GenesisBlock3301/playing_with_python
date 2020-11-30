import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
find_p = soup.find_all('p')
print(find_p[0].get_text())
