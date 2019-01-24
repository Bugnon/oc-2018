# File: 05_rotation.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
directions = (0, 90, 180, 270)

for dir in directions:
    sense.set_rotation(dir)
    sense.show_letter('F')
    sleep(0.5)
    sense.flip_h()
    sleep(1)

for dir in directions:
    sense.set_rotation(dir)
    s = 'dir='+str(dir)
    sense.show_message(s)
    
    