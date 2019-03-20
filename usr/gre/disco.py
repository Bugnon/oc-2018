from time import *
from gamelib import *
from sense_hat import SenseHat
import random
i = 0
sense = SenseHat()

while True:
    colors = [LEMON, PINK, RED, MINT, BLUE, GREEN, MAGENTA, CYAN, YELLOW, ORANGE, GRAY, CORAIL, BORDEAU, LIME]
    for x in range(8):
        for y in range(8):
            i = random.randint(0, 13)
            sense.set_pixel(x, y, colors[i])
    sleep(0.1)