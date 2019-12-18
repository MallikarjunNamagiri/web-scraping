import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.com/jobs/search/?q=Machine-Learning-Engineer&where=Bangalore"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
jobelements = results.find_all('section', class_='card-content')

# find Job Elements
for JobElement in jobelements:
    title_ele = JobElement.find('h2', class_='title')
    company_ele = JobElement.find('div', class_='company')
    location_ele = JobElement.find('div', class_='location')
    # Extract Text From HTML Elements
    if None in (title_ele, company_ele, location_ele):
        continue
    '''print(title_ele)
    print(company_ele)
    print(location_ele)'''
    print(title_ele.text.strip())
    print(company_ele.text.strip())
    print(location_ele.text.strip())
    print()