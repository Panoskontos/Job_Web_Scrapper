from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

#A remote jobs website
html = requests.get("https://remote.co/remote-jobs/developer/").text

soup = BeautifulSoup(html,'lxml')

#I will test it for 1 job first
job = soup.find('div', class_='col position-static')

# And then for all
jobs = soup.find_all('div', class_='col position-static')

# Will add our data to the list
my_jobs = []
my_companies=[]

for job in jobs:
    comp_job=job.find('span', class_="font-weight-bold larger").text
    my_jobs.append(comp_job)
    company = job.find('p', class_="m-0 text-secondary").text
    #some string manipulation
    company = re.sub(r"[\n\t\s]*","",company)
    company_sliced = company.split("|")
    company = company_sliced[0]
    # ------------------------ #
    my_companies.append(company)
    print(f"{i}.Job: {comp_job}\nCompany: {company}\n")

#Creating a dictionary
mydict = {"Jobs": my_jobs,
       "Companies": my_companies}

#Coverting it into a dataframe with all our data
df = pd.DataFrame(mydict)

#extracting our data to a csv file
df.to_csv("jobs.csv", index=False)