# web_scraping.py
import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=python+developer"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

job_listings = []
for job in soup.find_all('div', class_='jobsearch-SerpJobCard'):
    title = job.find('h2', class_='title').text.strip()
    company = job.find('span', class_='company').text.strip()
    location = job.find('span', class_='location').text.strip()
    salary = job.find('span', class_='salary').text.strip() if job.find('span', class_='salary') else None

    job_listings.append({'title': title, 'company': company, 'location': location, 'salary': salary})
