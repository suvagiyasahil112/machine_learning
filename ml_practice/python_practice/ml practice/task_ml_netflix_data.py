import pandas as pd
import numpy  as np 
import math
import time 
import matplotlib.pyplot as plt 


df = pd.read_csv("netflix_titles.csv")
print(df.head(23))
print(df.info())
print(df.isnull().all())


# categoraical = df.select_dtypes(include='object').columns.to_list()
# print(categoraical)


