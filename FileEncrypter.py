from tkinter import *

def Encrypt():
    

M = Tk()
M.title('FileEncrypt')

C = Canvas(M, width = 200, height = 150)
C.pack()

L1 = Label(C, text = 'One of your files is about to be encrrypted.')
L1.grid(row = 0, column = 0)

OkButton = Button(C, text = 'Ok', command = Encrypt)
OkButton.grid(row = 1, column = 0) 

