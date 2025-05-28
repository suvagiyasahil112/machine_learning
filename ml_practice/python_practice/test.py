# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # URL of the webpage containing the data
# url = "https://www.worldometers.info/coronavirus/"

# # Fetch the HTML content
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find the table (modify according to the structure of your webpage)
# table = soup.find('table')  

# # Extract table rows
# data = []
# for row in table.find_all('tr'):  # Loop through rows
#     cols = [col.text.strip() for col in row.find_all(['td', 'th'])]  # Get text
#     data.append(cols)

# # Convert to Pandas DataFrame
# df = pd.DataFrame(data)

# # Display the first few rows
# print(df.head())

# # Save to CSV (optional)
# df.to_csv("output.csv", index=False)



# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import matplotlib.pyplot as plt
# import time
# import re  # Import re for regex

# time.sleep(5)  # Pause between requests
# import random

# USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
# ]

# HEADERS = {
#     "User-Agent": random.choice(USER_AGENTS),
#     "Accept-Language": "en-US,en;q=0.9",
#     "Referer": "https://www.indeed.com/",
# }


# BASE_URL = "https://www.indeed.com/jobs?q={}&start={}"
# PROXIES = {
#     "http": "http://username:password@proxy-server:port",
#     "https": "http://username:password@proxy-server:port",
# }

# response = requests.get(BASE_URL, headers=HEADERS, proxies=PROXIES)

# def fetch_job_listings(keyword, pages=5):
#     jobs = []
#     for page in range(0, pages * 10, 10):
#         url = BASE_URL.format(keyword, page)
#         response = requests.get(url=url, headers=HEADERS)
        
#         if response.status_code != 200:
#             print(f"Failed to fetch data. Status code: {response.status_code}")
#             continue  # Skip this page if request fails
        
#         soup = BeautifulSoup(response.text, 'html.parser')
#         job_cards = soup.find_all('div', class_='job_seen_beacon')

#         for job in job_cards:
#             title = job.find('h2', class_='jobTitle')
#             company = job.find('span', class_='companyName')
#             location = job.find('div', class_='companyLocation')
#             salary = job.find('div', class_='attribute_snippet')

#             jobs.append({
#                 'title': title.text.strip() if title else None,
#                 'company': company.text.strip() if company else None,
#                 'location': location.text.strip() if location else None,
#                 'salary': salary.text.strip() if salary else None
#             })
        
#         time.sleep(2)  # Avoid making too many requests quickly
    
#     return pd.DataFrame(jobs)

# def clean_salary(salary):
#     if not salary:
#         return None

#     salary = re.sub(r'[^0-9-]', '', salary)  # Use re.sub instead of requests.sub

#     if '-' in salary:
#         try:
#             min_salary, max_salary = map(int, salary.split('-'))
#             return (min_salary + max_salary) / 2
#         except ValueError:
#             return None  # Handle unexpected formats safely
#     try:
#         return int(salary)
#     except ValueError:
#         return None

# def clean_data(df):
#     df = df.dropna(subset=['title', 'company', 'location'])
#     df['salary'] = df['salary'].apply(clean_salary)
#     df = df.dropna(subset=['salary'])
#     return df

# def visualize_data(df):
#     top_cities = df['location'].value_counts().nlargest(10)
    
#     # Bar chart for job listings per city
#     plt.figure(figsize=(10,5))
#     top_cities.plot(kind='bar', color='skyblue')
#     plt.title("Top Cities with Most Job Listings")
#     plt.xlabel("City")
#     plt.ylabel("Number of Jobs")
#     plt.xticks(rotation=45)
#     plt.show()

#     # Histogram for salary distribution
#     plt.figure(figsize=(10,5))
#     plt.hist(df['salary'], bins=20, color='green', edgecolor='black')
#     plt.title("Salary Distribution")
#     plt.xlabel("Salary ($)")
#     plt.ylabel("Frequency")
#     plt.show()

#     # Boxplot for salary variations by city
#     top_cities_list = top_cities.index.tolist()
#     df_filtered = df[df['location'].isin(top_cities_list)]
    
