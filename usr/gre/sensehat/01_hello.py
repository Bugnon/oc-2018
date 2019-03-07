# File: 01_hello.py
# Author: Raphael Holzer
# Date: 26. 11. 2018
<<<<<<< HEAD
import random
=======

>>>>>>> refs/remotes/origin/master
# from <module> import <object>
from sense_hat import SenseHat

# create a new SenseHat object
sense = SenseHat()

# infinite loop
while True:
    # use the method 'show_message'
<<<<<<< HEAD
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    sense.show_message('Hello world!',text_colour = (a, b, c), scroll_speed = 0.075)
=======
    sense.show_message('Bonjour, ici la Terre!', scroll_speed = 0.1)
>>>>>>> refs/remotes/origin/master
