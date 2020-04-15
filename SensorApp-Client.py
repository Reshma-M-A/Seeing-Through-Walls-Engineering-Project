from socket import *
from tkinter import *
import json
import os
import matplotlib.pyplot as plt
import matplotlib.animation

uservars = []

def show_entry_fields():
    ##print("minInCM: %s\nMaxInCm: %s\nresInCm: %s", (e1.get(), e2.get(), e3.get()))
    global uservars
    uservars = [e1.get(), e2.get(), e3.get()]

def getData():
    ipv4=sockrecv.recvfrom(16384*4)[0].decode('utf-8')
    targets = json.loads(ipv4)
    print(ipv4)
    return targets

sockrecv = socket(AF_INET, SOCK_DGRAM)
sockrecv.bind(('',5455))

socksend = socket(AF_INET, SOCK_DGRAM)
socksend.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socksend.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

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

Button(master, text='Send', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Save', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)


if __name__ == '__main__':
    master.mainloop()
    uservarsBytes = json.dumps(uservars).encode()

    socksend.sendto(uservarsBytes,('10.42.0.1',5454))
    fig, ax = plt.subplots()
    while True:
        ax.cla()
        ax.imshow(getData()[0])
        plt.pause(0.01)
