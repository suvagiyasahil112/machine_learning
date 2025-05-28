import random
import pandas as pd
import numpy as np
# 1263 unique

df=pd.read_csv("data.csv")

a=df["Sales"]
# print(a)

total_sales=np.sum(a)
unnique_items = df['Product Name'].drop_duplicates()

# print(unnique_items)
print("Total sales:",total_sales)

unique_items_in_number=len(unnique_items)
print("total unique products:",unique_items_in_number)

average_sales=total_sales/unique_items_in_number
# print("\n")
print("average sales per product:",average_sales)
print("top selling :\n")

tops=df["Product Name"].value_counts(ascending=False)
print(tops.head(5))

