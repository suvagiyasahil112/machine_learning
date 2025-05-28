import pandas as pd 
import numpy as np 
import random
import matplotlib.pyplot as plt 
import seaborn as sns 
from bs4 import BeautifulSoup 
import requests
headers = {"User-Agent": "Mozilla/5.0"}
url ="https://www.naukri.com/mnjuser/recommendedjobs"
responce = requests.get(url,headers=headers)
if responce.status_code==200:
    soup= BeautifulSoup(responce.text,"html.parser")
    title=soup.title.text.strip()
    print("TITLE:---------->",title)
    # class1 = soup.find_all("div", class__ ="list")
    article= soup.find_all("article",class_="oneThemeTuple  ")
    # aas=soup.find_all_next("div")
    
    for i in article:
        print(i)  


else :
    print(f"failed to retrive the page.Exception code:{responce.status_code}")

