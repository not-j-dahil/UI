#simple GUI

from tkinter import *

#create the window
root = Tk()

#Variables
counter = 0

#modify root window
root.title("Simple GUI")
root.geometry("640x360")

#creating label
label = Label(root, text = "This is a label!")

def button1Funct():
    '''Function for button1'''
    global counter #global needed for 'UnboundLocalError: local variable 'counter' referenced before assignment'
    counter += 1
    label.config(text=counter)

#creating a button
button1 = Button(root, text = "Button")
button1["command"] = button1Funct


#pack = put into the window
button1.pack(side=LEFT)
label.pack(side=LEFT)


#kick off the event loop
root.mainloop()
