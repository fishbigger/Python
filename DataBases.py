def getIndexOf(string):
    i = 0
    for item in database:
        if item == string:
            return(i)
            break
        i += 1
def dpkg(data):
    database = []
    addToArray = ''
    for letter in data:
        if letter == ' ':
            database.append(addToArray)
            addToArray = ''
        else:
            addToArray = addToArray + letter
    return(database)

while True:           
    f = open('TestDatabase', 'r+')
    database = dpkg(f.read())
    f.close()
    indexBarcode = getIndexOf(input('Barcode'))
    indexBook = indexBarcode + 1
    indexAuthor = indexBarcode + 2

    print('Barcode: ' + database[indexBarcode])
    print('Book: ' + database[indexBook])
    print('Author: ' + database[indexAuthor])

    if database[indexBarcode + 3] == 'out':
        print('{0} is currently on loan to {1}'.format(database[indexBook], database[indexBarcode + 4]))
        Return = input('would you like to return {0}? (y,n) '.format(database[indexBook]))
        if Return == 'y':
            database[indexBarcode + 3] = 'in'
            database[indexBarcode + 4] = 'null'
        
    else:
        takeout = input ('Would you like to take {0} out (y, n)'.format(database[indexBook]))
        name = input('Whats your name?')
        if takeout == 'y':
            allowed = True
            i = 0
            for item in database:
                if item == name:
                    allowed = False
                    break
                i += 1
        
            if allowed:
                database[indexBarcode + 3] = 'out'
                database[indexBarcode + 4] = name
            else:
                print('You already have {0} out'.format(database[i-3]))
                


    with open('TestDatabase', 'w'): pass
    f = open('TestDatabase', 'w')
    for item in database:
        f.write(item + ' ')
    
    f.close()
    
    

