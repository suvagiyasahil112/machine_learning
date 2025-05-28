from scipy.stats import uniform
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import t
from scipy.stats import f
import math
import random 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

# ============================1===========================================

# list1 = []
# for i in range (50,151):
#     list1.append (i)

# # print(list1)

# num_simulation = 100000
# greater_than_74=0
# between_range = 0
# for i in range (num_simulation):
#     a = random.choice(list1)
#     if a > 74 :
#         greater_than_74+=1
#     if a >50 and a<126:
#         between_range+=1
# b = greater_than_74/100000
# c= between_range/100000
# print("prob of greater than 74",(b*100 ,"%"))
# print("prob of between 50, 126:",(c*100 ,"%"))

# ================================4=======================================

# degreefreedom=5

# px_greater = 1-chi2.cdf(6.5,degreefreedom)
# px_less =chi2.cdf(11.8,degreefreedom)

# print(f"{px_greater}.4f")
# print(f"{px_less}.4f")


# =================================5=======================================
# mu= 25
# sigma = math.sqrt(36)

# x1 = 28 
# p1 =  norm.cdf (x1,mu,sigma)

# print("x<28  :",p1)

# x2= 30 
# p2 = 1- norm.cdf (x2,mu,sigma)
# print("x > 30  :",p2)

# x3 = 20 
# p3 = norm.cdf (x3,mu,sigma)
# print("x < 20  :",p3)



# p4 =  norm.cdf (29,mu,sigma) - norm.cdf (21,mu,sigma)
# print(" 4th  :",p4)



# =====================================6====================================
# 1

# df=15

# t1=1.341

# a=t.cdf(t1,df)
# print(f"answer = {a*100}percent")




# 2

# df = 8

# a=t.ppf(0.99,df)

# print("T value:",a)


# 3

# P(t_{24} < - 0.5314)


# df= 24

# t1= -0.5314

# a=t.cdf(t1,df)
# print("answer:",a)


# ===============================7================================

# 1
# df1=5
# df2=12
# f_value = 3.106

# a =f.cdf(f_value,df1,df2)
# print("answer:",a)


# 2

df1= 7
df2=4

a=f.cdf(0.99,df1,df2)

print("answer:",a)