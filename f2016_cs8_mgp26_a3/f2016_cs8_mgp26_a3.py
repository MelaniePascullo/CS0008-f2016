#
# name      : Melanie Pascullo
# email     : mgp26@pitt.edu
# class     : CS0008 - F2016
# instructor: Max Novelli
#
# Notes:
# MN: more comments please!!!
# MN: please indent comments properly, following the code indentation
# MN: please pay attention to code indentation
# MN: IMPORTANT: are you sure that you commit the right code?
#

# MN: can you explain what this line is for?
#f2016_cs8_a3.data.1.csv = 'letters'
# MN: the following 3 statements are not useful?
#     are you missing some code or are you just testing that the file exists?
#fh = open("f2016_cs8_a3.data.1.csv","r")
#fh = open(filename,"r")
#fh.close()

# MN: why not asking the user for the master list file name?
dataSources = "f2016_cs8_a3.data.txt"
fh = open(dataSources, "r")
sourceFiles = fh.readlines()
fh.close()
sourceFiles = [item.strip('\n') for item in sourceFiles]
sourceFiles

# initialize data container
data = []
# loop on all data files
for source in sourceFiles:
    # open current data file for reading
    fh = open(source,'r')
    # loop on all the lines
    for line in fh:
        # check if it is a header
        if not 'distance' in line:
            # read the whole file in
            data.append( fh.readlines())
    #close file
    fh.close()

    # MN: this code block is not properly indentent
    #
    # to find the number of files read in input
    #    filename = 'letters'
    #    fh = open(filename, 'r')
    #    words = fh.readlines()
    #    fh.close()

# number of words in the file
letters3 = [(line.strip('\n').lower() for line in words]
# number of words in the file with no duplicates
words_no_duplicates = list(set(letters3))
# number of words with no duplicates sorted
words_no_duplicates.sort()
# length of files
len[(f2016_cs8_a3.data.txt)]
# minimum amount of letters in words
        min(letters_length)
# max amount of letters in words
max(letters_length)
nwords = 0
        for item in words_length
            if item == 5:
                nwords += 1
# count words with certain length
def countWordsOfLength(1):
            nwords = 0
            for item in words_length:
                if item == 1:
                    nwords += 1
            return nwords



