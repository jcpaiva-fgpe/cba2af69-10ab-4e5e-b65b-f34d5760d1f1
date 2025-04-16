import numpy as np
import matplotlib.pyplot as plt np.random.seed(42)
binance_prices = np.random.normal(45000, 500, 100)
coinbase_prices = np.random.normal(45100, 400, 100)
kraken_prices = np.random.normal(44900, 600, 100)
gemini_prices = np.random.normal(45050, 450, 100) data = [binance_prices, coinbase_prices, kraken_prices, gemini_prices]
labels = ['Binance', 'Coinbase', 'Kraken', 'Gemini'] plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=labels, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Bitcoin Price Distribution Across Exchanges')
plt.ylabel('Price (USD)')
plt.grid(True, axis='y', alpha=0.3)
plt.show()