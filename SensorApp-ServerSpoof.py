from __future__ import print_function # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import json
from threading import Thread
import time
from socket import *

def NetworkSendTargets(targets):
    if targets:
        
        sock.sendto(json.dumps(data), ('255.255.255.255', 5455))

def Sensor():
    ArenaMinimumSize, ArenaMaximumSize, ArenaResolution = 30, 200, 3
    ArenaMinimumDegrees, ArenaMaximumDegrees, ArenaDegreesResolution = -15, 15, 5
    ArenaMinimumPhi, ArenaMaximumPhi, ArenaPhiResolution = -60, 60, 5

    while True:
        targets = {}
        

if __name__ == '__main__':
    Sensor()