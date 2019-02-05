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
def I1 (x, y):
    sense.clear()
    sense.set_pixel(x, y, cyan)
    sense.set_pixel(x-1, y, cyan)
    sense.set_pixel(x-2, y, cyan)
def I2 (x, y):
    sense.clear()
    sense.set_pixel(x, y, cyan)
    sense.set_pixel(x-1, y, cyan)
    sense.set_pixel(x+1, y, cyan)

## Le T en violet
def T1 (x, y):
    sense.clear()
    sense.set_pixel(x, y, magenta)
    sense.set_pixel(x-1, y, magenta)
    sense.set_pixel(x, y-1, magenta)
def T2 (x, y):
    sense.clear()
    sense.set_pixel(x-1, y-1, magenta)
    sense.set_pixel(x-1, y, magenta)
    sense.set_pixel(x, y-1, magenta)
def T3 (x, y):
    sense.clear()
    sense.set_pixel(x, y, magenta)
    sense.set_pixel(x-1, y, magenta)
    sense.set_pixel(x-1, y-1, magenta)
    
##shapes = [S(4, 7), Z(4, 7), J(4, 7), L(4, 7), T1(4, 7), O(4, 7)]
##functions = [S, Z, J, L, T1, O]

### JOYSTICK ###
    
while True:
    for event in sense.stick.get_events():
         if event.action == 'pressed' and event.direction == 'middle':
            print('Tourne')
         elif event.direction == 'up' and event.action == 'pressed':
            print('Rien')
         elif event.direction == 'down' and event.action == 'held':
            print('Descend')
         elif event.direction == 'left' and event.action == 'pressed':
            print('Gauche')
         elif event.direction == 'right' and event.action == 'pressed':
            print('Droite')
        