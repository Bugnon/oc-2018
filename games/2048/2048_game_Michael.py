## File: 2048_Game
# Author: Massimo ... , Michael Greub
# Date: 28
.12.2018

# Importation des modules requis
from sense_hat import SenseHat
from random import randint
from time import *

sense=SenseHat()
sense.clear(0, 0, 0)


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

L = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0], 
     ]

#----- Définitionts des fonctions-----

def set_pixels():
    for x in range(4):
        for y in range(4):
            sense.set_pixel(x, y, colors[L[x][y]])

def new_block():
    i=0
    for x in range(4):
        for y in range(4):
            if L[x][y]==0:
                i=i+1
    if i>1:
        r=0
        while r<2: #tant qu'on en a pas créé 2
            x=randint(0, 3)# 
            y=randint(0, 3)
            print(x,y)# On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y]=1 # On défini un bloc de couleur correspondant au chiffre 2
                r=r+1# Si le bloc est créé on indente pour créé exactement 2 nouveaux pixels
    elif i==1:
        r=0
        while r < 1: #tant qu'on en a pas créé 2
            x=randint(0, 3)# 
            y=randint(0, 3)# On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y]=1 # On défini un bloc de couleur correspondant au chiffre 2
                r=r+1
    set_pixels()
    print(L)

def moved_up():
  for y in range(4): 
    for x in range(4):# Sur chaque pixel en prenantles pixels en ligne puis en colonne
        if L[x][y] > 0 and y>=1:# On controle que le pixel ne soit pas une case vide
          while L[x][y-1] == 0 and y>=1:# Si la case est vide 
              L[x][y-1]=L[x][y]
              L[x][y]=0
              y=y-1
          if L[x][y-1]==L[x][y]:
             L[x][y-1]=L[x][y-1]+1
             L[x][y]=0
  new_block()
  
  
def moved_down():
    for z in range(3):
        for x in range(4):
            y=2-z
            if L[x][y] > 0 and y<=2:# On controle que le pixel ne soit pas une case vide
                while y<=2 and L[x][y+1] == 0:# Si la case est vide
                   L[x][y+1]=L[x][y]
                   L[x][y]=0
                   y=y+1
                if y<3:
                    if L[x][y+1]==L[x][y]:
                       L[x][y+1]=L[x][y+1]+1
                       L[x][y]=0
    new_block()
    
   
def moved_left():
    for x in range(4):
        for y in range(4):
            if L[x][y] > 0:# On controle que le pixel ne soit pas une case vide
                while x>0 and L[x-1][y] == 0:# Si la case est vide 
                    L[x-1][y]=L[x][y]
                    L[x][y]=0
                    x=x-1
                if L[x-1][y]==L[x][y]:
                   L[x-1][y]=L[x-1][y]+1
                   L[x][y]=0
    new_block()

def moved_right():
    for z in range(3):
        x=2-z
        for y in range(4):
            if L[x][y] > 0:# On controle que le pixel ne soit pas une case vide
                while x<3 and L[x+1][y] == 0:# Si la case est vide 
                    L[x+1][y]=L[x][y]
                    L[x][y]=0
                    x=x+1
                if L[x+1][y]==L[x][y]:
                   L[x+1][y]=L[x+1][y]+1
                   L[x][y]=0
    new_block()
            

    
#    
#def new_block():
#  i=0
#  while i < 2: #tant qu'on en a pas créé 2
#    x=randint(0, 7)# 
#    y=randint(0, 7)# On choisis aléatoirement une ligne et une colonne
#    if sense.get_pixel(x, y) == [0, 0, 0]:# On controle si ce pixel est vide
#      start = (0, 255, 248)
#      sense.set_pixel(x, y, start) # On défini un bloc de couleur correspondant au chiffre 2
#      i=i+1 # Si le bloc est créé on indente pour créé exactement 2 nouveaux pixels
#
#def moved_up():
#  for y in range(8): 
#    for x in range(8): # Sur chaque pixel en prenantles pixels en ligne puis en colonne
#      if sense.get_pixel(x, y) != (0, 0, 0) and y > 1:# On controle que le pixel ne soit pas une case vide
#          global z
#          z = y
#          while sense.get_pixel(x, z-1) == [0, 0, 0] and z>1:# Si la case est vide 
#              pixel=sense.get_pixel(x, z)
#              sense.set_pixel(x, z-1, pixel)
#              sense.set_pixel(x, z, 0, 0, 0)
#              z=z-1
#          if y != 0 :
#              pixel_to_upgrade = sense.get_pixel(x, y-1)
#              pixel_upgraded = collision(pixel_to_upgrade)
#              sense.set_pixel(x, y, 0, 0, 0)
#              sense.set_pixel(x, y-1, pixel_upgraded)
#  new_block()
#def moved_down():
#    pass
#  
#
new_block()

#-----Reactions du joystick-----
running= True

while running:
  for event in sense.stick.get_events():
      if event.action == 'pressed':
          if event.direction == 'up':
              moved_up()
          elif event.direction == 'down':
              moved_down()
          elif event.direction == 'right':
              moved_right()
          elif event.direction == 'left':
              moved_left()
          elif event.direction == 'middle':
              pass