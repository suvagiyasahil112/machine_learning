from sklearn.datasets import load_iris
import pandas as pd

# Load the dataset
iris = load_iris()

# Features
X = iris.data

# Target labels (0, 1, 2)
y = iris.target

# Feature names
print("Feature names:", iris.feature_names)

# Convert to pandas DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

# Show the first few rows  
print(df.head())




#Detecting Missing Values:
import pandas as pd

# Example data
data = {'age': [25, 30, None, 40], 'salary': [50000, 60000, 65000, None]}
df = pd.DataFrame(data)

# Check for missing values
print(df.isnull())


# 2.1 Handling Missing Values

#Filling Missing Values:

from sklearn.impute import SimpleImputer

# Fill missing values with mean
imputer = SimpleImputer(strategy='mean')
df[['age', 'salary']] = imputer.fit_transform(df[['age', 'salary']])

# 2.2 Feature Scaling (Normalization / Standardization)
# Machine learning models perform better when features are on the same scale.
#StandardScaler (Z-score scaling)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)


#MinMaxScaler (0 to 1 scaling)
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)


#2.3 Encoding Categorical Variables
#One-Hot Encoding (for non-ordinal categories)

from sklearn.preprocessing import OneHotEncoder 

data = pd.DataFrame({'city': ['London', 'Paris', 'New York']})
encoder = OneHotEncoder(sparse=False)
encoded = encoder.fit_transform(data[['city']])


#Label Encoding (for ordinal categories)
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
data['city_encoded'] = label_encoder.fit_transform(data['city'])


# 2.4 Feature Selection
# Remove irrelevant or less important features to improve model performance.
from sklearn.feature_selection import SelectKBest, f_classif

X = iris.data
y = iris.target

# Select top 2 features
selector = SelectKBest(score_func=f_classif, k=2)
X_new = selector.fit_transform(X, y)

#2.5 Putting It All Together with a Pipeline

from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)


# 3.1 Train/Test Split
#Before training, split your data into training and testing sets.

from sklearn.model_selection import train_test_split

# Assume X and y are your features and labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 3.2 Cross-Validation
# Cross-validation gives a better estimate of model performance by using multiple train/test splits.
# K-Fold Cross-Validation

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
scores = cross_val_score(model, X, y, cv=5)

print("Cross-validation scores:", scores)
print("Average accuracy:", scores.mean())

# 3.3 Hyperparameter Tuning
# Choosing the best settings (hyperparameters) for your model using:

# Grid Search (Exhaustive Search)

from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 5, 10]
}
    
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=3)
grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)


# Randomized Search (Faster)

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    'n_estimators': randint(10, 100),
    'max_depth': [None, 5, 10]
}

random_search = RandomizedSearchCV(RandomForestClassifier(), param_dist, n_iter=5, cv=3)
random_search.fit(X_train, y_train)

print("Best Parameters:", random_search.best_params_)

# 3.4 Comparing Multiple Models
# You can test different models easily:

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

models = [
    ('SVM', SVC()),
    ('Logistic Regression', LogisticRegression()),
    ('KNN', KNeighborsClassifier())
]

for name, model in models:
    model.fit(X_train, y_train)
    print(name, "Accuracy:", model.score(X_test, y_test))

# 4.2 Basic Classification Workflow (Iris Dataset)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))

# 4.3

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

#4.4 Classifiers with Simple Code
#Logistic Regression:
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
#k-NN:
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
# SVM:
from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(X_train, y_train)


#5.2 Basic Regression Workflow (Boston Dataset)
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
X, y = load_diabetes(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


#5.4 Regression Models in Action
#Linear Regression:

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)


#Random Forest Regressor:
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

#SVR (Support Vector Regression):
from sklearn.svm import SVR
model = SVR()
model.fit(X_train, y_train)

#Visualization Example
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")
plt.show()

#6.2 Clustering
#K-Means Clustering

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Create sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Apply KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red')
plt.title("KMeans Clustering")
plt.show()

#Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=3)
y_pred = model.fit_predict(X)


# 6.3 Dimensionality Reduction
# PCA (Principal Component Analysis)
# PCA reduces dimensions while keeping the most important information.

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True)

# Apply PCA to reduce to 2D
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Visualize
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA - 2D Projection of Iris Dataset')
plt.show()

#t-SNE (for advanced visual clustering)
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)


#7
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 0]

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
print("Classification Report:\n", classification_report(y_true, y_pred))

#ROC Curve & AUC
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

fpr, tpr, thresholds = roc_curve(y_true, [0.1, 0.4, 0.35, 0.8, 0.7])
plt.plot(fpr, tpr)
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

