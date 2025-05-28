# •Task 2:
# •Job Market Analysis
# •Scrape job listings (title, company, salary, location) from Indeed.
# •Use Pandas to filter high-paying jobs in a given field.
# •Create bar charts of job trends per city using Matplotlib.
# •Scraping Job Listings
# •Fetches job title, company, salary, and location from Indeed.
# •Loops through multiple pages to get more jobs.
# •Uses headers to avoid blocking.
# •:white_check_mark: Data Cleaning & Salary Extraction
# •Handles missing salaries and extracts min/max salary values.
# •Removes incomplete data for accuracy.
# •Filters high-paying jobs (e.g., $100,000+).
# •:white_check_mark: Data Analysis & Visualization
#  :bar_chart: Bar Chart – Shows the top cities with the most jobs.
#  :chart_with_upwards_trend: Histogram – Displays salary distribution.
#  :chart_with_downwards_trend: Box Plot – Compares salary variations by city.

# worldometers.infoworldometers.info
# COVID - Coronavirus Statistics - Worldometer
# Daily and weekly updated statistics tracking the number of COVID-19 cases,
#  recovered, and deaths. Historical data with cumulative charts, graphs, and updates.

# import pandas as pd
# import numpy as np 
# from bs4  import BeautifulSoup
# import requests
# import matplotlib.pyplot  as plt 
# import seaborn as sns 

# # url = "https://www.worldometers.info/coronavirus/"
# url="https://in.indeed.com/"
# response = requests.get(url)
# if response.status_code==200:
#     soup=BeautifulSoup(response.text,"html.parser")
#     title =soup.title.text.strip()
#     print(title)
#     td_tags=soup.find_all("td")
#     for i in td_tags[:100]:
#         print(i.text.strip())
#     # print(td_tags)


# else:
#     print(f"Failed to retrive the page. Status code {response.status_code}")
            

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests
import time
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
BASE_URL = "https://www.indeed.com/jobs?q={}&start={}"
def fetch_job_listings(keyword, pages=5):
    jobs = []
    for page in range(0, pages * 10, 10):
        url = BASE_URL.format(keyword, page)
        response = requests.get(url=url, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('div', class_='job_seen_beacon')
        for job in job_cards:
            title = job.find('h2', class_='jobTitle')
            company = job.find('span', class_='companyName')
            location = job.find('div', class_='companyLocation')
            salary = job.find('div', class_='attribute_snippet')
            jobs.append({
                'title': title.text.strip() if title else None,
                'company': company.text.strip() if company else None,
                'location': location.text.strip() if location else None,
                'salary': salary.text.strip() if salary else None
            })
        time.sleep(2)
    return pd.DataFrame(jobs)
def clean_salary(salary):
    if not salary:
        return None
    salary = re.sub(r'[^0-9-]', '', salary)
    if '-' in salary:
        min_salary, max_salary = map(int, salary.split('-'))
        return (min_salary + max_salary) / 2
    return int(salary)
def clean_data(df):
    df = df.dropna(subset=['title', 'company', 'location'])
    df['salary'] = df['salary'].apply(clean_salary)
    df = df.dropna(subset=['salary'])
    return df
def visualize_data(df):
    top_cities = df['location'].value_counts().nlargest(10)
    plt.figure(figsize=(10,5))
    top_cities.plot(kind='bar', color='skyblue')
    plt.title("Top Cities with Most Job Listings")
    plt.xlabel("City")
    plt.ylabel("Number of Jobs")
    plt.xticks(rotation=45)
    plt.show()
    plt.figure(figsize=(10,5))
    plt.hist(df['salary'], bins=20, color='green', edgecolor='black')
    plt.title("Salary Distribution")
    plt.xlabel("Salary ($)")
    plt.ylabel("Frequency")
    plt.show()
    df.boxplot(column=['salary'], by='location', rot=45, figsize=(12,6))
    plt.title("Salary Variations by City")
    plt.suptitle("")
    plt.xlabel("City")
    plt.ylabel("Salary ($)")
    plt.show()
keyword = "Data Scientist"
df = fetch_job_listings(keyword)
df = clean_data(df)
visualize_data(df)