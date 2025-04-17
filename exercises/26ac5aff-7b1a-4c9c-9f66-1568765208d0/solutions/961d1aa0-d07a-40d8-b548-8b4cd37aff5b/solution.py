import pandas as pd data = { 'Coin': ['BTC', 'ETH', 'DOT'], 'Price': [45000, 3000, 30], 'Market_Cap': [850000000000, 350000000000, 30000000000], '24h_Change': [2.3, -1.2, 5.4]
} df = pd.DataFrame(data)
print("Market Overview:")
print(df)
print("\nBasic Statistics:")
print(df.describe())