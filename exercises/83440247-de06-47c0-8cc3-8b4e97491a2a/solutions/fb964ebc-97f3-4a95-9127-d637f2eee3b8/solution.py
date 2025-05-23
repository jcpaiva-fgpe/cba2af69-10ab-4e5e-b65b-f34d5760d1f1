import pandas as pd data = { 'Coin': ['BTC', 'ETH', 'BNB', 'ADA', 'DOT'], 'Price': [45000, 3000, 400, 2, 30], 'Volume': [25000, 15000, 8000, 12000, 5000], 'Market_Cap': [850e9, 350e9, 80e9, 60e9, 30e9], 'Change_24h': [2.3, -1.2, 5.4, -0.8, 3.1]
} df = pd.DataFrame(data) print("Top 3 by Market Cap:")
print(df.sort_values('Market_Cap', ascending=False).head(3)) print("\nTop 3 by 24h Change (Lowest to Highest):")
print(df.sort_values('Change_24h', ascending=True).head(3)) print("\nTop 3 by Volume:")
print(df.sort_values('Volume', ascending=False).head(3))