prices = [45000, 44800, 44600, 44900, 45100]
for i in range(len(prices)-1): if prices[i+1] < prices[i]: print("Price increased") else: print("Price decreased")