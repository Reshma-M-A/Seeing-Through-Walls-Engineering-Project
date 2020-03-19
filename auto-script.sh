#!/bin/bash
while true; do
  python SensorApp.py
  echo SensorApp-Client is running
  sleep 5
  python SensorApp.py
  echo SensorApp-Server is running
  sleep 5
done