width_1 = int(input("Enter the width of the first rectangle"))
length_1 = int(input("Enter the length of the first rectangle"))
width_2 = int(input("Enter the width of the second rectangle"))
length_2 = int(input("Enter the length of the second rectangle"))
rectangle_1 = width_1 * length_1
rectangle_2 = width_2 * length_2
if rectangle_1 < rectangle_2:
    print("The area of rectangle 1 is less than the area of rectangle 2.")
elif rectangle_1 > rectangle_2:
    print("The area of rectangle 1 is greater than the area of rectangle 1.")
else:
    print("The area of rectangle 1 is equal to the area of rectangle 2.")