# File: 03_rgb.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

sense.set_rotation(180)


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

colors = (red, magenta, blue, cyan, green, yellow)
msg = 'Bonjour, ici la Terre!'

# cycle through the colours in the 'colors' list
for col in colors :
    sense.clear(col)
    sleep(1)

sense.show_message(msg, text_colour=cyan, back_colour=red)
sense.clear()