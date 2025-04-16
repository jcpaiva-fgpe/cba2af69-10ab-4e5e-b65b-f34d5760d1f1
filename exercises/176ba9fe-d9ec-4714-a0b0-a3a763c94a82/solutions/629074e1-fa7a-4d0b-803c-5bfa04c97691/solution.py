target_price = 45000
current_price = 46500 if current_price > target_price: print("Price above target")
elif current_price < target_price: print("Price below target")
else: print("Price at target") if abs(current_price - target_price) >= 1000: print("Price near target")