
# Real-Time Detection of Bot or Fake Accounts on Instagram using unsupervised learning

# EAAJ2llrGqn8BO9jPFcRJBV6ztbAYd6fzd478jW2fHzvUJBmMd0mrMZCOd3Apn6PhUy0lmblZA910ZBKpGIsExEoZBIoMrYL2RGAk7Rj5nXCpdEgCKcnNf1CZAu4hZCMl0cTAxXP6wvv8kidD6r0nZCWBhLLgSzF2HNKXTkEY8aF9CAoVTPrBwiIma442eseVUSwdpwkM3AYgUVUcrTSBgidFQlXT6ILCjexyLXiZCnvPigZDZD
# {
#   "id": "1233187525167504",
#   "name": "Sahil Suvagiya"
# }


# 1. Data Collection
# Collect Instagram account behavior data such as:
# Post frequency (posts per day/week)
# Follower growth rate (followers gained over time)
# Following/follower ratio
# Average likes/comments per post
# Time between posts
# Interaction patterns (e.g., likes/comments given to others)
# You can collect data via Instagram Graph API (requires permissions) or by scraping publicly available data responsibly (watch for TOS compliance).



# 2. Feature Extraction
# Process raw data into numeric features for each account:
# posts_per_day
# avg_follower_growth_rate
# follower_following_ratio
# avg_likes_per_post
# avg_comments_per_post
# avg_time_between_posts
# engagement_rate = (likes + comments) / followers
# Normalize or scale features to make clustering effective.




# 3. Real-Time Setup
# Use a streaming platform or schedule frequent data pulls to update features continuously.
# Store features in a database or in-memory store for quick access.




# 4. Unsupervised Learning: Clustering & Anomaly Detection
# Use clustering algorithms like DBSCAN or Isolation Forest for anomaly detection:
# DBSCAN: Detects clusters and labels points outside clusters as outliers.
# Isolation Forest: Specifically designed to detect anomalies.
# Alternatively, use Autoencoders for anomaly detection by measuring reconstruction error.





# 5. Detect Bots or Fake Accounts
# Accounts identified as outliers or in very small clusters with unusual behavior are flagged as potential bots/fakes.
# Output real-time alerts or dashboards for further manual review.





# 6. Visualization
# Build a dashboard using Streamlit or Dash showing:
# Clusters of accounts
# Highlighted suspicious accounts
# Time series graphs of follower growth or post frequencyimport pandas as pd


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
import cv2

import io
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from deep_translator import GoogleTranslator
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"




chrome_options = Options()
chrome_options.binary_location = r"C:\Users\Sahil\AppData\Local\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.instagram.com/accounts/edit/")

time.sleep(3)
email= "kakashi_from_leaf"
password_insta = "Sahil_0240"


mail = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_aa48'
))
        )
mail.send_keys(email)
time.sleep(3)

password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "password"))  # Use appropriate locator
)
password.send_keys(password_insta)

time.sleep(3)
login_btn = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]')
login_btn.click()

time.sleep(5)

x_btn = driver.find_element(By.CSS_SELECTOR,'x3nfvp2 x1n2onr6 xh8yej3')

x_btn.click()
time.sleep(8)
driver.quit()