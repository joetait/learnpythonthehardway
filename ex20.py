#This line imports the arguments given when the program is run  
from sys import argv

# This line assigns variable names to the inputs given, unpacking argv
script, input_file = argv

#This defines a function, called print_all, which takes one input
def print_all(f):
# This line reads out the file input to print_all
    print f.read()

# Define function rewind with one input
def rewind(f):
# reset file so it reads from first line   
    f.seek(0)


# function that takes a file and number and prints out that line of file
def print_a_line(line_count, f):
# print line number, then contents of line 
    print line_count, f.readline()

# set current file to be the input file
current_file = open(input_file)

print "First let's print the whole file:\n"

# print the contents of the input file 
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# apply rewind to input file, to reset where it is read from
rewind(current_file)


print "Let's print three lines:"

# set current line to be 1, since we will be reading from the first line
current_line = 1
# print first line, numbered, using print_a_line function
print_a_line(current_line, current_file)

current_line +=  1
print_a_line(current_line, current_file)

current_line +=  1
print_a_line(current_line, current_file)
