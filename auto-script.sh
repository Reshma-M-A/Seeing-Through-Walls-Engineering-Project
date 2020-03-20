#!/bin/bash
while true; do
  python SensorApp-Server.py
  echo SensorApp-Server is running
  sleep 5
  python SensorApp-Client.py
  echo SensorApp-Client is running
  sleep 5
done