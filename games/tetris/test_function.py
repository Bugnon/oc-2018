from sense_hat import SenseHat
from time import sleep
from random import randint, choice

sense = SenseHat()
sense.clear()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
white = (255, 255, 255)
black = (0, 0, 0)

colors = (red, magenta, blue, cyan, green, yellow, white, orange)

### FORMES ###

## Le carré en jaune
def O (x, y):
    sense.set_pixel(x, y, yellow)
    sense.set_pixel(x-1, y, yellow)
    sense.set_pixel(x, y-1, yellow)
    sense.set_pixel(x-1, y-1, yellow)

## La barre en cyan
def I (x, y):
    sense.set_pixel(x, y, cyan)
    sense.set_pixel(x-1, y, cyan)
    sense.set_pixel(x-2, y, cyan)
    sense.set_pixel(x-3, y, cyan)

## Le T en violet
def T (x, y):
    sense.set_pixel(x, y, magenta)
    sense.set_pixel(x-1, y, magenta)
    sense.set_pixel(x-2, y, magenta)
    sense.set_pixel(x-1, y-1, magenta)
    
## Le L en orange
def L (x, y):
    sense.set_pixel(x, y, orange)
    sense.set_pixel(x, y-1, orange)
    sense.set_pixel(x, y-2, orange)
    sense.set_pixel(x-1, y-2, orange)
    
## Le J en bleu
def T (x, y):
    sense.set_pixel(x, y, blue)
    sense.set_pixel(x-1, y, blue)
    sense.set_pixel(x-2, y, blue)
    sense.set_pixel(x-2, y-1, blue)

## Le Z en rouge
def Z (x, y):
    sense.set_pixel(x, y, red)
    sense.set_pixel(x-1, y, red)
    sense.set_pixel(x-1, y-1, red)
    sense.set_pixel(x-2, y-1, red)
    
## Le S en vert
def S (x, y):
    sense.set_pixel(x, y, green)
    sense.set_pixel(x-1, y, green)
    sense.set_pixel(x, y-1, green)
    sense.set_pixel(x+1, y-1, green)

forms = [O (4, 4), I (4, 4), T (4, 4), L (4, 4), T (4, 4), Z (4, 4), S (4, 4)]

while True:
    choice(forms)
    sleep(1)
    sense.clear()
        
        