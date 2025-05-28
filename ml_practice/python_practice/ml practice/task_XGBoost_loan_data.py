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
df = pd.read_excel('Bank_Personal_Loan_Modelling.xlsx', sheet_name="Data")

# print(df.head(15))
# print(df.columns)
# print(df.describe())

categorical_cols = df.select_dtypes(include=['object']).columns.to_list()
# print("categorical columns:",categorical_cols)  

#    plots 
plt.figure(figsize=(20,10))
sns.histplot(df['Income'], kde=True, bins=30, color='skyblue')
plt.title('Distribution of Customer Income')
plt.xlabel('Income ($000)')
plt.ylabel('Number of Customers')
plt.grid(True)
# plt.show()

# print(df.describe())
# print(df.isnull().all())

# print(df['Personal Loan'])
df = df.drop("ID",axis=1)
x= df.drop(['Personal Loan'],axis=1)
y = df['Personal Loan']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# print(x_train)

dtrain  = xgb.DMatrix(x_train,label = y_train)
dtest = xgb.DMatrix(x_test,label  = y_test)

# params = {
#     'objective' : 'multi:softprob',
#     'num_class' : 3,
#     'max_depth' : 3,
#     'eta' : 0.1,
#     'subsample' : 0.8,
#     'colsample_bytree' : 0.8,
#     'lambda' : 0.1,
#     'alpha': 0.5,
#     'nthread':4 , 
#     'tree_method' : 'exact',
#     'eval_metric' :'mlogloss'

# }

params = {
    'objective': 'multi:softprob',  # Specify the objective for multi-class classification
    'num_class': 3,  # Number of classes in the target (Iris dataset has 3 classes)
    'max_depth': 3,  # Maximum depth of a tree (controls the complexity of the model)
    'eta': 0.1,  # Learning rate (controls the step size at each iteration)
    'subsample': 0.8,  # Subsample ratio of the training instances (to prevent overfitting)
    'colsample_bytree': 0.8,  # Subsample ratio of columns when constructing each tree (to prevent overfitting)
    'lambda': 1.0,  # L2 regularization term on weights (to prevent overfitting)
    'alpha': 0.5,  # L1 regularization term on weights (to prevent overfitting)
    'nthread': 4,  # Number of parallel threads used to run XGBoost (for faster computation)
    'tree_method': 'exact',  # Tree construction algorithm
    'eval_metric': 'mlogloss'  # Evaluation metric (logarithmic loss for multi-class classification)
}

cv_results = xgb.cv(dtrain=dtrain, params=params, nfold=5, num_boost_round=100,
                    early_stopping_rounds=10, metrics="mlogloss", as_pandas=True, seed=42)

best_num_boost_round= cv_results['test-mlogloss-mean'].idxmin()
model = xgb.train(params,dtrain,num_boost_round=best_num_boost_round)

y_pred_prob = model.predict(dtest)
y_pred = y_pred_prob.argmax(axis=1)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

model.save_model('xgboost_model1.json')