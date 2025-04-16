import pandas as pd data = { 'Exchange': ['Binance', 'Binance', 'Coinbase', 'Coinbase'], 'Coin': ['BTC', 'ETH', 'BTC', 'ETH'], 'Volume': [1000, 5000, 800, 4000], 'Avg_Price': [45000, 3000, 45100, 3010]
} df = pd.DataFrame(data) print("Total volume per exchange:")
print(df.groupby('Exchange')['Volume'].sum()) print("\nAverage price per coin:")
print(df.groupby('Coin')['Avg_Price'].mean()) print("\nTrading pairs per exchange:")
print(df.groupby('Exchange').size())