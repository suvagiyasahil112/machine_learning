

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Descriptive Statistics (scipy.stats)
data = np.array([2, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Mean:", np.mean(data))  # Mean
print("Median:", np.median(data))  # Median
print("Mode:", stats.mode(data))  # Mode
print("Variance:", np.var(data))  # Varianc
print("Standard Deviation:", np.std(data))  # Standard Deviation


# Probability Distributions
# Generate random values from a normal distribution
data = stats.norm.rvs(loc=0, scale=1, size=1000)  # Mean=0, Std=1

# Plot the histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Plot the probability density function (PDF)
xmin, xmax = plt.xlim() 
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, 0, 1)
plt.plot(x, p, 'k', linewidth=2)  
plt.show()

# T-Test (Comparing Two Sample Means)
# Sample Data

sample1 = np.random.normal(50, 10, 100)
sample2 = np.random.normal(52, 10, 100)
print(sample1)
print(sample2)




# Perform t-test
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)


# Chi-Square Test (Checking Association Between Categories)
observed = np.array([[50, 30], [20, 50]])

# Perform Chi-Square Test
chi2_stat, p_val, dof, expected = stats.chi2_contingency(observed)
print("Chi-Square Statistic:", chi2_stat)
print("P-Value:", p_val)


# Finding the Minimum of a Function3

from scipy.optimize import minimize

# Define the function
def f(x):
    return x**2 + 3*x + 2

# Minimize the function
result = minimize(f, x0=0)  # x0 is the initial guess
print(result)

# Solving Linear Equations
from scipy.linalg import solve

A = np.array([[3, 2], [1, -1]])  # Coefficient Matrix
B = np.array([18, 2])  # Result Matrix

solution = solve(A, B)
print("Solution (x, y):", solution)


# Interpolation Example

from scipy.interpolate import interp1d

# Given data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 8, 18, 32, 50])

# 2x^2
# Create an interpolation function
f = interp1d(x, y, kind='cubic')

# Predict new values
x_new = np.linspace(0, 5, 50)
y_new = f(x_new)

# Plot the results
plt.scatter(x, y, label="Data Points", color="red")
plt.plot(x_new, y_new, label="Interpolated Curve")
plt.legend()
plt.show()


#  Fourier Transform (FFT) for Signal Processing

from scipy.fft import fft

# Sample signal data
signal = np.sin(2 * np.pi * np.linspace(0, 1, 100))

# Compute the FFT
fft_signal = fft(signal)
print(fft_signal)


# ✅ Weather Forecasting using Interpolation
# ✅ Stock Market Analysis using Probability Distributions
# ✅ Image Processing using Fourier Transform


# Generate and Visualize Stock Returns

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Simulate daily returns (Normal Distribution with Mean=0.001, Std=0.02)
daily_returns = np.random.normal(0.001, 0.02, 1000)  # 1000 days of returns

# Plot histogram of daily returns
plt.hist(daily_returns, bins=50, density=True, alpha=0.6, color='g')

# Fit normal distribution to the data
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, 0.001, 0.02)
plt.plot(x, p, 'k', linewidth=2)

plt.title("Histogram of Simulated Daily Stock Returns")
plt.xlabel("Daily Return")
plt.ylabel("Density")
plt.show()


# Modeling Stock Prices Using Log-Normal Distribution

# Simulate stock prices using a log-normal distribution
initial_price = 100  # Starting price of stock
days = 1000  # Number of days

# Simulating stock price movement
stock_prices = initial_price * np.exp(np.cumsum(np.random.normal(0.001, 0.02, days)))

# Plot stock price movement
plt.plot(stock_prices, color='blue')
plt.title("Simulated Stock Price Movement")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()


# Using Exponential Distribution for Market Trends

# Simulate waiting times between large stock price jumps
waiting_times = np.random.exponential(scale=10, size=1000)  # Average 10 days between jumps

# Plot histogram
plt.hist(waiting_times, bins=50, density=True, alpha=0.6, color='r')
plt.title("Histogram of Waiting Times Between Large Price Jumps")
plt.xlabel("Days")
plt.ylabel("Density")
plt.show()



# Applying Poisson Distribution to Model Trade Volumes

# Simulate trade volumes per minute using Poisson Distribution
trade_volumes = np.random.poisson(lam=30, size=1000)  # Avg 30 trades per minute

# Plot histogram
plt.hist(trade_volumes, bins=30, density=True, alpha=0.6, color='purple')
plt.title("Histogram of Trades Per Minute")
plt.xlabel("Number of Trades")
plt.ylabel("Density")
plt.show()



# Monte Carlo Simulation for Stock Price Forecasting

num_simulations = 1000  # Number of simulations
time_horizon = 252  # Number of trading days in a year
mu = 0.0005  # Expected return
sigma = 0.02  # Volatility
initial_stock_price = 100  # Initial stock price

simulated_prices = np.zeros((num_simulations, time_horizon))

for i in range(num_simulations):
    price = initial_stock_price
    for t in range(time_horizon):
        price *= np.exp(np.random.normal(mu, sigma))  # Log-normal model
        simulated_prices[i, t] = price

# Plot Monte Carlo simulations
plt.plot(simulated_prices.T, alpha=0.1, color='blue')
plt.title("Monte Carlo Simulation of Stock Prices")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()


# 📌 Which Probability Distribution to Use?

# Distribution	Use Case in Stock Market
# Normal Distribution	Models daily stock returns.
# Log-Normal Distribution	Models actual stock prices.
# Exponential Distribution	Models waiting times for significant price changes.
# Poisson Distribution	Models trade volume per unit time.
# Monte Carlo Simulation	Forecasts future stock prices under uncertainty.




import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Step 1: Apply Fourier Transform to the image
f = np.fft.fft2(image)  # Perform the 2D Fourier Transform
fshift = np.fft.fftshift(f)  # Shift the zero-frequency component to the center

# Step 2: Calculate the magnitude spectrum (log scale for better visualization)
magnitude_spectrum = np.log(np.abs(fshift) + 1)  # Log scale for better visualization

# Step 3: Visualize the original image and the frequency domain (magnitude spectrum)
plt.figure(figsize=(10, 5))

# Plot Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Plot Magnitude Spectrum
plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.axis('off')

plt.show()

# Step 4: Apply a filter in the frequency domain (e.g., low-pass filter)
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  # Center of the image

# Create a low-pass filter mask (circle in the center)
mask = np.zeros((rows, cols), dtype=np.float32)
radius = 30  # Filter size
center = [crow, ccol]
cv2.circle(mask, center, radius, 1, thickness=-1)

# Apply the mask to the frequency domain (filter the frequencies)
fshift_filtered = fshift * mask

# Step 5: Inverse Fourier Transform to get the filtered image
f_ishift = np.fft.ifftshift(fshift_filtered)  # Inverse shift
image_back = np.fft.ifft2(f_ishift)  # Perform the inverse 2D Fourier Transform
image_back = np.abs(image_back)  # Get the real part of the result

# Step 6: Visualize the filtered image
plt.figure(figsize=(10, 5))

# Plot Filtered Image
plt.imshow(image_back, cmap='gray')
plt.title('Filtered Image (Low-Pass Filter)')
plt.axis('off')
plt.show()
