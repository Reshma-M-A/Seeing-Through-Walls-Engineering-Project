from __future__ import print_function
from sys import platform
from os import system
from imp import load_source
from os.path import join
import json
from socket import *

if platform == 'win32':
    modulePath = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK',
    'python', 'WalabotAPI.py')
elif platform.startswith('linux'):
    modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py') 

socksend = socket(AF_INET, SOCK_DGRAM)
socksend.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socksend.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

sockrecv = socket(AF_INET, SOCK_DGRAM)
sockrecv.bind(('',5454))

wlbt = load_source('WalabotAPI', modulePath)
wlbt.Init()

def SensorApp(receivedVariables):
    minInCm = int(receivedVariables[0])
    maxInCm = int(receivedVariables[1])
    resInCm = int(receivedVariables[2])
    minIndegrees, maxIndegrees, resIndegrees = -0, 20, 10
    minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees = -60, 60, 1
    mtiMode = False
    wlbt.Initialize()
    wlbt.ConnectAny()
    wlbt.SetProfile(wlbt.PROF_SENSOR)
    wlbt.SetArenaR(minInCm, maxInCm, resInCm)
    wlbt.SetArenaTheta(minIndegrees, maxIndegrees, resIndegrees)
    wlbt.SetArenaPhi(minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees)
    filterType = wlbt.FILTER_TYPE_MTI if mtiMode else wlbt.FILTER_TYPE_NONE
    wlbt.SetDynamicImageFilter(filterType)
    wlbt.Start()
    if not mtiMode:
        wlbt.StartCalibration()
	print("Calibrating")
    while wlbt.GetStatus()[0] == wlbt.STATUS_CALIBRATING:
        wlbt.Trigger()
    while True:
        appStatus, calibrationProcess = wlbt.GetStatus()
        wlbt.Trigger()
        targets = wlbt.GetRawImageSlice()
        #rasterImage, _, _, sliceDepth, power = wlbt.GetRawImageSlice()

        socksend.sendto(json.dumps(targets),('10.42.0.240',5455))
        
        print("Sent Data.")
    wlbt.Stop()
    wlbt.Disconnect()
    wlbt.Clean()
    print('Terminate successfully')

if __name__ == '__main__':
    receivedVariables = json.loads(sockrecv.recvfrom(16384)[0])
    SensorApp(receivedVariables)
