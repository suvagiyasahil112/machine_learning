
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

service = Service("D:\python_practice\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # Update with your actual path
browser = webdriver.Chrome(service=service, options=chrome_options)

# url = "https://www.zara.com/in/" 
url = "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss"
browser.get(url)

time.sleep(2)  
total_height = browser.execute_script("return document.body.scrollHeight")
view_height = browser.execute_script("return window.innerHeight")


browser.set_window_size(1920, total_height)
time.sleep(2) 
screenshot_path = "full_page_screenshot.png"
browser.save_screenshot(screenshot_path)
print(f"Full-page screenshot saved as {screenshot_path}")
browser.quit()
