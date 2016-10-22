# Introduce the color creator
print("Welcome to the color creator, where you will combine two primary colors to create another color.")
print("Primary colors are Red, Blue and Yellow.")
# Ask user to input two primary colors
primary1 = (input("Enter the first primary color"))
primary2 = (input("Enter the second primary color"))
# Create an if-elif statement to show which color has been made
if primary1 == "Red" and primary2 == "Blue":
    print("You have made purple!")
elif primary1 == "Blue" and primary2 == "Red":
    print("You have made purple!")
elif primary1 == "Red" and primary2 == "Yellow":
    print("You have made orange!")
elif primary1 == "Yellow" and primary2 == "Red":
    print("You have made orange!")
elif primary1 == "Blue" and primary2 == "Yellow":
    print("You have made green!")
elif primary2 == "Yellow" and "Blue":
    print("You have made green!")
else:
    print("You did not choose two primary colors")