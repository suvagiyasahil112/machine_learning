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
driver.get("https://jogiayurved.com/prakriti/")

# button1 = driver.find_element(By.CLASS_NAME,"")
# time.sleep(2)

product_titles_text=[]
Option1=[]
Option2=[]
Option3 = []
for i in range (30):
    # next_que_name=f"next-q{i}"

    product_titles = driver.find_elements(By.CLASS_NAME, "question")
    product_titles_text0 = [title.text for title in product_titles]
    product_titles_text.append(product_titles_text0)
    button_1 = driver.find_element(By.NAME,'q1')
    button_1.click()
    time.sleep(2)
    button_2 = driver.find_element(By.ID,f"next-que{i}")
    button_2.click()
    time.sleep(2)


df=pd.DataFrame(product_titles_text)     
print(df)

# ==============

# button1.click()

# time.sleep(2)
# button2 = driver.find_element(By.XPATH,'//*[@id="theme-app"]/div/div/header/ul/li[1]/a')
# button2.click()
# time.sleep(2)
# search_box = driver.find_element(By.XPATH,'//*[@id="search-home-form-combo-input"]')

# time.sleep(2)
# search_box.send_keys("shirt")
# time.sleep(2)
# search_box.send_keys(Keys.RETURN)

# time.sleep(2)
# man2 = driver.find_element(By.XPATH,'//*[@id="theme-app"]/div/div/header/div[2]/div[2]/div[1]/ul/li[2]/button')
# man2.click()

# time.sleep(10)
# product_titles = driver.find_elements(By.TAG_NAME,"h2")
# product_titles_texts = [title.text for title in product_titles]
# df= pd.DataFrame(product_titles_texts,columns=["product title"])
# print(df)
time.sleep(5)
driver.quit()
