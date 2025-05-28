import pandas as pd
import requests
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import random 


# api_key = "37SQKVMTM3SS091S"
# symbol =  "AAPL"
# # url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"
# url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

# responce = requests.get(url)
# data =responce.json()

# timeseries = data.get("Time Series (Daily)",{})

# df =pd.DataFrame.from_dict(timeseries,orient="index")
df= pd.read_csv("slqapidata.csv")

# print(df)

# df.columns=["open","high","low","colse","volume"]
# cols = ["open", "high", "low", "close", "volume"]
# df.columns=cols
# df=df.astype(float)
# df.index=pd.to_datetime(df.index)

df=df.sort_index()
# print(df.head())
# print("\n\n\n\n\n\n\n")
df["SMA_5"] = df["close"].rolling(window=5).mean()
# print(df.tail())

# print(df.describe())

# df["Close"].plot(figsize=(10,5), title="Stock Closing Price", xlabel="Date", ylabel="Price", grid=True)
# df["close"].plot(figsize=(10,5),title="Daily_colse",xlabel="Date",ylabel="Price",grid=True),
# plt.show()

plt.figure(figsize=(10,5))
sns.lineplot(x=df.index,y=df["close"])
plt.title("Daily Close ")
plt.xlabel=("Date")
plt.ylabel=("Price")
plt.grid=True
plt.show()

