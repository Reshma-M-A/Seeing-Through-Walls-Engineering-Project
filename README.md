# Seeing-Through-Walls-Engineering-Project
This is an honours project. 

# Purpose
This project will develop an innovative solution for first responders  to  plan  their  evacuation  assistance  at  the scene  of  an  emergency,  e.g.,  fire  and  earthquakes. Knowingthe distribution of people inside buildings can help first respondersin defining their evacuation plan. 

The  basic  idea  of  this  project  is utilisingthe  recent technology   improvements   of   wireless   sensing   that allows for tracking people through walls and occlusions. The team will also explore the use of robots and drones fordefining the best evacuation path.
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
