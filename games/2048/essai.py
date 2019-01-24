## File: 2048_Game
# Author: Massimo ... , Michael Greub
# Date: 28.12.2018

# Importation des modules requis
from sense_hat import SenseHat
from random import randint
from time import *
from threading import Thread

sense=SenseHat()
sense.clear(0, 0, 0)
size = 4


#-----Définition des couleurs-----

black = (0, 0, 0)
blue_1 = (0, 255, 255)
green_2 = (0, 255, 127)
green_3 = (0, 255, 0)
green_4 = (127, 255, 0)
yellow_5 = (255, 255, 0)
orange_6 = (255, 127, 0)
red_7 = (255, 0, 0)
pink_8 = (255, 0, 127)
pink_9 = (255, 0, 255)
pink_10 = (127, 0, 255)
blue_11 = (0, 0, 255)
blue_12 = (0, 127, 255)
white_13 = (255, 255, 255)

colors = [black, blue_1, green_2, green_3, green_4, yellow_5, orange_6, red_7,\
          pink_8, pink_9, pink_10, blue_11, blue_12, white_13]

# ------Définition des matrices utilisées------


# ------Définition des matrices utilisées------


L4 = [[1, 2, 3, 4],
      [5, 4, 6, 7],
      [8, 9, 10, 11],
      [12, 13, 14, 15], 
     ]
L8 = [[L4[0][0], L4[0][0], L4[0][1], L4[0][1], L4[0][2], L4[0][2], L4[0][3], L4[0][3]],
      [L4[0][0], L4[0][0], L4[0][1], L4[0][1], L4[0][2], L4[0][2], L4[0][3], L4[0][3]],
      [L4[1][0], L4[1][0], L4[1][1], L4[1][1], L4[1][2], L4[1][2], L4[1][3], L4[1][3]],
      [L4[1][0], L4[1][0], L4[1][1], L4[1][1], L4[1][2], L4[1][2], L4[1][3], L4[1][3]],
      [L4[2][0], L4[1][0], L4[2][1], L4[2][1], L4[2][2], L4[2][2], L4[2][3], L4[2][3]],
      [L4[2][0], L4[2][0], L4[2][1], L4[2][1], L4[2][2], L4[2][2], L4[2][3], L4[2][3]],
      [L4[3][0], L4[3][0], L4[3][1], L4[3][1], L4[3][2], L4[3][2], L4[3][3], L4[3][3]],
      [L4[3][0], L4[3][0], L4[3][1], L4[3][1], L4[3][2], L4[3][2], L4[3][3], L4[3][3]]
     ]



