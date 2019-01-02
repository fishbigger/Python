from rsaLib import setupValues, encodeMessage, decodeMessage, getPrimes

primes = getPrimes()
    
P = 811
Q = 773

Public, d, N = setupValues(P,Q, primes)

Message = ('Hello World')

cList = encodeMessage(Message, Public)

NewDecodedM = decodeMessage(cList, d, N)

print(''.join(NewDecodedM))
