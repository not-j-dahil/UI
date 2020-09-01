#simple GUI

from tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Simple GUI")
root.geometry("640x360")

app = Frame(root)
app.grid()
label = Label(app, text = "This is a label!")

label.grid()

#kick off the event loop
root.mainloop()
