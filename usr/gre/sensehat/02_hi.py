# File: 02_hi.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat
from time import sleep

# create a new SenseHat object
sense = SenseHat()

<<<<<<< HEAD
blue = (0, 0, 255)
red = (30,30,30)
while True:
    sense.show_letter('P', text_colour=blue, back_colour = red)
    sleep(0.75)
    sense.show_letter('i', text_colour= blue, back_colour= red)
    sleep(0.75)


# clear the LED display
sense.clear()
=======
sense.show_letter('H')
sleep(0.5)
sense.show_letter('i')
sleep(0.5)

# clear the LED display
sense.clear()
>>>>>>> refs/remotes/origin/master
