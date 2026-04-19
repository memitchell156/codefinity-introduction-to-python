prices = [29.99, 45.50, 12.75, 38.20]
for updated_prices in range(len(prices)):
    if updated_prices == 0:
        prices[updated_prices] *= 0.90
    elif updated_prices == 1:
        prices[updated_prices] *= 0.80
    elif updated_prices == 2:
        prices[updated_prices] *= 0.85
    elif updated_prices == 3:
        prices[updated_prices] *= 0.95
    print(f"Updated price for item {updated_prices}: ${prices[updated_prices]:.2f}")
