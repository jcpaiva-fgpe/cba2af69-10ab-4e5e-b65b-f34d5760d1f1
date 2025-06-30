import pandas as pd
import numpy as np data = { 'Coin': ['BTC', 'ETH', 'DOT'], 'Price_History': [ [45000, 44000, 46000, 45500, 45200], [3000, 2900, 3100, 3050, 3020], [30, 28, 32, 31, 29] ], 'Volume': [1000, 5000, 300]
} df = pd.DataFrame(data) def calculate_volatility(prices): returns = np.diff(prices) / prices[:-1] return np.std(returns) * 100 def calculate_risk_score(volatility, volume): return (volatility * 0.7) + (1000/volume * 0.3) def get_recommendation(risk_score): if risk_score < 5: return 'Low Risk - Buy' elif risk_score < 10: return 'Medium Risk - Hold' else: return 'High Risk - Sell' df['Volatility'] = df['Price_History'].apply(calculate_volatility)
df['Risk_Score'] = df.apply(lambda x: calculate_risk_score(x['Volatility'], x['Volume']), axis=1)
df['Recommendation'] = df['Risk_Score'].apply(get_recommendation) print("Risk Analysis Results:")
print(df[['Coin', 'Volatility', 'Risk_Score', 'Recommendation']])