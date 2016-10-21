# Introduce the program
print("Welcome to the cookie quantity converter!")
# Ask the user how many cookies they would like to make
quantity = int(input("How many cookies would you like to make?"))
# define the original amount of cookies, sugar, butter and flour
sugar = 1.5
butter = 1
cups_of_flour = 2.75
cookies = 48
# define how much sugar, butter and flour will be necessary for each amount of cookies entered
new_sugar = sugar / cookies * quantity
new_butter = butter / cookies * quantity
new_flour = cups_of_flour / cookies * quantity
# Let the user know how much of each item they will have to use
print("The amount of cookies you entered was " + (str(quantity)))
print("You will need to use: " + str(format(new_sugar, '.2f')) + " cups of sugar")
print("                      " + str(format(new_butter, '.2f') + " cups of butter"))
print("                      " + str(format(new_flour, '.2f') + " cups of flour"))
print("Enjoy your cookies!")