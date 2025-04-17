import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd # Generate sample data
dates = pd.date_range(start='2024-01-01', periods=30)
prices = np.random.normal(45000, 1000, 30).cumsum() + 45000 plt.style.use('seaborn')
fig, ax = plt.figure(figsize=(12, 6)) plt.plot(dates, prices, color='#2ecc71', linewidth=2, label='BTC/USD')
plt.fill_between(dates, prices, alpha=0.1, color='#2ecc71') # Customize axes and grid
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Bitcoin Price Movement (30 Days)', pad=20)
plt.xlabel('Date')
plt.ylabel('Price (USD)') # Add annotation for significant point
max_price_idx = np.argmax(prices)
plt.annotate('Peak Price', xy=(dates[max_price_idx], prices[max_price_idx]), xytext=(10, 10), textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5), arrowprops=dict(arrowstyle='->')) plt.legend(loc='upper left')
plt.tight_layout()
plt.show()