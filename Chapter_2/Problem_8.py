food = float(input("Enter charge for food"))
tip = food * .18
sales_tax = food * .07
total = food + tip + sales_tax
print("The price of your food is $" + str(format(food, '.2f')))
print("Tip = $" + str(format(tip, '.2f')))
print("Sales tax = $" + str(format(sales_tax, '.2f')))
print("Total sales = $" + str(format(total, '.2f')))