#7.3
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print("MSE:", mean_squared_error(y_true, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
print("MAE:", mean_absolute_error(y_true, y_pred))
print("R² Score:", r2_score(y_true, y_pred))

#7..4
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=4)
model = KMeans(n_clusters=4)
model.fit(X)

print("Silhouette Score:", silhouette_score(X, model.labels_))


#8 . Save Model 
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from joblib import dump, load

# Train a model
X, y = load_iris(return_X_y=True)
model = LogisticRegression()
model.fit(X, y)

# Save model
dump(model, 'logistic_model.pkl')


#Load the model
# Load the saved model
loaded_model = load('logistic_model.pkl')

# Predict using the loaded model
print(loaded_model.predict([X[0]]))

#8.4 Saving & Loading with pickle
#Save
import pickle

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

#Load
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

print(loaded_model.predict([X[1]]))

#Quick Example: Flask (for context)

from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)
model = load('logistic_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    prediction = model.predict([data])
    return jsonify({'prediction': prediction.tolist()})

app.run()


#9.3 K-Fold Cross-Validation Example
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load data
X, y = load_iris(return_X_y=True)

# Create model
model = LogisticRegression()

# Perform K-fold cross-validation
scores = cross_val_score(model, X, y, cv=5)  # 5 folds
print("Cross-Validation Scores:", scores)
print("Average Score:", scores.mean())


# 9.4 Stratified K-Fold Cross-Validation (for Classification)
# This technique ensures that each fold has the same proportion of labels (useful for imbalanced datasets).

from sklearn.model_selection import StratifiedKFold

# Use Stratified K-Fold
stratified_kfold = StratifiedKFold(n_splits=5)
for train_idx, test_idx in stratified_kfold.split(X, y):
    print("Train:", train_idx, "Test:", test_idx)


# 9.5 Leave-One-Out Cross-Validation (LOO)
# This method uses each data point as a test set and the rest as the training set. It’s computationally expensive, especially for large datasets.


from sklearn.model_selection import LeaveOneOut

# Use Leave-One-Out Cross-Validation
loo = LeaveOneOut()
for train_idx, test_idx in loo.split(X):
    print("Train:", train_idx, "Test:", test_idx)

# 9.6 Evaluating Models: Cross-Validation and Grid Search
# Cross-validation works hand-in-hand with model selection techniques, such as Grid Search, which helps to find the best hyperparameters.

# 9.7 Grid Search with Cross-Validation
# Grid Search allows us to search for the best combination of hyperparameters for a model using cross-validation.

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# Define model
svc = SVC()

# Define hyperparameter grid
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}

# Perform Grid Search with Cross-Validation
grid_search = GridSearchCV(svc, param_grid, cv=5)
grid_search.fit(X, y)

# Best parameters and best score
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

# 9.8 Randomized Search (Alternative to Grid Search)
# Randomized search samples from the hyperparameter grid randomly, which can be more efficient when dealing with a large search space.

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

# Define model
svc = SVC()

# Define hyperparameter grid
param_dist = {'C': randint(1, 100), 'kernel': ['linear', 'rbf']}

# Perform Randomized Search with Cross-Validation
random_search = RandomizedSearchCV(svc, param_distributions=param_dist, n_iter=100, cv=5)
random_search.fit(X, y)

# Best parameters and best score
print("Best Parameters:", random_search.best_params_)
print("Best Score:", random_search.best_score_)


# 9.9 Model Selection and Comparison
# To compare multiple models, you can use cross-validation to assess their performance on different algorithms.

from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Define models
models = [SVC(), RandomForestClassifier()]

for model in models:
    scores = cross_val_score(model, X, y, cv=5)
    print(f"Model: {model.__class__.__name__} - Cross-validation Score: {scores.mean()}")


# 10.3 Creating a Simple Pipeline
# Here’s an example pipeline with StandardScaler for scaling features and LogisticRegression for classification.

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a pipeline with scaler and model
pipeline = Pipeline([
    ('scaler', StandardScaler()),       # Preprocessing step
    ('logreg', LogisticRegression())    # Model step
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)
print("Predictions:", y_pred)


# 10.4 Preprocessing in Pipelines
# You can include preprocessing steps like:

# Standardization (scaling data)

# One-hot encoding (for categorical features)

# Imputation (for missing values)


from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

# Example data with missing values
X = [[1, 'Male', 22], [2, 'Female', None], [3, 'Female', 24], [4, 'Male', 25]]
y = [0, 1, 1, 0]

# Preprocessing pipeline with imputer for missing values
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), [2]),  # Impute missing values for column 2 (age)
        ('cat', OneHotEncoder(), [1])                   # One-hot encode column 1 (gender)
    ]
)

# Define a complete pipeline: preprocessing + classification model
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# Fit the model
pipeline.fit(X, y)

# Predictions
y_pred = pipeline.predict(X)
print("Predictions:", y_pred)


# 10.5 Saving and Loading Pipelines
# You can save and load entire pipelines, not just the models, making it easy to deploy and maintain.

from joblib import dump, load

