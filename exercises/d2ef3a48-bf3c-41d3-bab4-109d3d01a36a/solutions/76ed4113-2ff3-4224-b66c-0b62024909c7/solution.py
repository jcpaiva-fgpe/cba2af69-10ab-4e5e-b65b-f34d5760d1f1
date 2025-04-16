import pandas as pd data = { 'Coin': ['BTC', 'ETH', 'DOT'], 'Price': [45000, 3000, 30], 'Market_Cap': [850000000000, 350000000000, 30000000000], '24h_Change': [2.3, -1.2, 5.4]
} df = pd.DataFrame(data) print("Coins with positive change:")
print(df[df['24h_Change'] > 0]) print("\nHigh Market Cap coins:")
print(df[df['Market_Cap'] > 100000000000]) print("\nSorted by Price:")
print(df.sort_values('Price', ascending=False)) df['Status'] = df['Market_Cap'].apply(lambda x: 'High Cap' if x > 500000000000 else 'Regular')
print("\nWith Status:")
print(df)