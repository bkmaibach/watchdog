#!/usr/bin/python3
import json, requests, time
import RPi.GPIO as GPIO
import pygame
import getopt
import sys

def trint(m):
        print(time.ctime())
        print(m)

address = '0xffd9d51341288bd7e41e689f516eda8ee8c23c08'
poolUrl = 'http://dwarfpool.com/eth/api?wallet=' + address + '&email=bmaibach@gmail.com'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

debug_mode = False
secondsInterval = 600
secondsElapsed = 0

trint("Sleeping " + str(secondsInterval))
time.sleep(secondsInterval)
secondsElapsed += secondsInterval

if sys.argv[1] == '0':
	secondsDuration = int(sys.maxsize)
else:
	secondsDuration = int(sys.argv[1])*3600

while(secondsElapsed < secondsDuration):
        #print("Fetching status...")
        resp = requests.get(url=poolUrl)
        #print("Parsing")
        data = json.loads(resp.text)
        error = data['error']
        workers = data['workers']
        rig1 = workers['rig1']
        alive = rig1['alive']
        hashrate = rig1['hashrate']
        second_since_submit = rig1['second_since_submit']
        #print("Status obtained...")
        if alive == False:
                trint("Crash detected...")
                if debug_mode == False:
                        print("Restarting...")
                        GPIO.output(12, True)
                        time.sleep(.5)
                        GPIO.output(12, False)
                        time.sleep(secondsInterval)
                        alive = True
                else:
                        print("Debug mode enabled, leaving restart switch alone...")
        time.sleep(secondsInterval)
        secondsElapsed += secondsInterval
        print("\n")
trint("Job finished! Good work.")
GPIO.cleanup()
