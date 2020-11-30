import requests
from bs4 import BeautifulSoup


page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
# print(page.content)
soup = BeautifulSoup(page.content,'html.parser')

forcast = soup.find_all(id="seven-day-forecast-list")
print(forcast)