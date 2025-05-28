import pandas as pd
import requests
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import random 


api_key ="7VZE093SOD8UIF0X"
symbol = "AAPL"

url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
responce= requests.get(url)
data= responce.json()
time_series = data.get("Time Series (Daily)", {})
df=pd.DataFrame.from_dict(time_series,orient="index")
print(df.head())

df.columns=["open","high","low","close","volume"]

df=df.astype(float)
df.index=pd.to_datetime(df.index)
df=df.sort_index()

df["SMA_5"] = df["close"].rolling(window=5).mean()
print(df.tail())

plt.figure(figsize=(10,5))
sns.lineplot(x=df.index,y=df["close"])
plt.title("Daily Close ")
plt.xlabel=("Date")
plt.ylabel=("Price")
plt.grid=True
plt.show()
