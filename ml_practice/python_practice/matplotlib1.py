import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
# a= [1,2,3,4,9,8,7,6,5,8,9]
# b =[4,3,4,5]

# plt.plot(a,b ,label="data",color="red",linewidth=2)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()

# plt.show()


# plt.scatter(a,b ,label="data",color="red",linewidth=2)
# plt.xlabel("x")
# plt.ylabel("y")

# plt.show()



# --------------------------- bar----------------
# plt.bar(a,b ,label="data",color="red")
# plt.xlabel("x")
# plt.ylabel("y")

# plt.show()


# da = [1,2,3,4,1,6,7,7,8,9,9]

# plt.hist(da,bins=11 ,label="data",color="red",edgecolor ="black")
# plt.xlabel("x")
# plt.ylabel("y")

# plt.show()

# x_axis=pd.DataFrame(np.random.arange(15))   
# print(x_axis)

df=pd.read_csv('movies.csv')
print(df.dtypes)
print(df.head(5))
grouped_genre=df.groupby("Genre").agg(
    Genre=("Genre","count"),
    # count_of_names=("Film","count"),
    avg_of_audience=("Audience score %","mean"),
    avg_of_rotten=("Rotten Tomatoes %","mean")
    ) 

print(grouped_genre)
z=df["Genre"]
# print(df.dtypes)

x_axis=grouped_genre["avg_of_audience"]
y_axis=grouped_genre["avg_of_rotten"]
z_axise=np.unique(z)
z_axis=np.unique(z_axise)
# random.shuffle(x_axis)
# random.shuffle(y_axis)
# print(z_axis)

plt.bar(z_axis,y_axis,label="ratings",color="red",linewidth=3)
plt.xlabel("Genre")
plt.ylabel("avg_rotten_score")
plt.legend()
plt.show()



