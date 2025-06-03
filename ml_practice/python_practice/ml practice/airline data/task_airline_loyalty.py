import pandas as pd
import numpy as np 
import math 
import matplotlib.pyplot as plt
import seaborn as sns


dictionary = pd.read_csv("Airline Loyalty Data Dictionary.csv")
calander = pd.read_csv("Calendar.csv")
loyalty = pd.read_csv("Customer Loyalty History.csv")
activity = pd.read_csv("Customer Flight Activity.csv")
print(dictionary.head(19))
print(dictionary.info())
print(dictionary.describe())


# print(calander.info())

print(activity.info())

# print(loyalty.info())

customers = activity.groupby('Loyalty Number',as_index=False).sum()
print(''' 
sfdaj
      cawfs
      wf
      awfc
      aw''' )
print(customers.head(20))
print(activity.head(20))

final =pd.merge(loyalty,customers,on='Loyalty Number',how='inner')
# print(final.info())

print(final.isnull().sum())
print(final.nunique())


final_encoded = pd.get_dummies(final,columns=['Gender','Loyalty Card'])

print(final_encoded)
# final_encoded.to_csv("123.csv")

# Create a correlation matrix
num = final_encoded.select_dtypes(include=['int64', 'float64', 'boolean']).columns

correlation_matrix = final_encoded[num].corr()

print(final.columns)
final['Cancelled'] = final['Cancellation Year'].notna().astype(int)

print(final.head(12))
final = final.drop(["Cancellation Month","Enrollment Month"],axis=1)

# plt.figure(figsize=(10,8))
# sns.histplot(x=final['Loyalty Card'],y=final["CLV"])

# plt.show()


count_of_enrollment = final.groupby("Enrollment Year")['Loyalty Number'].count().reset_index()

print('count of enrollment ',count_of_enrollment)

cancellation = final.groupby("Cancellation Year")['Loyalty Number'].count().reset_index()
print(" count of cancellation : ",cancellation)