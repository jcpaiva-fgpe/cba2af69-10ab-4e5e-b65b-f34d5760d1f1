import pandas as pd data = { 'Zone': ['Tropical', 'Tropical', 'Temperate', 'Temperate'], 'Region': ['Amazon', 'Congo', 'Europe', 'North America'], 'Temperature': [28, 27, 15, 12], 'Rainfall': [2500, 1800, 700, 850]
} df = pd.DataFrame(data) print("Average temperature per zone:")
print(df.groupby('Zone')['Temperature'].mean()) print("\nTotal rainfall per zone:")
print(df.groupby('Zone')['Rainfall'].sum()) print("\nRegions per zone:")
print(df.groupby('Zone').size())