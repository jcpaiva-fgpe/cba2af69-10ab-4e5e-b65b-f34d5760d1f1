bitcoin_price = 39500  # Change this value for testing

# Check price conditions
if bitcoin_price < 40000:
    print("Warning: Bitcoin price dropped below $40,000!")
elif bitcoin_price > 50000:
    print("Alert: Bitcoin price rose above $50,000!")
else:
    print("Bitcoin price is stable.")