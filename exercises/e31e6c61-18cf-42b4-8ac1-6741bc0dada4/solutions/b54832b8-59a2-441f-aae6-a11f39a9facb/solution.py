import matplotlib.pyplot as plt sources = ['Solar', 'Wind', 'Hydro', 'Other Renewables']
percentages = [35, 28, 22, 15]
explode = (0.1, 0.05, 0, 0)
colors = ['#f1c40f', '#3498db', '#2ecc71', '#95a5a6'] plt.figure(figsize=(10, 8))
plt.pie(percentages, explode=explode, labels=sources, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Global Renewable Energy Mix')
plt.axis('equal')
plt.show()