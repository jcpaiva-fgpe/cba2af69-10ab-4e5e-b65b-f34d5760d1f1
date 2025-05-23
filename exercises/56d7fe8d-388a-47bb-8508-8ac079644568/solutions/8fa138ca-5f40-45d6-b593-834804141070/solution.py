import matplotlib.pyplot as plt
import numpy as np prices = [45000, 45500, 44800, 46000, 45200, 45800, 47000]
days = range(1, 8)
mean_price = np.mean(prices) plt.figure(figsize=(10, 6))
plt.plot(days, prices, 'b-o', label='BTC Price')
plt.axhline(y=mean_price, color='r', linestyle='--', label=f'Mean: ${mean_price:,.0f}')
plt.title('Bitcoin 7-Day Price Trend')
plt.xlabel('Days')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.show()