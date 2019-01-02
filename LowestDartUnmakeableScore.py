def canNumBeMade(n):
    possible = []

    for i in range(1, 21):
        possible.append(i)
        possible.append(i * 2)
        possible.append(i * 3)

    possible.append(25)
    possible.append(50)

    #print(possible)

    total = int(n)
    possibleOutcomes = []

    for d1 in possible:
        for d2 in possible:
            for d3 in possible:
                total = total - (d1 + d2 + d3)
                if total == 0:
                    dart1 = makeSingleDart(d1)
                    dart2 = makeSingleDart(d2)
                    dart3 = makeSingleDart(d3)

                    newDart3 = str(dart3[0])
                    if newDart3[0] == 'D':
                        #possibleOutcomes.append("{0} {1} {2}".format(dart1[0],dart2[0],dart3[0]))
                        return "{0} {1} {2}".format(dart1[0],dart2[0],dart3[0])
                    #return True
                total = int(n)

    return False


def makeSingleDart(num):
    #print(num)
    possibleWays = []
    n = int(num)
    if n < 20:
        possibleWays.append(n)
    if n % 2 == 0:
        l = int(n/2)
        if l <= 20:
            possibleWays.append("T{0}".format(l))
    if n % 3 == 0:
        l = int(n/3)
        if l <= 20:
            possibleWays.append("T{0}".format(l))
    if n == 50:
        possibleWays.append("D25")
    if n == 25:
        possibleWays.append("25")
        
    return possibleWays
                    



for i in range(3, 180):
    if not canNumBeMade(i):
       print(i)
        

while True:
    val = canNumBeMade(input("Num"))
    print(val)

    #val = makeSingleDart(input("Num"))
    #print(val)
