from rsaLib import decodeMessage, setupValues, getPrimes, StringToList

P = 7
Q = 3

#Creates Public key and prints it
primes = getPrimes()
Public, d, N = setupValues(P,Q, primes)
print('PublicKey: {0}'.format(Public))

#Asks for cipher
cList = StringToList(input('Cipher?'))
#Decodes cipher and prints
decodedM = decodeMessage(cList, d, N)
print(''.join(decodedM))
