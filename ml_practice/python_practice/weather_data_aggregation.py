import numpy as np
import pandas as pd 
import random

df=pd.read_csv('ahmedabad.csv')
# print(data)

avg_temp=np.sum(df["temp"])/(len(df["temp"]))

print("average daily temprature:",avg_temp)

avg_humidity=np.sum(df["humidity"])/(len(df["humidity"]))

print("average daily humidity:",avg_humidity)

