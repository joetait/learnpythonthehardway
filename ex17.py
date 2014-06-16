from sys import argv

script, from_file, to_file = argv

#we could these two on one line too, how?
indata =open(from_file).read()



out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
