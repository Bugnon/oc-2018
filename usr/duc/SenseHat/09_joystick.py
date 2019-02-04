# File: 09_joystick.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        print(event)