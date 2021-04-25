import sys
import random

#import variables from command line
#print(sys.argv)
assert(len(sys.argv) == 4)
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

#print((trials,days,people))

collisions = 0
for t in range(trials):
    #create an empty calander
    calendar = [0] * days
    for i in range(days):
        calendar.append(0)
    #print(calendar)
    #fill with empty birthdays
    for i in range(people):
        bd = random.randint(0,days-1)
        calendar[bd] +=1
    #print(calendar)
    #are there any collisions
    found = False
    for v in calendar: #will give you the number
        if v > 1:
            found = True
            break
    #add one if we find any collisions
    if found: collisions += 1
print(collisions/trials)
