# This line tells python to import the arguments given when the program is run
from sys import argv

# Unpack the inputs, calling them script and filename respectively
script, filename = argv

# define variable txt to be the file with name "filename"
txt = open(filename)

# Tell user what file is about to be displayed
print "Here's your file %r:" % filename
# then display the file
print txt.read()

# Ask user to input the name of the file again
print "Type the filename again:"
# take filename given and assign it variable file_again
file_again = raw_input("> ")

# let txt_again be the file with name given above
txt_again = open(file_again)

# print out the file again
print txt_again.read()
