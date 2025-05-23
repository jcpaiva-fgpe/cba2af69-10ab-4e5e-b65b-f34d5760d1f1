import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt # Prepare data
X = np.array([2025, 2026, 2027, 2028, 2029]).reshape(-1, 1)
y = np.array([15.2, 15.4, 15.6, 15.7, 15.9]) # Create and fit the model
model = LinearRegression()
model.fit(X, y) # Make prediction
year_2030 = np.array([[2030]])
temp_2030 = model.predict(year_2030) # Create prediction line
X_line = np.array([2025, 2026, 2027, 2028, 2029, 2030]).reshape(-1, 1)
y_pred = model.predict(X_line) # Plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Historical Data')
plt.plot(X_line, y_pred, color='red', label='Trend Line')
plt.scatter(2030, temp_2030, color='green', label='2030 Prediction')
plt.xlabel('Year')
plt.ylabel('Global Temperature (°C)')
plt.title('Global Temperature Trend and Prediction')
plt.legend()
plt.grid(True)
plt.show() print(f"Predicted temperature for 2030: {temp_2030[0]:.2f}°C")