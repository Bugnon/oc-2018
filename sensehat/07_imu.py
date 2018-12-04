# File: 07_imu.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.set_imu_config(False, True, False) # gyroscope only

while True:
    orientation = sense.get_orientation_degrees()
    print(orientation)
    sleep(1)
    

