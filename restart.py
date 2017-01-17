#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
print (time.ctime())
print ("Restarting...")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, True)
time.sleep(.5)
GPIO.output(12, False)
