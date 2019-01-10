# File: Démineur
# Author: Fabian Roulin
# Date: 8.01.2019

from sense_hat import SenseHat
#On importe le module random
from random import randint, choice

from time import sleep, time

#On définit les couleurs
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
white = (255, 255, 255)
black = (0, 0, 0)

sense = SenseHat()
sense.set_rotation(180)

sense.clear()

List_Bomb = []
i=0
while i < 5 :
    x = randint(0, 7)
    y = randint(0, 7)
    q=0
    print(len(List_Bomb))
    while q < (len(List_Bomb)):
        if([x, y] == List_Bomb[q]):
            i = i - 1
            q = q + 1
        else:
            q = q + 1
        
        
    List_Bomb.append([x, y])
    i = i+1
    
print(List_Bomb)


for j in range(len(List_Bomb)):
    a = List_Bomb[j][0]
    b = List_Bomb[j][1]
    sense.set_pixel(a, b, red)
