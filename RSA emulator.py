# selects E based on
def ChooseE(A):
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
    Current = M**E
    Cipher = Current % N
    return Cipher

# Add comment
def DecodeCipher(C, D, N):
    current = C**D
    DecodedM = current % N
    return int(DecodedM)

# Add comment
def Encode(M):
    return ord(M)

# Add comment
def Decode(M):
    return chr(M)

def getPrimes():
    f = open('primes','r')
    primes = f.readlines()
    f.close()
    return primes

primes = getPrimes()
    
P = 811
Q = 773
N = (P*Q)
Phi = ((P-1)*(Q-1))

e = (ChooseE(Phi))
d = ChooseD(Phi, e)

Public = [N, e]

Message = ('Hello World')
mList = []
for m in Message:
    mList.append(Encode(m))

# Add comment
cList = []
for m in mList:
    C = CreateCipher(m, Public[0], Public[1])
    cList.append(C)

#Add comment
DecodedM = []
for c in cList:
    M = DecodeCipher(c, d, N)
    DecodedM.append(M)

#Add comment
NewDecodedM = []
for m in DecodedM:
    NewDecodedM.append(Decode(m))
print(''.join(NewDecodedM))
