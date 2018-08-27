#!/usr/bin/python
 
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("No water detected")
    else:
        print("Water detected")
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #lets us know when the pin goes high or low
GPIO.add_event_callback(channel, callback) #assign function to GPIO PIN, run function on change

#Infinite loop
while True:
    time.sleep(1)
