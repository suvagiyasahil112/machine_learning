import pandas as pd
import requests
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import random 

api_key ="bae90eb65677e04efbc5b034e49e2894"
lat="23"
lon="72"

url =f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}"
responce = requests.get(url)
data=responce.json()
list =data.get("list",{})

df= pd.DataFrame.from_dict("list",orient="index")

print(df.head())