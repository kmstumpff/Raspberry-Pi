import RPi.GPIO as GPIO
import os

#use P1 header pin numbering convention
GPIO.setmode(GPIO.BCM)

#remove warnings
#GPIO.setwarnings(False) 

# Set up the GPIO channels
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


os.system('clear')

io = 0
o_o = 0

while True:
	
	io = input('Enter the GPIO number or -1 to exit: ')
	if io == -1:
		break
	while True:
		os.system('clear')
		o_o=input('Turn On/Off (1/0) or exit (-1)? ')
		if  o_o == 1:
			GPIO.output(io, GPIO.HIGH)
		elif o_o == 0:
		       GPIO.output(io, GPIO.LOW)
		else:
			GPIO.output(io, GPIO.LOW)
			os.system('clear')
			break


os.system('clear')
#GPIO.cleanup()
