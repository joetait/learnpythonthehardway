#Take arguments given when running program
from sys import argv 

#unpack argv as script and filename
script, filename = argv

#print some lines, asking the user whether they are happy to erase the file they input
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."
print "In case you are wondering, the file contents is:"
#set text to be the file they input
text = open(filename)
#Print the contents of the file so they can check they are happy to delete it
print text.read()

#Take input from user to decide whether to erase the file
raw_input("?")

print "Opening the file..."
#open the file in order to delete the contents
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#delete the contents
target.truncate()

#Tell user they need to input three lines of text
print "Now I'm going to ask you for three lines."

#three lines of input, assigning them to line1, line2 and line3
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#write the input lines to the file
target.write("%s \n %s \n %s \n" % (line1, line2, line3))


print "And finally, we close it."
#close the file
target.close()

#Set text to be the contents of the (newly edited) file
text = open(filename)
print "Your file now reads as follows:"
#print new file
print text.read()
