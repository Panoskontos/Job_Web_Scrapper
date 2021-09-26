from bs4 import BeautifulSoup
import requests
import re

#A remote jobs website
html = requests.get("https://remote.co/remote-jobs/developer/").text

soup = BeautifulSoup(html,'lxml')

#I will test it for 1 job first
job = soup.find('div', class_='col position-static')

# And then for all
jobs = soup.find_all('div', class_='col position-static')

i = 1
for job in jobs:
    comp_job=job.find('span', class_="font-weight-bold larger").text
    company = job.find('p', class_="m-0 text-secondary").text
    company = re.sub(r"[\n\t\s]*","",company)
    print(f"{i}.Job: {comp_job}\nCompany: {company}\n")
    i=i+1