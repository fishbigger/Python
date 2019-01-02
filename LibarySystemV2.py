from tkinter import *

def setup(wi, he):
    global w
    w = Tk()

#    canvas_width = w
#    canvas_height = h
#    w = Canvas(master, 
#    width=canvas_width,
#           height=canvas_height)
#    w.pack()

def TakeOutBCallback():
    TakeOutB.pack_forget()
    

def takeOut():
    

setup(800, 400)
TakeOutB = Button(w, text = "Take Out", command = TakeOutBCallback)
takeOutB = Button(w, text = "Take Out", command = takeOut)
TakeOutB.pack()
