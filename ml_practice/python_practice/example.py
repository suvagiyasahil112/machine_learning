import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
# Step 1: Load the dataset
data = {
    'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
    'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25]
}
df = pd.DataFrame(data)
# Step 2: Split the data into inputs (X) and outputs (y)
X = df[['Hours']]
y = df['Scores']
# Step 3: Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 4: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Step 5: Predict the test set
y_pred = model.predict(X_test)
# Step 6: Evaluate the model
r2_train = r2_score(y_train, model.predict(X_train))
r2_test = r2_score(y_test, y_pred)
print(f"R² score for training set: {r2_train:.4f}")
print(f"R² score for test set: {r2_test:.4f}")
# Step 7: Predict score for a student who studies 6.5 hours/day
hours = 6.5
predicted_score = model.predict([[hours]])
print(f"Predicted score for a student who studies {hours} hours/day: {predicted_score[0]:.2f}")
# Step 8: Plotting
# Regression line
line = model.coef_ * X + model.intercept_
# Plot
plt.figure(figsize=(8, 6))
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='green', label='Test data')
plt.plot(X, line, color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Hours vs Score (Linear Regression)')
plt.legend()
plt.grid(True)
plt.show()