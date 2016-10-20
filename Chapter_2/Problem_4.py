item_1 = float(input("Enter price of item 1 $"))
item_2 = float(input("Enter price of item 2 $"))
item_3 = float(input("Enter price of item 3 $"))
item_4 = float(input("Enter price of item 4 $"))
item_5 = float(input("Enter price of item 5 $"))
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
print("Subtotal = $" + str(float(subtotal)))
tax = float("{0:.3f}".format(subtotal * 0.07))
print("Sales tax = $" + str(float(tax)))
total_amount = subtotal + tax
print("Total amount = $" + str(float(total_amount)))

