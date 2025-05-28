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


mu ,sigma ,n = 100,25,5

sigma_xbar= sigma/(math.sqrt(n))
P1 = norm.cdf(120,loc=mu,scale=sigma_xbar)-norm.cdf(80,loc=mu,scale=sigma_xbar)

degree_freedom = n-1
chi2_stat= (degree_freedom*(41.7**2)/sigma**2)

p2=1-chi2.cdf(chi2_stat,degree_freedom)

print("p1",P1)
print("p2",p2)
