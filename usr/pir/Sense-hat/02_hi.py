# File: 02_hi.py
# Author: Raphael Holzer
# Date: 26. 11. 2018
import random
# from <module> import <object>
from sense_hat import SenseHat
from time import sleep

# create a new SenseHat object
sense = SenseHat()
a=random.randint(0, 255)
b=random.randint(0, 255)
c=random.randint(0, 255)

sense.show_letter('H', text_colour=(a, b, c), back_colour=(255, 255, 255))
sleep(0.5)
sense.show_letter('i')
sleep(0.5)

# clear the LED display
sense.clear()