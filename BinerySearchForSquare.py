def findMiddle(a, b):
	diff = b - a
	mid = b - diff / 2
	return mid

while True:
    target = int(input("Squared"))
    lowBound = 0
    highBound = target
    i = findMiddle(int(lowBound), int(highBound))
    #print (i)

    n = 0 

    while not i**2 == target:

        if i**2 > target:
                highBound = i
                i = findMiddle(lowBound, highBound)
        else:
                lowBound = i
                i = findMiddle(lowBound, highBound)

        n += 1

        if n >= 100:
                break
        #print (i)

    repr(i)
	
