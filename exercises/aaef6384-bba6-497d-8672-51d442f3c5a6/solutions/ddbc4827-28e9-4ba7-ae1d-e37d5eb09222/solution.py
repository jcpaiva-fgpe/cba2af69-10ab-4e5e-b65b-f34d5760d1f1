import matplotlib.pyplot as plt
import numpy as np anomalies = [0.65, 0.70, 0.82, 0.75, 0.88, 0.92, 0.95]
years = range(2029, 2036)
critical_threshold = 0.8 plt.figure(figsize=(10, 6))
plt.plot(years, anomalies, 'r-o', label='Temperature Anomaly')
plt.axhline(y=critical_threshold, color='gray', linestyle='--', label=f'Critical Threshold ({critical_threshold}°C)')
plt.title('Global Temperature Anomalies (2029-2035)')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.grid(True)
plt.legend()
plt.show()