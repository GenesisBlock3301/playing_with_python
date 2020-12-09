import requests
from bs4 import BeautifulSoup

url = "https://www.monster.com/jobs/search/?q=software__2Ddeveloper&where=bangladesh"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
results = soup.find(id="ResultsContainer")

job_elements = results.find_all('section', class_="card-content")
# print(job_elements)
file = open('scrapping_data.txt','a+',encoding='utf-8')
for job_elem in job_elements:
    title_ele = job_elem.find('h2',class_='title')
    company_ele = job_elem.find('div',class_='company')
    location_ele = job_elem.find('div',class_='location')
    time = job_elem.find('div',class_='meta')
    if None in (title_ele,company_ele,location_ele,time):
        continue
    print("Title: ",title_ele.text.strip())
    print("Company Name:",company_ele.text.strip())
    print("Lacation: ",location_ele.text.strip())
    print("Time: ",' '.join(time.text.strip().split()[0:2]))
    file.write(f"Title: {title_ele.text.strip()}\nCompany Name: {company_ele.text.strip()}\n"
               f"Time: {' '.join(time.text.strip().split()[0:2])}\n---------------------------\n")
    # file.write(f"Company Name: {company_ele.text.strip()}")
    # file.write(f"Time: {time.text.strip()}")
file.close()