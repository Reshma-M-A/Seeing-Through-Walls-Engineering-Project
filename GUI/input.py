from Tkinter import *

def show_entry_fields():
    print("minInCM: %s\nMaxInCm: %s\nresInCm: %s", (e1.get(), e2.get(), e3.get()))
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

master = Tk()
Label(master, text="minInCm").grid(row=0)
Label(master, text="maxInCm").grid(row=1)
Label(master, text="resInCm").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
#  minInCm, maxInCm, resInCm = 30, 200, 3
e1.insert(10, "30")
e2.insert(10, "200")
e3.insert(10, "3")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=W, 
                                                               pady=4)

master.mainloop()

mainloop()
