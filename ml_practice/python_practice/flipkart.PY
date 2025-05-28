from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import time

chrome_options = Options()
chrome_options.binary_location = r"C:\Users\Sahil\AppData\Local\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.flipkart.com/")

try:
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    None
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    time.sleep(20)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cPHDOP"))
    )
    time.sleep(200)
    product_titles = driver.find_elements(By.CLASS_NAME, "KzDlHZ")

    product_titles_text = [title.text for title in product_titles]

    df = pd.DataFrame(product_titles_text, columns=["Product Title"])

    print(df)

except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()
