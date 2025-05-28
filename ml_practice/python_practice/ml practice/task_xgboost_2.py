import pandas as pd
import numpy as nu
import matplotlib.pyplot as plt
import random
import math 
import xgboost as xgb
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
import pandas as pd
df = pd.read_csv('mushrooms.csv')


print(df.info())
