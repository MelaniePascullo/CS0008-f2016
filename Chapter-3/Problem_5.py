mass = float(input("Enter mass of the object"))
weight = mass * 9.8
if weight < 100:
    print("Object is too light")
elif 100 <= weight <= 500:
    print(str(format(weight, '.2f')) + "newtons")
else:
    print("object is too heavy")