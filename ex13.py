from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "I need one more variable: ",
last_thing = raw_input()
print "Your final variable is %r" % last_thing
