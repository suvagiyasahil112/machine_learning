# Create a real-time stock price simulation using Pandas, Matplotlib, and Seaborn without making API requests.
# Tasks:
# Generate simulated stock prices using random values.
# Store data in a Pandas DataFrame and update it dynamically.
# Use Matplotlib's FuncAnimation to update the chart in real-time.
# Enhance visualization with Seaborn for better styling.
# Limit data to the last 20 values for a clean real-time effect
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import datetime as dt
import time 

starting_price=150
stock_name="python"
price_list=[]

df=pd.DataFrame({
    "price":[starting_price],
    "Timestamp":[pd.Timestamp.now()]
})

fig,ax=plt.subplots(figsize=(10,6))
sns.set_theme(style="whitegrid")
    
def update(frame):
    global df,starting_price
    
    updated_stock = random.randint(-20, 20)  
    starting_price += updated_stock
    new_row = {"price": starting_price, "Timestamp": pd.Timestamp.now()}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # print("====>",updated_stock)

    if (len(df)>20):
        df=df.iloc[-20:]
    ax.clear()
    sns.lineplot(x="Timestamp",y="price",data=df,ax=ax,markers="o",linewidth=2)
    ax.set_title(f"Real time stock price of {stock_name}",fontsize=20)
    ax.set_xlabel("Timestamp",fontsize=12)
    ax.set_ylabel("price",fontsize=12)
    plt.xticks(rotation=45)
    ax.set_ylim(df["price"].min() -10,df["price"].max()+10 )

ani=FuncAnimation(fig,update,interval=500)
plt.show()