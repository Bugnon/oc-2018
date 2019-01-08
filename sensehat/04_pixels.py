# File: 04_pixels.py
# Author: Raphael Holzer
# Date: 26. 11. 2018

# from <module> import <object>
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

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

x = 0
y = 0

# cycle through the colours in the 'colors' list
sense.clear()
sense.set_pixel(x, y, red)

(x, y) = (2, 3) #on affiche le pixel colonne 2 ligne 3
sense.set_pixel(x, y, blue)
sleep(1)

for x in range(8):
    for y in range(8):
        sense.set_pixel(x, y, blue)
        sleep(0.02)
        
sleep(1)

o = green
x = black
creeper = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, x, x, o, o, x, x, o,
    o, x, x, o, o, x, x, o,
    o, o, o, x, x, o, o, o,
    o, o, x, x, x, x, o, o,
    o, o, x, x, x, x, o, o,
    o, o, x, o, o, x, o, o] #remplace o par la couleur verte et x par noir

sense.set_pixels(creeper)
sleep(2)

b = (255, 255, 255)
r = (255, 0, 0)
o = (255, 127, 0)
j = (255, 255, 0)
v = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
m = (159, 0, 255)
n = (0, 0, 0)

image = [
    n,n,n,n,n,n,n,n,
    n,n,n,r,r,n,n,n,
    n,r,r,o,o,r,r,n,
    r,o,o,j,j,o,o,r,
    o,j,j,v,v,j,j,o,
    j,v,v,b,b,v,v,j,
    b,b,b,i,i,b,b,b,
    b,i,i,m,m,i,i,b
    ]

sense.set_pixels(image)
