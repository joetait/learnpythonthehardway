
def list_numbers(length, inc):
    numbers = []
    for i in range (0,length,inc):
        print "At the top i is %d" % i
        numbers.append(i)   
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    return numbers

numbers = list_numbers(20,3)


#
#def list_numbers(length, inc):
#    i = 0
#    j = inc
#    numbers = []
#    while i < length:
#        print "At the top i is %d" % i
#        numbers.append(i)
#    
#        i = i + j
#        print "Numbers now: ", numbers
#        print "At the bottom i is %d" % i
#
#    return numbers
#        
#numbers = list_numbers(10,2)

print "The numbers: "

for num in numbers:
    print num
