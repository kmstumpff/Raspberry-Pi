import os
import time

def getTemp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

go_on = 1
os.system('clear')

while True:

    CPU_Temp = getTemp()
    print ("CPU tempurature: " + CPU_Temp)
    time.sleep(1)
    os.system('clear')