#     plt.figure(figsize=(12,6))
#     df_filtered.boxplot(column=['salary'], by='location', rot=45)
#     plt.title("Salary Variations by City")
#     plt.suptitle("")
#     plt.xlabel("City")
#     plt.ylabel("Salary ($)")
#     plt.show()

# # Run the script
# keyword = "Data Scientist"
# df = fetch_job_listings(keyword)
# df = clean_data(df)

# if not df.empty:
#     visualize_data(df)
# else:
#     print("No data available after cleaning.")



# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import matplotlib.pyplot as plt
# import re
# import time
# HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# BASE_URL = "https://www.indeed.com/jobs?q={}&start={}"
# def fetch_job_listings(keyword, pages=5):
#     jobs = []
#     for page in range(0, pages * 10, 10):
#         url = BASE_URL.format(keyword, page)
#         response = requests.get(url, headers=HEADERS)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         job_cards = soup.find_all('div', class_='job_seen_beacon')
#         for job in job_cards:
#             title = job.find('h2', class_='jobTitle')
#             company = job.find('span', class_='companyName')
#             location = job.find('div', class_='companyLocation')
#             salary = job.find('div', class_='attribute_snippet')
#             jobs.append({
#                 'title': title.text.strip() if title else None,
#                 'company': company.text.strip() if company else None,
#                 'location': location.text.strip() if location else None,
#                 'salary': salary.text.strip() if salary else None
#             })
#         time.sleep(2)
#     return pd.DataFrame(jobs)
# def clean_salary(salary):
#     if not salary:
#         return None
#     salary = re.sub(r'[^0-9-]', '', salary)
#     if '-' in salary:
#         min_salary, max_salary = map(int, salary.split('-'))
#         return (min_salary + max_salary) / 2
#     return int(salary)
# def clean_data(df):
#     df = df.dropna(subset=['title', 'company', 'location'])
#     df['salary'] = df['salary'].apply(clean_salary)
#     df = df.dropna(subset=['salary'])
#     return df
# def visualize_data(df):
#     top_cities = df['location'].value_counts().nlargest(10)
#     plt.figure(figsize=(10,5))
#     top_cities.plot(kind='bar', color='skyblue')
#     plt.title("Top Cities with Most Job Listings")
#     plt.xlabel("City")
#     plt.ylabel("Number of Jobs")
#     plt.xticks(rotation=45)
#     plt.show()
#     plt.figure(figsize=(10,5))
#     plt.hist(df['salary'], bins=20, color='green', edgecolor='black')
#     plt.title("Salary Distribution")
#     plt.xlabel("Salary ($)")
#     plt.ylabel("Frequency")
#     plt.show()
#     df.boxplot(column=['salary'], by='location', rot=45, figsize=(12,6))
#     plt.title("Salary Variations by City")
#     plt.suptitle("")
#     plt.xlabel("City")
#     plt.ylabel("Salary ($)")
#     plt.show()
# keyword = "Data Scientist"
# df = fetch_job_listings(keyword)
# df = clean_data(df)
# visualize_data(df)







# ============================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import time



chrome_driver_path = r"D:\python_practice\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.zara.com/")

button1 = driver.find_element(By.CLASS_NAME,"zds-button")
time.sleep(2)

button1.click()

time.sleep(2)
button2 = driver.find_element(By.XPATH,'//*[@id="theme-app"]/div/div/header/ul/li[1]/a')
button2.click()
time.sleep(2)
search_box = driver.find_element(By.XPATH,'//*[@id="search-home-form-combo-input"]')

time.sleep(2)
search_box.send_keys("shirt")
time.sleep(2)
search_box.send_keys(Keys.RETURN)

time.sleep(2)
man2 = driver.find_element(By.XPATH,'//*[@id="theme-app"]/div/div/header/div[2]/div[2]/div[1]/ul/li[2]/button')
man2.click()

time.sleep(5)
product_titles = driver.find_elements(By.TAG_NAME,"h2")
product_titles_texts = [title.text for title in product_titles]
df= pd.DataFrame(product_titles_texts,columns=["product title"])
print(df)

# driver.save_screenshot("Aqqqqqqqqqqqqqqqq.png")
driver.quit()

df= df.drop(columns=[0,1,2,3,41],axis=0)
print(df.head())