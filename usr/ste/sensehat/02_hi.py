# File: 02_hi.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat
from time import sleep

# create a new SenseHat object
sense = SenseHat()

sense.show_letter('H')
sleep(0.5)
sense.show_letter('i')
sleep(0.5)

# clear the LED display
sense.clear()