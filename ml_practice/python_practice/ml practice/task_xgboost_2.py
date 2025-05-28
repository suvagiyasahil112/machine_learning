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
from sklearn.preprocessing import OneHotEncoder

import pandas as pd
df = pd.read_csv(r'C:\Users\Sahil\OneDrive\Desktop\Documents\GitHub\machine_learning\ml_practice\python_practice\ml practice\personality_dataset.csv')


# print(df.info())
# print(df.head(20))

categorical_columns = df.select_dtypes(include=['object']).columns.to_list()
ohe = OneHotEncoder(sparse_output=False)
onehotencoder = ohe.fit_transform(df[categorical_columns])
oh_df = pd.DataFrame(onehotencoder,columns=ohe.get_feature_names_out(categorical_columns))
df = pd.concat([df,oh_df],axis=1)
# print(df.head())
df = df.drop(categorical_columns,axis=1)
df = df.dropna()

# print(df.sample(9))
print(df.columns)
df = df.drop("Personality_Introvert",axis=1)

x = df.drop(["Personality_Extrovert"],axis=1)
# print(x.head(6))
y = df[["Personality_Extrovert"]]
# print(x.head(6))
print(df.info())
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


dtrain = xgb.DMatrix(x_train,label =y_train)
dtest = xgb.DMatrix(x_test,label=y_test)


params = {
    'objective': 'multi:softprob', 
    'num_class': 2,  
    'max_depth': 3, 
    'eta': 0.01, 
    'subsample': 0.8,  
    'colsample_bytree': 0.8,
    'lambda': 1.0, 
    'alpha': 0.5, 
    'nthread': 4, 
    'tree_method': 'exact',
    'eval_metric': 'mlogloss'  
}
# print(df.head(34))


cv_results= xgb.cv(dtrain=dtrain,params=params, nfold=5,num_boost_round =100,
                   early_stopping_rounds=10,metrics='mlogloss',as_pandas=True,seed=42)
best_numm_boost_round=  cv_results['test-mlogloss-mean'].idxmin()
model = xgb.train(params,dtrain ,num_boost_round=best_numm_boost_round)

y_pred_prob = model.predict(dtest)
y_pred = y_pred_prob.argmax(axis=1)
acc = accuracy_score(y_test,y_pred)
print(f"accuracy score:{acc*100:.2f}%")
print(y.value_counts())
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

import pandas as pd

# Assuming your target is in a Series or DataFrame column named 'target'
num_classes = y.nunique()
print(f"Number of unique classes: {num_classes}")



model.save_model('xgboost_model2_personality.json')     