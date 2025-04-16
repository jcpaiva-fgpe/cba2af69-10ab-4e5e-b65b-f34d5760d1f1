import pandas as pd
import numpy as np data = { 'Coin': ['BTC', 'ETH', 'BTC', 'ETH', 'BTC'], 'Price': [45000, np.nan, 44800, 3000, np.nan], 'Volume': [1000, 800, np.nan, 750, 950]
} df = pd.DataFrame(data) print("Original DataFrame:")
print(df)
print("\nMissing values:")
print(df.isnull().sum()) # Fill missing prices with mean by coin
df['Price'] = df.groupby('Coin')['Price'].transform(lambda x: x.fillna(x.mean())) # Drop rows with missing volume
df_cleaned = df.dropna(subset=['Volume']) print("\nCleaned DataFrame:")
print(df_cleaned) print("\nCleaning Summary:")
print(f"Original rows: {len(df)}")
print(f"Rows after cleaning: {len(df_cleaned)}")