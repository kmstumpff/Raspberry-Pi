import RPi.GPIO as GPIO
import os
from pprint import pprint

number = 0

# use P1 header pin numbering convention
GPIO.setmode(GPIO.BCM)

#remove warnings
#GPIO.setwarnings(False) 

# Set up the GPIO channels
GPIO.setup(2, GPIO.OUT)  #1
GPIO.setup(3, GPIO.OUT)  #2
GPIO.setup(17, GPIO.OUT)  #3
GPIO.setup(27, GPIO.OUT)  #4
GPIO.setup(22, GPIO.OUT)  #5
GPIO.setup(10, GPIO.OUT)  #6
GPIO.setup(9, GPIO.OUT)  #7

def clearNumber():
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(9, GPIO.LOW)

def displayNumber(na):
#	print('displayNumber')
	clearNumber()
	if na[1] == 1:
		GPIO.output(2, GPIO.HIGH)
	if na[2] == 1:
		GPIO.output(3, GPIO.HIGH)
	if na[3] == 1:
		GPIO.output(17, GPIO.HIGH)
	if na[4] == 1:
		GPIO.output(27, GPIO.HIGH)
	if na[5] == 1:
		GPIO.output(22, GPIO.HIGH)
	if na[6] == 1:
		GPIO.output(10, GPIO.HIGH)
	if na[7] == 1:
		GPIO.output(9, GPIO.HIGH)


def setNumber(number):
#	print('setNumber')
	na = [0,0,0,0,0,0,0,0]
	if number == 1:
#		print('1')
		na = [0,0,1,1,0,0,0,0]	
	if number == 2:
		na = [0,1,1,0,1,1,0,1]
	if number == 3:
		na = [0,1,1,1,1,0,0,1]
	if number == 4:
		na = [0,0,1,1,0,0,1,1]
	if number == 5:
		na = [0,1,0,1,1,0,1,1]
	if number == 6:
		na = [0,1,0,1,1,1,1,1]
	if number == 7:
		na = [0,1,1,1,0,0,0,0]
	if number == 8:
		na = [0,1,1,1,1,1,1,1]
	if number == 9:
		na = [0,1,1,1,0,0,1,1]
	if number == 0:
		na = [0,1,1,1,1,1,1,0]
	displayNumber(na)



GPIO.output(9, GPIO.HIGH)
clearNumber()
#na = [0,0,0,0,0,0,0,0]
while True:
	os.system('clear')
	print('Displaying ' + str(number))
	number=input('Enter a number 0-9. Enter -1 to exit:')
	if number == -1:
		clearNumber()
		break
	else:
		setNumber(number)
		

os.system('clear')
#GPIO.cleanup()
