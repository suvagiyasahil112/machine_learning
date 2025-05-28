# Real-Time Traffic Monitoring Simulation
# Generate random vehicle count data for different city locations.
# Use a Pandas DataFrame to store real-time traffic trends.
# Visualize the data using stacked bar charts.


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import datetime as dt
import time 
cities_in_gujarat = [
    "Ahmedabad",
    "Surat",
    "Vadodara",
    "Rajkot",
    "Bhavnagar",
    "Jamnagar",
    "Junagadh",
    "Gandhinagar",
    "Anand",
    "Morbi",
    "Nadiad",
    "Mehsana",
    "Surendranagar",
    "Navsari",
    "Bharuch",
    "Porbandar",
    "Vapi",
    "Palanpur",
    "Valsad",
    "Himatnagar",
    "Godhra",
    "Botad",
    "Dahod",
    "Amreli",
    "Veraval",
    "Bhuj",
    "Gondal",
    "Patan",
    "Deesa",
    "Mandvi",
    "Dwarka",
    "Kalol",
    "Modasa",
    "Chhota Udaipur",
    "Sanand",
    "Wadhwan",
    "Kadi",
    "Unjha",
    "Halol",
    "Dhoraji"
]
print(len(cities_in_gujarat))
df=pd.DataFrame({
    "city":[],
    "low":[],
    "medium":[],
    "high":[]

})
for i in range (1000):
    new_row={"city":random.choice(cities_in_gujarat),"medium":random.randint(25,75),"high":random.randint(75,100),"low":random.randint(0,25)}


    df=pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)
    df.drop_duplicates()
    
df=df.drop_duplicates("city")
df=df.set_index("city")
print(df)
df.plot(kind="bar",stacked=True,color=["green","skyblue","red"])    

plt.xlabel("city")
plt.ylabel("traffic intencity")

plt.title("traffic rate ")  
plt.show()

