# 6Task: Customer Lifetime Value (CLV) Calculation
# •Task: Using transaction data (with CustomerID, TransactionDate,
#  and AmountSpent), calculate the Customer Lifetime Value (CLV) using the historical method,
#  considering the average purchase frequency and average revenue per user (ARPU).


import pandas as pd
import numpy as np
import random

df=pd.read_csv("customer_segmentation.csv", encoding='ISO-8859-1')
print(df.head(5))

# print(df)

df["revenue"]=df["UnitPrice"]*df["Quantity"]
# print(df.head(3))

df["cost"]=df["UnitPrice"]*(0.66)
# print(df.head())


grouped_df=df.groupby("CustomerID").agg(
    total_revenue=("revenue","sum"),
    total_cost=("cost","sum"))
# print(grouped_df)

grouped_df["customer lifetime value"]=grouped_df["total_revenue"]-grouped_df["total_cost"]


# grouped_df=grouped_df.sort_values(by="customer lifetime value",ascending=False)
print(grouped_df)
