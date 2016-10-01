# define variables
distance = "what was the total distance traveled?"
gas = "what was the total gas used?"
measurement = str(input("usc or metric?"))
# create an if-elif statement to determine km or miles
# also asks the user the distance traveled
if measurement == "usc":
    distance = str(input("what was the total distance traveled in miles? (include unit of measurement) "))
elif measurement == "metric":
    distance = str(input("what was the total distance traveled in km? (include unit of measurement) "))
else:
    print("invalid answer")
print(distance)
# create an if-elif statement to convert miles to km and km to miles
if measurement == "usc":
    new_distance = print(distance) * int(1.60934)
elif measurement == "metric":
    new_distance = (distance) * int(0.621371)
    print(new_distance)
else:
    print("invalid answer")
# create an if-elif statement to ask user quantity of gas
if measurement == "usc":
    gas = str(input("what was the total gas used in gallons? (include unit of measurement "))
elif measurement == "metric":
    gas = str(input("what was the total gas used in liters? (include unit of measurement )"))
else:
    print("invalid answer")
print(gas)
# show formula for consumption of gas
consumption = (distance) / (gas)
print(consumption)
# create an if-elif statement to determine what the gas consumption rating is
if consumption > 20:
    print("gas consumption rating is extremely poor")
elif 15 < consumption <= 20:
    print("gas consumption rating is poor")
elif 10 < consumption <= 15:
    print("gas consumption rating is average")
elif 8 < consumption <= 10:
    print("gas consumption rating is good")
elif consumption <= 8:
    print("gas consumption rating is excellent")
else:
    print("invalid consumption")
