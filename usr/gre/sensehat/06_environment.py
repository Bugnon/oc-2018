# File: 06_environment.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

from sense_hat import SenseHat
<<<<<<< HEAD
from time import sleep
=======
>>>>>>> refs/remotes/origin/master

sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)

<<<<<<< HEAD
while True:
    h = int(sense.get_humidity())
    t = int(sense.get_temperature())
    p = int(sense.get_pressure())
    sense.show_message('t='+str(t), text_colour=red)
    sense.show_message('p='+str(p))
    sense.show_message('h='+str(h), text_colour=blue)

    while True:
        print('>>> New values <<< \n \n humidity =', h)
        print('pressure =', p)
        print('temperature =', t)
        print('temp from pressure =', sense.get_temperature_from_pressure())
        print('temp from humidity =', sense.get_temperature_from_humidity(),'\n ---------------------\n')
        sleep(20)
=======
h = int(sense.get_humidity())
t = int(sense.get_temperature())
p = int(sense.get_pressure())

print('humidity =', h)
print('pressure =', p)
print('temperature =', t)
print('temp from pressure =', sense.get_temperature_from_pressure())
print('temp from humidity =', sense.get_temperature_from_humidity())

while True:
    sense.show_message('t='+str(t), text_colour=red)
    sense.show_message('p='+str(p))
    sense.show_message('h='+str(h), text_colour=blue)
>>>>>>> refs/remotes/origin/master
