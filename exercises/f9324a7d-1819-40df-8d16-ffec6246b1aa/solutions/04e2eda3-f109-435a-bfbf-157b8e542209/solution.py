temperatures = [32.5, 33.1, 33.8, 33.4, 33.9]
for i in range(len(temperatures)-1): if temperatures[i+1] > temperatures[i]: print("Temperature Increased") else: print("Temperature Decreased")