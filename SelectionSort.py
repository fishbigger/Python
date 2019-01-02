from random import randint
import time

def findLargest(l):
    currrentLargest = 0
    for i in l:
        if i > currrentLargest:
            currrentLargest = i
    return currrentLargest

def sort(l):
    newList = []
    oldList = l

    for i in range(len(l)):
        largest = findLargest(oldList)
        newList.append(largest)
        oldList.remove(largest)
        #print(list(reversed(newList)))
        
    
    return newList[::-1]

length = int(input('Length'))

for i in range 10:

    l = []
    for i in range(length):
        l.append(randint(0, 100))
    
    start = time.clock()
    
    temp = sort(l)

    end = time.clock()

    print("")
