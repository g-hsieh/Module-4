print("Enter the purchase price per share ")
purchasePrice = float(input())
print("Enter the current price per share ")
currentPrice = float(input())
print("Enter the quantity of shares ")
quantity = int(input())
value = currentPrice - purchasePrice * quantity
print("The amount purchased in store is $" + str(value))
