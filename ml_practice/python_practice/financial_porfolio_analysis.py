#  Given daily stock price data for multiple stocks,
#  compute the daily returns, calculate the portfolio's weighted returns,
#  and perform a risk analysis (standard deviation) of the portfolio.


# •Task: Given daily stock price data for multiple stocks,
#  compute the daily returns, calculate the portfolio's weighted returns,
# #  and perform a risk analysis (standard deviation) of the portfolio.

import datetime as dt
import pandas as pd
import numpy as np
import random

df=pd.read_csv("ADANIPORTS.csv")



#  (Today's closing price - Yesterday's closing price) / Yesterday's closing price) x 100%; essentially


today_close=list(df["Close"])
prev_close=list(df["Prev Close"])

daily_returns=[]
for i in range (len(df)):
    returns=((today_close[0]-prev_close[0])/prev_close[0])-1
    today_close.pop(0)
    prev_close.pop(0)

    daily_returns.append(returns)

# TWRR = (1 + R1) * (1 + R2) * ... (1 + Rn) - 1 
# In this formula, R is the simple return for each time period,
#  which is calculated using the formula: R = (Ve - Vb) / Vb. 


df["daily return"]=daily_returns
o=1
wt=[]
for i in range(len(df)):
    weight=(o+df["daily return"][i])
    wt.append(weight)

df["daily return"]=np.multiply(df["daily return"],100)
# print(df["daily return"])
df["wt"]=wt


print(wt)
wtt=list(wt)

multiple=1.0
for i in range (len(wt)):
    multiple=multiple*wtt[i]
    

weighted_return=multiple
weighted_return-1

print("weighted return:",weighted_return)

sd=np.std(df["daily return"])
print("stanndard deviation of daily returns",sd)

