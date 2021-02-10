""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Adrien Dor

Insert Github repository link here.
"""
git@github.com:usc-ee250-spring2021/lab02-adidor.git

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
import grove_rgb_lcd

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 3    # D3
    
    # Connect the Grove Rotary Angle Sensor to analog port A0
    # SIG,NC,VCC,GND
    potentiometer = 0
    grovepi.pinMode(potentiometer,"INPUT")

    # Maximum distance threshold to be set with rotary angle sensor
    maxThreshold = 50
    
    # Set RGB
    setRGB(121, 19, 210)

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        
        
        # Read angle  value from potentiometer
        sensor_value = grovepi.analogRead(potentiometer)
        setThreshold = int(sensor_value*maxThreshold/1024)
        
        time.sleep(0.1)
        print (setThreshold)
        print(grovepi.ultrasonicRead(PORT))
        
        # Compare if the threshold set by the rotary angle sensor is less than the
        # distance measured by the ultrasonic sensor
        if (grovepi.ultrasonicRead(PORT) < setThreshold):
            lcdText = "{:>3d}".format(setThreshold) + "cm OBJ Pres  \n" + "{:>3d}".format(grovepi.ultrasonicRead(PORT)) + "cm"
            setText_norefresh(lcdText)
            setRGB(189, 83, 72)
        else:
            lcdText = "{:>3d}".format(setThreshold) + "cm           \n" + "{:>3d}".format(grovepi.ultrasonicRead(PORT)) + "cm"
            setText_norefresh(lcdText)
            setRGB(143, 189, 119)
