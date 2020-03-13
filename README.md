# Seeing-Through-Walls-Engineering-Project
This is an honours project. 

# Purpose

# Technologies

# Setting it Up
Power up RPi
Connect to WiFi ubiquityrobots2222 - robotseverywhere
Open 3x SSH sessions to ubuntu@10.42.0.1
Password: walabotSLAVE
SSH 1 (walabot sensor)
cd Desktop
python SensorApp.py
SSH 2 (ros ‘server’)
roslaunch turtlebot_bringup minimal.launch
SSH 3 (operator)
roslaunch turtlebot_teleop keyboard_teleop.launch
Locally start SensorApp-Client.py

You many need to change the TCP_PORT and TCP_IP in both SensorApp.py and SensorApp-client.py

To find IP Address:
Windows: ipconfig
Mac: ifconfig

Improvements:
Visual diagram of what the sensor sees
A method of remotely calibrating the sensor.


# Outcomes
