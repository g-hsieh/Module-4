print("How much are the fixed costs?")
fixedCosts = float(input())
print("How much is the price per unit?")
pricePerUnit = float(input())
print("How much is the cost per unit?")
costPerUnit = int(input())
breakEvenPoint = fixedCosts / pricePerUnit - costPerUnit
print("The Break-even point is " + str(breakEvenPoint) + " units.")
