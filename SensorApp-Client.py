from socket import *
import json
import os
import matplotlib.pyplot as plt
import matplotlib.animation

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('',1337))

figure, axis = plt.subplots()
x, y = [],[]
scatterPlot = axis.scatterPlotatter(x,y)
plt.xlim(-100,100)
plt.ylim(-100,100)

def getData(i):
    x, y = [],[]
    multicastData=sock.recvfrom(1024)
    targets = json.loads(multicastData[0].decode('utf-8'))
    os.system("CLS")
    if targets != "":
        for target in targets["targets"]:
            print("ID:{0}\n  X:{1}\n  Y:{2}\n  Z:{3}\n  A:{4}".format(target["targetID"],
                target["x"], target["y"], target["z"], target["a"]))
            x=target["x"]
            y=target["y"]
    scatterPlot.set_offsets([x,y])

ani = matplotlib.animation.FuncAnimation(figure, getData, frames=2, interval=100, repeat=True)
plt.show()
