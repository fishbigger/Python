def StringToList(String):
    List = []
    for s in String:
        List.append(s)
    return List
# selects E based on
def ChooseE(A, primes):
    for prime in primes:
        if not int(A) % int(prime) == 0:
            e = int(prime)
            break
    return e

# Add comment
def ChooseD(A, E):
    for k in range(int(A+1), int(A*E), int(A)):
            if k % E == 0:
                d = (k/E)
                break
    return int(d)

# Add comment
def CreateCipher(M, N, E):
    Current = int(M)**int(E)
    Cipher = int(Current) % int(N)
    return Cipher

# Add comment
def DecodeCipher(C, D, N):
    current = int(C)**int(D)
    DecodedM = current % N
    return int(DecodedM)

# Add comment
def letterToNumber(M):
    return ord(M)

# Add comment
def numberToLetter(M):
    return chr(M)

def getPrimes():
    f = open('primes','r')
    primes = f.readlines()
    f.close()
    return primes


def setupValues(P,Q, primes):
    N = (P*Q)
    Phi = ((P-1)*(Q-1))

    e = ChooseE(Phi, primes)
    d = ChooseD(Phi, e)

    Public = [N, e]
    return Public, d, N

def encodeMessage(message, publicKey):
    mList = []
    for m in message:
        mList.append(letterToNumber(m))
    # Add comment
    cList = []
    for m in mList:
        C = CreateCipher(m, publicKey[0], publicKey[1])
        cList.append(C)
    return cList

def decodeMessage(cipher, d, N):
    DecodedM = []
    for c in cipher:
        M = DecodeCipher(c, d, N)
        DecodedM.append(M)

    #Add comment
    NewDecodedM = []
    for m in DecodedM:
        NewDecodedM.append(numberToLetter(m))

    return NewDecodedM
