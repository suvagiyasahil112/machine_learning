# Real-Time Temperature Monitoring Simulation
# Generate random temperature values between 20°C and 40°C.
# Store data in a Pandas DataFrame.
# Use Matplotlib's FuncAnimation to update the plot dynamically.
# Apply Seaborn for better visualization.

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import datetime as dt
import time 
city="AHMEDABAD"
df = pd.DataFrame({
    "temp":[],
    "time":[]

})


# print(df)
fig,ax=plt.subplots(figsize=(10,6))
sns.set_theme(style="darkgrid",palette="husl")

def update(frame):
    global df
    rand_temp=random.randint(20,40)
    
    row={"temp":rand_temp,"time":pd.Timestamp.now()}

    df=pd.concat([df,pd.DataFrame([row])],ignore_index=True)
    
    if len(df)>20:
        df=df.iloc[-20:]
    ax.clear()
    sns.lineplot(x="time",y="temp",data=df,markers="o",linewidth=1)
    ax.set_title(f"REAL-TIME TEMPRATURE:",fontsize=20)
    ax.set_xlabel("time",fontsize=12)
    ax.set_ylabel("temp",fontsize=12)
    plt.xticks(rotation=45)
    ax.set_ylim(df["temp"].min()-10,df["temp"].max()+10)


ani=FuncAnimation(fig,update,interval=750)
plt.show()