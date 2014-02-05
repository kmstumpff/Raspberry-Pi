import RPi.GPIO as GPIO
import os
import time

on = 1
off = 0


# use P1 header pin numbering convention
GPIO.setmode(GPIO.BCM)

#remove warnings
GPIO.setwarnings(False) 

# Set up the GPIO channels
GPIO.setup(24, GPIO.OUT)
#GPIO.setup(27, GPIO.OUT)

while True:
	GPIO.output(24, GPIO.HIGH)
#	GPIO.output(27, GPIO.LOW)
	time.sleep(.01)
	GPIO.output(24, GPIO.LOW)
#	GPIO.output(27, GPIO.HIGH)
	time.sleep(.01)
	
GPIO.cleanup()
