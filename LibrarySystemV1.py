from tkinter import *
def Return():
    titleEntry.grid_forget()
    authorEntry.grid_forget()
    barcodeEntry.grid_forget()
    addBookButton.grid_forget()
    titleLabel.grid_forget()
    authorLabel.grid_forget()
    barcodeLabel.grid_forget()
    takeOutButton2.grid_forget()
    quitButton.grid_forget()
    yearLabel.destroy()
    yearEntry.grid_forget()
    takeOutLabel.grid_forget()
    takeOutButton3.grid_forget()
    searchButton.grid_forget()
    barcodeEntry2.grid_forget()
    printData.grid_forget()
    newBookButton.grid(row = 0)
    takeOutButton.grid(row = 1)
    getDataButton.grid(row = 2)
    
def search():
    searchButton.grid_forget()
    barcodeEntry.grid_forget()
    barcodeLabel.grid_forget()
    quitButton.grid(row = 0)

    barcode = barcodeEntry.get()
    if barcode in library:
        if library[barcode]['in']:
            takeOutLabel.grid(row = 2, column = 0)
            takeOutButton2.grid(row = 0, column = 2)
    else:
        Return()

def finalyTakeOut():
    bookBarcode = barcodeEntry.get()
    personBarcode = barcodeEntry2.get()
    library[bookBarcode]['in'] = False
    library[bookBarcode]['who_got_it'] = personBarcode
    library[bookBarcode]['year'] = yearEntry.get()
    setData()

def takeOut():
    newBookButton.grid_forget()
    takeOutButton.grid_forget()
    getDataButton.grid_forget()
    #takeOutLabel.grid_forget()

    quitButton.grid(row = 1)
    
    searchButton.grid(row = 1, column = 1)
    barcodeEntry.grid(row = 0, column = 1)
    barcodeLabel.grid(row = 0, column = 0)

def takeOutBook():
    
    takeOutButton2.grid_forget()
    takeOutLabel.grid_forget()

    barcodeEntry2.grid(row = 1, column = 1)
    barcodeLabel.grid(row = 1, column = 0)

    yearEntry.grid(row = 2, column = 1)
    yearLabel.grid(row = 2, column = 0)

    takeOutButton3.grid(row = 0,  column = 1)

def setData():
    Return()
    
    with open('library.txt', 'w'): pass
    f = open('Library.txt', 'r+')
    f.write( str(library) )
    f.close()
    
def addBook(Author, Title):
    book = {}
    book['Author'] = Author
    book['Title'] = Title
    book['in'] = True
    book['who_got_it'] = None
    book['year'] = None
    book['name'] = None
    return book
    
def newBookEntry():
    newBookButton.grid_forget()
    takeOutButton.grid_forget()
    getDataButton.grid_forget()
    
    titleLabel.grid(row = 0)
    authorLabel.grid(row = 1)
    barcodeLabel.grid(row = 2)
    quitButton.grid(row = 3)
    
    titleEntry.grid(row = 0, column = 1)
    authorEntry.grid(row = 1, column = 1)
    barcodeEntry.grid(row = 2, column = 1)
    addBookButton.grid(row = 3, column = 1)
def getData():
    f = open('Library.txt', 'r+')
    file = f.read()
    library = eval(file)
    return library
def addBook():
    library[barcodeEntry.get()] = addBook(authorEntry.get(), titleEntry.get())
    setData()
def askData():
    newBookButton.grid_forget()
    takeOutButton.grid_forget()
    getDataButton.grid_forget()    
    
    yearLabel.grid(column = 0)
    yearEntry.grid(column = 1, row = 0)
    printButton.grid(column = 1, row = 1)
    
def Print():
    global toPrint
    
    yearLabel.grid_forget()
    yearEntry.grid_forget()
    printButton.grid_forget()
    stringList = []

    for barcode in library:
        if library[barcode][year] == yearEntry.get():
            string = library[barcode][who_got_it] + '-'
            string += library[barcode][name] + '-'
            string += library[barcode][Title]
            
master = Tk()
master.title('librarySystem')
#master.config(bg = '#006400')


global library

library = getData()

global newBookButton
global takeOutButton
global getDataButton

newBookButton = Button(master, text = 'NewBook', command = newBookEntry)
takeOutButton = Button(master, text = 'TakeOut', command = takeOut)
getDataButton = Button(master, text = 'GetData', command = askData)

newBookButton.grid(row = 0)
takeOutButton.grid(row = 1)
getDataButton.grid(row = 2)

global titleEntry
global authorEntry
global barcodeEntry
global barcodeEntry2
global takeOutEntry
global yearEntry

global addBookButton
global searchButton
global quitButton
global takeOutButton2
global takeOutButton3
global printButton

global titleLabel
global authorLabel
global barcodeLabel
global takeOutLabel
global yearLabel 

titleEntry = Entry(master)
authorEntry = Entry(master)
barcodeEntry = Entry(master)
barcodeEntry2 = Entry(master)
yearEntry = Entry(master)

titleLabel = Label(master, text = 'Title: ')
authorLabel = Label(master, text = 'Author: ')
barcodeLabel = Label(master, text = 'Barcode: ')
takeOutLabel = Label(master, text = 'Would you like to take it out?')
yearLabel = Label(master, text = 'Year: ')

addBookButton = Button(master, text = 'AddBook', command = addBook)
searchButton = Button(master, text = 'Search', command = search)
quitButton = Button(master, text = 'Quit', command = Return)
takeOutButton2 = Button(master, text = 'takeOut?', command = takeOutBook)
takeOutButton3 = Button(master, text = 'takeOut?', command = finalyTakeOut)
printButton = Button(master, text = 'printData?', command = Print)

#while True:
#    f = open('Library.txt', 'r+')
#    file = f.read()
#    library = eval(file)
#    
#    barcode = input('Barcode: ')
#    if barcode in library:
#        print('Title: {0}'.format(library[barcode]['Title']))
#        print('Author: {0}'.format(library[barcode]['Author']))
#    else:
#        print('Book not in library!')
#
#    with open('library.txt', 'w'): pass
#    f = open('Library.txt', 'r+')
#    f.write( str(library) )
#    f.close()

    

