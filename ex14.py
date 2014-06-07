from sys import argv

script, user_name, user_age = argv
prompt = '*'

print "Hi %sm I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live in %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me, and you are %s years old.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, user_age, lives, computer)
