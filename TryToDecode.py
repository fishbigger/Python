f = open('TextToDecode.txt')
toDecode = f.read()

def StringToList(Str):
    output = []
    for l in Str:
        output.append(l)
    return(output)

def count(l):
    Chars = ' abcdefghijklmnopqrstuvwxyz1234567890!@£$%^&*()'
    chars = StringToList(Chars)
    charCount = []
    
    for i in range (len(chars)):
        charCount.append(0)

    for j in range (len(l)):
        for k in range (len(chars)):
            if chars[k] == l[j]:
                charCount[k] = charCount[k] + 1
                break
    return charCount
    
l = StringToList(toDecode)
charCount = count(l)

print(charCount)

#for i in range (len(l)):
#    print(l[i])
