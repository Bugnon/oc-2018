# File: 01_hello.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat

# create a new SenseHat object
sense = SenseHat()
sense.set_rotation(180)
# infinite loop
while True:
    c = [225, 0, 0]
    # use the method 'show_message'
    sense.show_message("HELLO", scroll_speed = 0.1, text_colour=c)
