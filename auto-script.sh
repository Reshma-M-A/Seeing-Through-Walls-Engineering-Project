#!/bin/bash
while true; do
  python SensorApp.py
  sleep 5
  python SensorApp-Server.py
  sleep 5
done