# Save the pipeline
dump(pipeline, 'pipeline.joblib')

# Load the pipeline
loaded_pipeline = load('pipeline.joblib')

# Use the loaded pipeline to predict
print(loaded_pipeline.predict(X))


# 10.6 Pipelines in Production
# Pipelines are crucial when deploying models to production because:

# They ensure the same steps are followed when making predictions in real-time.

# Data preprocessing becomes part of the deployment process, so there's no risk of inconsistent transformations.


# Project

# Loan Default Prediction
# Problem: Predict whether a borrower will default on a loan based on features like credit score, income, loan amount, etc.
# Skills Learned: Classification, imbalanced datasets handling, feature scaling.
# Tools: scikit-learn, Pandas, Matplotlib.

# Steps:
# Load a loan dataset (e.g., LendingClub dataset).

# Preprocess the data (e.g., handle missing values, balance the dataset).

# Train a classification model (e.g., Logistic Regression, Decision Trees).

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score, precision_score, recall_score

# Step 1: Data Collection
# Load the dataset (You can replace this with the LendingClub dataset or any other dataset)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/loan_prediction.csv"
data = pd.read_csv(url)

# Display the first few rows of the dataset
print(data.head())

# Step 2: Preprocessing
# Handle missing values
data = data.dropna()  # Remove rows with missing values (you can also use imputation if necessary)

# Convert categorical variables into numeric values using one-hot encoding
data = pd.get_dummies(data, drop_first=True)

# Display the first few rows after preprocessing
print(data.head())

# Step 3: Feature Engineering
# Define the target variable (Loan Default: 1 = Default, 0 = No Default)
X = data.drop('Loan_Status_Y', axis=1)  # Features (All columns except the target)
y = data['Loan_Status_Y']  # Target (Loan default status)

# Step 4: Train-Test Split
# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Feature Scaling (Standardize the features)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: Train a Classification Model
# Logistic Regression Model
log_reg_model = LogisticRegression()
log_reg_model.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = log_reg_model.predict(X_test)

# Step 8: Evaluate the Model
# Classification Report
print("Classification Report (Logistic Regression):")
print(classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['No Default', 'Default'], yticklabels=['No Default', 'Default'])
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

# Step 9: Evaluate using F1-Score, Precision, and Recall
print(f'F1 Score: {f1_score(y_test, y_pred)}')
print(f'Precision: {precision_score(y_test, y_pred)}')
print(f'Recall: {recall_score(y_test, y_pred)}')

# Step 10: Train a Decision Tree Classifier
decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X_train, y_train)

# Make Predictions
y_pred_dt = decision_tree_model.predict(X_test)

# Evaluate the Decision Tree Model
print("Classification Report (Decision Tree):")
print(classification_report(y_test, y_pred_dt))

# Confusion Matrix for Decision Tree
conf_matrix_dt = confusion_matrix(y_test, y_pred_dt)
plt.figure(figsize=(6,6))
sns.heatmap(conf_matrix_dt, annot=True, fmt='d', cmap='Blues', xticklabels=['No Default', 'Default'], yticklabels=['No Default', 'Default'])
plt.title("Confusion Matrix - Decision Tree")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

# Evaluate using F1-Score, Precision, and Recall for Decision Tree
print(f'F1 Score (Decision Tree): {f1_score(y_test, y_pred_dt)}')
print(f'Precision (Decision Tree): {precision_score(y_test, y_pred_dt)}')
print(f'Recall (Decision Tree): {recall_score(y_test, y_pred_dt)}')

# Step 11: Train a Random Forest Classifier (Optional for better performance)
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Make Predictions
y_pred_rf = rf_model.predict(X_test)

# Evaluate the Random Forest Model
print("Classification Report (Random Forest):")
print(classification_report(y_test, y_pred_rf))

# Confusion Matrix for Random Forest
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
plt.figure(figsize=(6,6))
sns.heatmap(conf_matrix_rf, annot=True, fmt='d', cmap='Blues', xticklabels=['No Default', 'Default'], yticklabels=['No Default', 'Default'])
plt.title("Confusion Matrix - Random Forest")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

# Evaluate using F1-Score, Precision, and Recall for Random Forest
print(f'F1 Score (Random Forest): {f1_score(y_test, y_pred_rf)}')
print(f'Precision (Random Forest): {precision_score(y_test, y_pred_rf)}')
print(f'Recall (Random Forest): {recall_score(y_test, y_pred_rf)}')


# Model Tuning: You can tune the hyperparameters of your models using Grid Search or Randomized Search.

# Handling Imbalanced Data: If your dataset has imbalanced classes (e.g., more non-defaults than defaults), you can use techniques like SMOTE (Synthetic Minority Over-sampling Technique) or adjust class weights in the model.

# Advanced Models: You can try XGBoost or LightGBM for better performance on imbalanced datasets.

