import matplotlib.pyplot as plt regions = ['North America', 'Europe', 'Asia', 'South America']
emissions = [5.2, 3.8, 16.5, 1.2]
colors = ['#2ecc71', '#3498db', '#e74c3c', '#f1c40f'] plt.figure(figsize=(10, 6))
bars = plt.bar(regions, emissions, color=colors) # Add value labels on top of each bar
for bar in bars: height = bar.get_height() plt.text(bar.get_x() + bar.get_width()/2., height, f'{height} GT', ha='center', va='bottom') plt.title('Annual CO2 Emissions by Region')
plt.ylabel('CO2 Emissions (Gigatons)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()