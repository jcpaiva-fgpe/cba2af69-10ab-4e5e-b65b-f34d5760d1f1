import numpy as np prices = np.array([44000, 45000, 44800, 44900, 45200])
price_changes = np.diff(prices)
percent_changes = (price_changes / prices[:-1]) * 100
max_increase = np.max(percent_changes) print(f"Daily price changes: {price_changes}")
print(f"Percentage changes: {percent_changes}")
print(f"Largest increase: {max_increase}%")