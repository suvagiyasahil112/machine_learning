import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

data = stats.norm.rvs(loc=0,scale=1,size=1000)
# plt.figure(figsize=(12,6))
plt.hist(data, bins=30, density=True, alpha=0.6,color="g")

# plotting PDF
x_min,x_max=plt.xlim()
x=np.linspace(x_min,x_max,100)
p=stats.norm.pdf(x,0,1)
plt.plot(x,p,'k',linewidth=2)
plt.show()