""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Adrien Dor

Insert Github repository link here.

https://github.com/usc-ee250-spring2021/lab02-adidor.git
"""
"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 3    # D3
    
    # Connect the Grove Rotary Angle Sensor to analog port A0
    # SIG,NC,VCC,GND
    potentiometer = 0
    grovepi.pinMode(potentiometer,"INPUT")

    # Max distance threshold set with rotary angle sensor
    maxT = 50
    
    

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        
        
        # Read angle  value from potentiometer
        threshold = grovepi.analogRead(potentiometer)
        
        time.sleep(0.15)
        print (threshold)
        print(grovepi.ultrasonicRead(PORT))
        
        #txt = "{:>4d}".format(threshold) + "cm  \n" + "{:>4d}".format(grovepi.ultrasonicRead(PORT)) + "cm"
        #setText_norefresh(txt) 
        # Compare if the threshold set by the rotary angle sensor is less than the
        # distance measured by the ultrasonic sensor
        if (grovepi.ultrasonicRead(PORT) < threshold):
            txt = "{:>4d}".format(threshold) + "cm OBJ Pres \n" + "{:>4d}".format(grovepi.ultrasonicRead(PORT)) + "cm"
            setText_norefresh(txt)
 
        else:
            txt = "{:>4d}".format(threshold) + "cm          \n" + "{:>4d}".format(grovepi.ultrasonicRead(PORT)) + "cm"
            setText_norefresh(txt)
