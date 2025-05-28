import pandas as pd
import numpy as np   
import random


df=pd.read_csv("churn.csv")
# print(data)

churns=df["Churn"].value_counts()

print(churns)
total=np.sum(churns)
print("TOTAL:",total)


churn_rate=pd.Series.value_counts(df["Churn"])
# print("",churn_rate)
churned=(churn_rate["Yes"])/total

print(f"churn rate:{churned*100}% ")