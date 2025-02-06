import random

# Define initial prices
bitcoin_price = 45000
ethereum_price = 3200
other_crypto = "Solana"
other_crypto_price = 150

# Simulate price fluctuations over 5 hours
for hour in range(1, 6):
    bitcoin_price += random.randint(-500, 500)
    ethereum_price += random.randint(-50, 50)
    other_crypto_price += random.uniform(-10, 10)
    
    print(f"Hour {hour}: Bitcoin: ${bitcoin_price}, Ethereum: ${ethereum_price}, {other_crypto}: ${other_crypto_price:.2f}")