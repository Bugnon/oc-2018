# File: 08_compas.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    raw = sense.get_compass_raw()
#    print(raw)
    print('x: {x}, y: {y}, z: {z}'.format(**raw))
    sleep(1)