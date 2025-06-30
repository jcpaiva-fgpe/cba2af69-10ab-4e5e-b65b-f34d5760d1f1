import matplotlib.pyplot as plt coins = ['Bitcoin', 'Ethereum', 'Binance Coin', 'Others']
market_share = [42, 20, 15, 23]
explode = (0.1, 0.05, 0, 0)
colors = ['#f1c40f', '#2ecc71', '#3498db', '#95a5a6'] plt.figure(figsize=(10, 8))
plt.pie(market_share, explode=explode, labels=coins, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Crypto Market Dominance')
plt.axis('equal')
plt.show()