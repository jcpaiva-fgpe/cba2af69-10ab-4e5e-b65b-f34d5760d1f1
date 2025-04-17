import pandas as pd data = { 'Region': ['Arctic', 'Amazon', 'Mediterranean'], 'Temperature': [-5, 28, 22], 'Sea_Level_Rise': [3.2, 0, 2.8], 'CO2_Level': [412, 405, 415]
} df = pd.DataFrame(data)
print("Global Climate Indicators:")
print(df)
print("\nBasic Statistics:")
print(df.describe())