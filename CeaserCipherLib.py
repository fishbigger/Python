def StringToList(Str):
    output = []
    for l in Str:
        output.append(l)
    return(output)

def encode(M, key):
    MList = StringToList(M)
    topRow = 'abcdefghijklmnopqrstuvwxyz1234567890!@£$%^&*()_ '
    bottomRow = ''
    for i in range(len(topRow)):
        bottomRow = bottomRow + topRow[i + key]

    encodedMessage = ''
    for letter in MList:
        for i in range(len(topRow)):
            if topRow[i] == letter:
                encodedMessage = encodedMessage + bottomRow[i]
                break
    return(encodedMessage)

def decode(C, key):
    
    Clist = StringToList(C)
    decodedMessage = ''
    for letter in Clist:
        for i in range(len(bottomRow)):
            if bottomRow[i] == letter:
                decodedMessage = decodedMessage + topRow[i]
                break
    return(decodedMessage)

print(encode('hello', 1))






