# introduce the system
print("Welcome to the day of the week generator")
# Ask user to choose a number
day = int(input("Enter a number 1-7 that corresponds to a day of the week"))
if day == 1:
    print("Monday!")
elif day == 2:
    print("Tuesday!")
elif day == 3:
    print("Wednesday!")
elif day == 4:
    print("Thursday!")
elif day == 5:
    print("Friday!")
elif day == 6:
    print("Saturday!")
elif day == 7:
    print("Sunday!")
else:
    print("You did not enter a number 1-7.")
