#
#
# name       : Melanie Pascullo
# email      : mgp26@pitt.edu
# class      : CS0008-f2016
# instructor : Max Novelli

# Final Project
1


# example we had in class
"""# class definition
class definition
    ***participant class***

    # properties
    # methods
    # initializer methods
    def _init_(self,name,distance=0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0:
            #set distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1
        # end if
    #end def _init_

    # add distance method
    def addDistance(self,distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
        # end if
    # end def addDistance

    # return the name of the participants
    def getName(self):
        return self.name
    # end def getName

    # return the total distance run computed
    def getDistance(self):
        return self.distance
    # end def getDistance

    #return the number of runs
    def getRuns(self):
        return self.runs
    # end def getRuns

    # stringify the object
    def _str_(self):
        return \
            "Name : " + format(self.name,'>20s')
    # end def _init_

    # convert to cav
    def tocsv(self):
        return ','.join(self.name, str(self.runs), str(self.distance))
    # end def tocsv
# end class participant"""

# Also I tried searching for ways to comment out big blocks of code and this was the best
# that I could find, is this the best way?

# define the master file
master_file = "f2016_cs8_a3.data"

dictionary = {}
outfile = open('output.txt', 'w')

def process_file(filename, d):
    file = open(filename, 'r')
    file.readline()
    num_lines = 0

def print_kv(key, value, lenkv=30)
    if isinstance (value, float):
        f_str = '010.5f'
    elif isinstance (value, int):
        f_str = '2d'
    else:
        f_str = 's'
    print(format(key, str(lenkv) + 's') + ": " + format(value, f_str))
    return

total_num_lines = 0
num_files = 0
for data_file in master:
    data_file - data_file.rstrip("\n")
    my_list = process_file(data_file, dictionary)
    dictionary.update(my_list[0])
    total_num_lines += my_list[1]
    num_files =+ 1

master.close()

# Define the class
# Make sure to capitalize the class name
class Marathon:
    # initializer method
    def __init__(self, name, distance=1):
        # define variables
        name = self.name
        If distance > 0
            # define variables
            distance = self.distance

    # end def __int__








