# File: 02_hi.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat
from time import sleep

# create a new SenseHat object
sense = SenseHat()

sense.set_rotation(180)

blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)

sense.show_letter('H', text_colour=blue, back_colour=white)
sleep(0.5)
sense.show_letter('i', text_colour=white, back_colour=red)
sleep(0.5)

# clear the LED display
sense.clear()