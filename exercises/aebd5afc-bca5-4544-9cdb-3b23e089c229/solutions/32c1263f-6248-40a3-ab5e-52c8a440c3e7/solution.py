import matplotlib.pyplot as plt exchanges = ['Binance', 'Coinbase', 'Kraken', 'Gemini']
volumes = [1000, 800, 600, 400]
colors = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c'] plt.figure(figsize=(10, 6))
bars = plt.bar(exchanges, volumes, color=colors) # Add value labels on top of each bar
for bar in bars: height = bar.get_height() plt.text(bar.get_x() + bar.get_width()/2., height, f'{height:,} BTC', ha='center', va='bottom') plt.title('24h Trading Volume by Exchange')
plt.ylabel('Volume (BTC)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()