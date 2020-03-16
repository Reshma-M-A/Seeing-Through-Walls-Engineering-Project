from __future__ import print_function # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import json
from threading import Thread
import time
from socket import *

if platform == 'win32':
	modulePath = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK',
		'python', 'WalabotAPI.py')
elif platform.startswith('linux'):
    modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')

walabot = load_source('WalabotAPI', modulePath)
walabot.Init()

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

def NetworkSendTargets(targets):
    if targets:
        data = {"targets": []}
        for i, target in enumerate(targets):
            data["targets"].append({
                "targetID":i,
                "x": target.xPosCm,
                "y": target.yPosCm,
                "z": target.zPosCm,
                "a": target.amplitude
            })
        sock.sendto(json.dumps(data), ('255.255.255.255', 5455))

def Sensor():
    ArenaMinimumSize, ArenaMaximumSize, ArenaResolution = 30, 200, 3
    ArenaMinimumDegrees, ArenaMaximumDegrees, ArenaDegreesResolution = -15, 15, 5
    ArenaMinimumPhi, ArenaMaximumPhi, ArenaPhiResolution = -60, 60, 5
    mtiMode = False

    walabot.Initialize()
    walabot.ConnectAny()

    walabot.SetProfile(walabot.PROF_SENSOR)

    walabot.SetAreanaR(ArenaMinimumSize, ArenaMaximumSize, ArenaResolution)
    walabot.SetArenaTheta(ArenaMinimumDegrees, ArenaMaximumDegrees, ArenaDegreesResolution)
    walabot.SetAreanaPhi(ArenaMinimumPhi, ArenaMaximumPhi, ArenaPhiResolution)

    filterType = walabot.FILTER_TYPE_MTI if mtimode else walabot.FILTER_TYPE_NONE
    walabot.SetDynamicImageFilter(filterType)
    
    walabot.Start()
    
    if not mtiMode:
        input("Calibration Required. Press any key once area is clear...")
        walabot.StartCalibration()
        while walabot.GetStatus()[0] == walabot.STATUS_CALIBRATING:
            print("Calibrating...")
            walabot.Trigger()
    
    while True:
            appStatus, calibrationProcess = walabot.GetStatus()
            walabot.Trigger()
            targets = walabot.GetSensorTargets()
            rasterImage, _, _, sliceDepth, power = walabot.GetRawImageSlize()
            NetworkSendTargets(targets)
    
    walabot.Stop()
    walabot.Disconnect()
    walabot.Clean()
    print("Terminated Successfully.")

if __name__ == '__main__':
    Sensor()