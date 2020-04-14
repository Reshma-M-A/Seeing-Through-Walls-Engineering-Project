from Tkinter import *


root = Tk()

def myClick():
    myLabel1 = Label(root, text="Look I clicked a Button!")
    myLabel1.pack()


# Creating a Button widget
myButton = Button(root, text="Click me!", command=myClick)
myButton.pack()


root.mainloop()