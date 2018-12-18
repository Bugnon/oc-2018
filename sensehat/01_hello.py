# File: 01_hello.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat

# create a new SenseHat object
sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)

# infinite loop
while True:
    # use the method 'show_message'
    sense.show_message('Bonjour, ici la Terre!', scroll_speed = 0.1, text_colour = red)
