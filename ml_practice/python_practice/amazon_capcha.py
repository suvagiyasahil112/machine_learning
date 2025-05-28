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
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import pytesseract 
from PIL import ImageDraw,ImageFont
from PIL import ImageFilter
import pytesseract
import cv2test

import io
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from deep_translator import GoogleTranslator
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


chrome_options = Options()
chrome_options.binary_location = r"C:\Users\Sahil\AppData\Local\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.amazon.in/")

try:
    capcha_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "captcha")]'
))
        )
    location = capcha_element.location
    size= capcha_element.size
    x,y = location['x'],location['y']
    width,height = size['width'],size['height']
    print(f"capcha position : X={x},Y={y},Width={width},Height={height}")
    driver.save_screenshot("amazon_fllpage.png")
    # driver.quit()
    img=cv2test.imread("amazon_fllpage.png")
    cropped_capcha= img[y:y+height,x:x+width]
    chrome_options.add_experimental_option("detach", True)  
    captcha_text = pytesseract.image_to_string(cropped_capcha, config="--psm 6")
    print("\n")
    print("Extracted CAPTCHA:", captcha_text)
    print("\n")

    try:
            box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "captchacharacters"))
            )

            box.send_keys(captcha_text)
            box.send_keys(Keys.RETURN)
            time.sleep(2)
    except Exception as TimeoutException:
        print("CAPTCHA input box not found, skipping CAPTCHA solving.")
    

    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    None
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "s-main-slot"))
    )

    
    product_titles = driver.find_elements(By.TAG_NAME, "h2")

    product_titles_text = [title.text for title in product_titles]

    df = pd.DataFrame(product_titles_text, columns=["Product Title"])
    print(df)

except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()
