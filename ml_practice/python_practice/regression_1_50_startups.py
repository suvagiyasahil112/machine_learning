import pandas as pd
import numpy as np
import math
import sklearn
from sklearn.preprocessing  import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt


df = pd.read_csv('50_Startups.csv')

print(len(df))

df.columns = df.columns.str.strip()



plt.figure(figsize=(12,6))
# plt.scatter(df['Marketing Spend'],df['Profit'],alpha=0.5)
# plt.title ("scatter plot of profit woith marketing spent")

# plt.xlabel("marketing spend")
# plt.ylabel("profit")
# plt.show()
