# File: 01_hello.py
# Author: Raphael Holzer
# Date: 26. 11. 2018
import random 
# from <module> import <object>
from sense_hat import SenseHat


# create a new SenseHat object
sense = SenseHat()

sense.set_rotation(90)
# infinite loop
while True:
    # use the method 'show_message'
    a=random.randint(0, 255)
    b=random.randint(0, 255)
    c=random.randint(0, 255)
    sense.show_message('Bonjour, je suis Mirko le boss!', scroll_speed = 0.05, text_colour =(a, b, c))
