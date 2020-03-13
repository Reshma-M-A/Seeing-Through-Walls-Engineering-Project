from socket import *
import json
import os
import matplotlib.pyplot as plt
import matplotlib.animation

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('',1337))

fig, ax = plt.subplots()
x, y = [],[]
sc = ax.scatter(x,y)
plt.xlim(-100,100)
plt.ylim(-100,100)

def getData(i):
    x, y = [],[]
    broadcast_data=sock.recvfrom(1024)
    json_data = json.loads(broadcast_data[0].decode('utf-8'))
    os.system("CLS")
    if json_data != "":
        for target in json_data["targets"]:
            print("ID:{0}\n  X:{1}\n  Y:{2}\n  Z:{3}\n  A:{4}".format(target["targetID"],
                target["x"], target["y"], target["z"], target["a"]))
            x=target["x"]
            y=target["y"]
            ##x.append(target["x"])
            ##y.append(target["y"])
    sc.set_offsets([x,y])

ani = matplotlib.animation.FuncAnimation(fig, getData, frames=2, interval=100, repeat=True)
plt.show()
