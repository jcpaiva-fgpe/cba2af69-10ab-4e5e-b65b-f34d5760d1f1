import numpy as np temperatures = np.array([14.8, 15.1, 15.4, 15.3, 15.7])
temp_changes = np.diff(temperatures)
percent_changes = (temp_changes / temperatures[:-1]) * 100
max_increase = np.max(temp_changes) print(f"Year-over-year changes: {temp_changes}°C")
print(f"Percentage changes: {percent_changes}%")
print(f"Largest increase: {max_increase}°C")