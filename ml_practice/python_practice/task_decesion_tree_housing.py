from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
import pandas as pd
import random
from scipy.stats import chi2_contingency
from scipy.linalg import solve
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from scipy.fft import fft,ifft,fftfreq
from scipy.interpolate import CubicSpline
from scipy. optimize import curve_fit
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import math
import joblib
import seaborn as sns
from IPython.display import SVG
from IPython.display import display

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import  OneHotEncoder
from sklearn.tree import export_graphviz
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor

from graphviz import Source