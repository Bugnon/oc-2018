# File: 06_environment.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

red = (255, 0, 0)
blue = (0, 0, 255)

h = sense.get_humidity()
t = sense.get_temperature()
p = sense.get_pressure()

print('humidity =', h)
print('pressure =', p)
print('temperature =', t)
print('temp from pressure =', sense.get_temperature_from_pressure())
print('temp from humidity =', sense.get_temperature_from_humidity())

while True:
    h = sense.get_humidity()
    t = sense.get_temperature()
    p = sense.get_pressure()
    sense.show_message('t='+str(t), text_colour=red)
    sense.show_message('p='+str(p))
    sense.show_message('h='+str(h), text_colour=blue)
