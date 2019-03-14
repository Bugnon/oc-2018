# File: 01_hello.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat
import random

# create a new SenseHat object
sense = SenseHat()
sense.set_rotation(180)


red = (255, 0, 0)
green = (0 , 255, 0)
blue = (0, 0, 255)

# infinite loop
while True:
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # use the method 'show_message'
    sense.show_message('Bonjour, ici la Terre!', text_colour=colour, scroll_speed = 0.02)
