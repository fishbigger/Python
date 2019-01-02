from math import sqrt
f = open('Primes', 'r')
try:
    lines = f.readlines()
except Exception as inst:
    print(inst)
finally:
    f.close()

try:
    changeBy = 100
    percentage = 10
    primes = lines
    length =len(primes)
    if int(lines[-1]) % 2 == 0:
        start = int(lines[-1]) + 1
    else:
        start = int(lines[-1]) + 2
    print('starting at: ' + str(start))
    end = (start + changeBy)
    progress = 0
    for i in range (start, end, 2):
        isPrime = True
        for prime in primes:
            if i % int(prime) == 0:
                isPrime = False
            if not isPrime or int(prime) > sqrt(i):
                break
        if isPrime:
            primes.append(i)
        progress = (progress + 2)
        if progress % (changeBy/percentage) == 0:
            print(str(int(progress/(changeBy/percentage)*10)) + '% done')
except Exception as inst:
    print(inst)
finally:
    f = open('Primes', 'w')
    try:
        f.truncate()
        for prime in primes:
            f.write("%s\n" % int(prime))
            
        f.close()
    except Exception as inst:
        print(inst)
    finally:
        f.close()
        print('last found prime: ' + str(primes[-1]))
        print(str(len(primes)-length) + ' primes found')
