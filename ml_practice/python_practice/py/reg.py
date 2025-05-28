import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Prepare the data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable (reshaped to 2D)
y = np.array([2, 4, 6, 8, 10])  # Dependent variable

# Step 2: Create and train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Make predictions
y_pred = model.predict(X)

# Step 4: Plot actual data and regression line
plt.scatter(X, y, color='blue', label='Actual data')         # Actual points
plt.plot(X, y_pred, color='red', label='Regression Line')    # Predicted line
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
