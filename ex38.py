ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there's not 10 things on that list, let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["Day", "night", "Song", "Frisbee", "Corn"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # Whoa! Fancy
print stuff.pop()
print ' '.join(stuff) #what? cool
print "#".join(stuff[3:5]) # super stellar!

