import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^2 and its derivative f'(x) = 2x
def function(x):
    return x**2

def gradient(x):
    return 2*x  # Derivative of x^2 is 2x

# Gradient Descent Algorithm
learning_rate = 0.1  # Step size
x = 5  # Start point
history = [x]  # To store the path of x values

for i in range(20):  # 20 iterations
    x = x - learning_rate * gradient(x)  # Update x
    history.append(x)

# Plot the function and gradient descent path
x_values = np.linspace(-6, 6, 100)
y_values = function(x_values)

plt.plot(x_values, y_values, label="f(x) = x^2")
plt.scatter(history, [function(x) for x in history], color='red', label="Path")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Gradient Descent on f(x) = x^2")
plt.show()
