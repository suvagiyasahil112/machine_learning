import random
import numpy as np
import pandas as pd

df=pd.read_csv("movies.csv",index_col="Film")
# print(df.head())

avg_audience_score_per_movie=np.sum(df["Audience score %"])/len(df["Audience score %"])

avg_rotten_tomatoes_rating=np.sum(df["Rotten Tomatoes %"])/len(df["Rotten Tomatoes %"])

avg_movie_rating=(avg_rotten_tomatoes_rating+avg_audience_score_per_movie)/2

print("average rating per movie:",avg_movie_rating)


high =max(df["Audience score %"])
maximum=np.max(df["Rotten Tomatoes %"])


a=df.loc[df["Audience score %"]==high]
print("highest rated  movie by audience",a)



b=df.loc[df["Rotten Tomatoes %"]==maximum]
print("highest rated  movie by rotten tomatoes:",b)

