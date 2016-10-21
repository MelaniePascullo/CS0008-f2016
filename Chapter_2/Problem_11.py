# Introduce the program
print("Ever wonder what percent of your class is male vs female?")
# Ask user amount of males and females in the class
females = int(input("How many females are in this class?"))
males = int(input("How many males are in this class?"))
# Create formulas to calculate percent of males and females
percent_females = females / (females + males)
percent_males = males / (females + males)
# Let the user know the results, and convert the data to a percent using format
print(str(format(percent_females, '.0%')) + " of your class is female")
print(str(format(percent_males, '.0%')) + " of your class is male")
