import pandas as pd data = { 'Region': ['Arctic', 'Amazon', 'Mediterranean'], 'Temperature': [-5, 28, 22], 'Sea_Level_Rise': [3.2, 0, 2.8], 'CO2_Level': [412, 405, 415]
} df = pd.DataFrame(data) print("Regions with high temperature:")
print(df[df['Temperature'] > 20]) print("\nRegions with high CO2:")
print(df[df['CO2_Level'] > 410]) print("\nSorted by Sea Level Rise:")
print(df.sort_values('Sea_Level_Rise', ascending=False)) df['Risk_Level'] = df['Sea_Level_Rise'].apply(lambda x: 'High' if x > 3.0 else 'Moderate')
print("\nWith Risk Levels:")
print(df)