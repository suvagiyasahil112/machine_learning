# ---------------------1---------------------------------

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# chrome_driver_path = r"D:\python_practice\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# service = Service(chrome_driver_path)

# driver = webdriver.Chrome(service=service)

# driver.get("https://spectricssolutions.com/")

# print(driver.title)
# driver.quit()


# -------------------------2---------------------------------------------------------

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

# driver.get("https://spectricssolutions.com/")


# element_by_class1 = driver.find_element(By.CLASS_NAME,"navbar-brand")

# element_by_class2 = driver.find_element(By.CLASS_NAME,"sub-high")

# element_by_class3 = driver.find_element(By.CLASS_NAME,"title")
# print(element_by_class1.text)
# print(element_by_class2.text)
# print(element_by_class3.text)

#----------------------- by xpath -------------------------

# element_by_xpath =driver.find_element(By.XPATH,"/html/body/section[3]/div/div[1]/div/p")
# print(element_by_xpath.text)
# -----------------------draft -----------------------------------------

# driver.get("https://www.google.com/")

# element_by_class1 = driver.find_element(By.ID,"APjFqb")

# search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
# None
# search_box.send_keys("laptop")

# search_box.send_keys(Keys.RETURN)
# time.sleep(20)

# print(element_by_class1.text)


# ------------------------keys ----------------------------------------------------


driver.get("https://www.zara.com/")
button = driver.find_element(By.CLASS_NAME,"zds-button")
time.sleep(10)

button.click()
# time.sleep(10)
button2 =driver.find_element(By.CLASS_NAME,"layout-header-action layout-header-action-search")
button2.click()
# time.sleep(10)
# search_box= driver.find_element(By.CLASS_NAME,"search-home-form-combo-input")
search_box= WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(By.CLASS_NAME, "search-home-form-combo-input")
    )
# None

search_box.send_keys("shirt")
search_box.send_keys(Keys.RETURN)

driver.quit()


