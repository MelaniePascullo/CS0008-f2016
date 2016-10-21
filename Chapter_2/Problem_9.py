temp = float(input("Enter temperature in degrees celcius"))
# define the formula for converting celcius to fahrenheit
fahrenheit = temp * 9 // 5 + 32
print("Temperature entered was " + str(format(temp, '.0f')) + " degrees celcius")
print("This is equal to " + str(format(fahrenheit, '.0f')) + " degrees fahrenheit")
