import numpy as np
import matplotlib.pyplot as plt
from scipy import stats volume = np.random.normal(1000, 200, 50)
price = volume * 42 + np.random.normal(45000, 500, 50) slope, intercept, r_value, p_value, std_err = stats.linregress(volume, price)
line = slope * volume + intercept plt.figure(figsize=(10, 6))
plt.scatter(volume, price, alpha=0.5)
plt.plot(volume, line, color='red', label=f'R² = {r_value**2:.3f}')
plt.title('Bitcoin Price vs Trading Volume')
plt.xlabel('Trading Volume (BTC)')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()