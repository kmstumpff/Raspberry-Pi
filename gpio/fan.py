import RPi.GPIO as GPIO
import os

def getCPUtemp():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

on = 1
off = 0
power = off


# use P1 header pin numbering convention
GPIO.setmode(GPIO.BCM)

#remove warnings
#GPIO.setwarnings(False) 

# Set up the GPIO channels
GPIO.setup(25, GPIO.OUT)  # +5V
GPIO.setup(24, GPIO.OUT)  # LED

# os.system('clear')

while on != off:
	os.system('clear')
	CPU_Temp = getCPUtemp()
	if power == on:
	        print "The fan is on."
	else:
	        print "The fan is off"
	print ("CPU Tempurature: " + CPU_Temp)
	power=input('Turn fan on (1), off (0), or exit (-1)?')
	if power == -1:
		break
	elif power == on:
#		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
	elif power == off:
#		GPIO.output(25, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
os.system('clear')
GPIO.cleanup()
