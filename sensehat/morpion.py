from sense_hat import SenseHat

from time import sleep, time

sense = SenseHat()
sense.set_rotation(180)

##tableau
sense.clear()
for x in range(0, 8, 2):
    for y in range(8):
        sense.set_pixel(x, y, green)
        sleep(0.1)
        