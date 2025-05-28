# asjcajk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Initialize the WebDriver
chrome_driver_path = r"D:\python_practice\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://jogiayurved.com/prakriti/")

product_titles_text = []

for i in range(30):  # Iterate over 30 questions
    try:
        # Wait for the question element to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "quiz"))
        )
        product_titles = driver.find_elements(By.CLASS_NAME, "question")
        product_titles_text.append([title.text for title in product_titles])

        # Click the answer button (Make sure "q1" is correct)
        q=1
        button_1 =driver.find_element((By.NAME, f"q{q+1}"))
        
        q+=1
        button_1.click()
        time.sleep(2)

        # Click the next button (Check actual ID structure on website)
        u=0
        button_2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, f"next-q{u+1}"))
        )
        u+=1
        button_2.click()
        time.sleep(2)

    except Exception as e:
        print(f"Error on iteration {i}: {e}")
        break  # Stop loop if an error occurs

# Convert to DataFrame
df = pd.DataFrame(product_titles_text)


# Close the driver
driver.quit()
print(df.head())