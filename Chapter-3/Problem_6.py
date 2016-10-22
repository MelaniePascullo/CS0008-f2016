month = int(input("Please enter a month in numeric form"))
day = int(input("Please enter a day"))
year = int(input("Please enter the last two digits of a year"))
if month * day == year:
    print("Your date is magic!")
else:
    print("Your date is not magic.")
