# File: 03_rgb.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat
from random import randint

sense = SenseHat()
red=(255, 0, 0)
msg = 'Bonjour, ici la Terre!'
while 0==0 is True:
  r=randint(0, 255)
  g=randint(0, 255)
  b=randint(0, 255)
  color=(r, g, b)
  sense.show_message(msg, text_colour=color, back_colour=red)
  sense.clear()