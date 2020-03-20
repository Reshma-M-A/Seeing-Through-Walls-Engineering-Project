from socket import *
import json
import os
import matplotlib.pyplot as plt
import matplotlib.animation

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('',5455))

def getData():
    ipv4=sock.recvfrom(16384)[0].decode('utf-8')
    targets = json.loads(ipv4)
    print(ipv4)
    return targets

fig, ax = plt.subplots()

while True:
    ax.cla()
    ax.imshow(getData()[0])
    plt.pause(0.1)