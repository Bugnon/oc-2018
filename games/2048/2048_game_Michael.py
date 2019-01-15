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


L4 = [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0], 
     ]
L8 = [[0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0]
     ]

#----- Définitionts des fonctions-----
def control_end(e):
    end = True
    for x in range(e):
        for y in range(e):
            if L[x][y]==0:
                end=False
    for x in range(e-2):
        for y in range(e-2):
            x=x+1
            y=y+1
            if L[x][y]==L[x+1][y+1]:
                end = False
            elif L[x][y]==L[x+1][y-1]:
                end = False
            elif L[x][y]==L[x-1][y+1]:
                end = False
            elif L[x][y]==L[x-1][y-1]:
                end = False
    if e==8:
        pass
                                                                         
            
            
            

<<<<<<< HEAD
=======
def startup():
    sense.clear()
    sense.show_message('Choose your mode:',0.075)
    sleep(0.2)
    

def set_pixels(a):
    if a==8:
        for x in range(4):
           for y in range(4):
              sense.set_pixel(x, y, colors[L[x][y]])
   elif a==4:
        
>>>>>>> 3e290848daf26f4cc7ec427e202bcaa5d46b87d6


#def set_pixels(a):
#    if a==8:
#        for x in range(4):
#           for y in range(4):
#              sense.set_pixel(x, y, colors[L[x][y]])
#   elif a==4:
        

def new_block(e):
    i=0
    for x in range(e):
        for y in range(e):
            if L[x][y]==0:
                i=i+1
    if i>1:
        r=0
        while r<2: #tant qu'on en a pas créé 2
            x=randint(0, (e-1))# 
            y=randint(0, (e-1))
            print(x,y)# On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y]=1 # On défini un bloc de couleur correspondant au chiffre 2
                r=r+1# Si le bloc est créé on indente pour créé exactement 2 nouveaux pixels
    elif i==1:
        r=0
        while r < 1: #tant qu'on en a pas créé 2
            x=randint(0, (e-1))# 
            y=randint(0, (e-1))# On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y]=1 # On défini un bloc de couleur correspondant au chiffre 2
                r=r+1
    set_pixels(e)
    print(L)

def startup():
    global size
    sense.clear()
    sense.show_message('Choose your mode:',0.15)
    sleep(0.2)
    run=True
    while run:
        size = 4
        sense.show_message('4X4', 0.1)
        sleep(0.1)
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                run= False
        if run == True:
            size = 8
            sense.show_message('8X8', 0.1)
            sleep(0.1)
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    run= False
    new_block(size) 

def moved_up(d):
  for y in range(d): 
    for x in range(d):# Sur chaque pixel en prenantles pixels en ligne puis en colonne
        if L[x][y] > 0 and y>=1:# On controle que le pixel ne soit pas une case vide
          while L[x][y-1] == 0 and y>=1:# Si la case est vide 
              L[x][y-1]=L[x][y]
              L[x][y]=0
              y=y-1
          if L[x][y-1]==L[x][y]:
             L[x][y-1]=L[x][y-1]+1
             L[x][y]=0
  new_block(d)
  
  
def moved_down(b):
    for z in range(b-1):
        for x in range(b):
            y=b-2-z
            if L[x][y] > 0 and y<=(b-2):# On controle que le pixel ne soit pas une case vide
                while y<=(b-2) and L[x][y+1] == 0:# Si la case est vide
                   L[x][y+1]=L[x][y]
                   L[x][y]=0
                   y=y+1
                if y<(b-1):
                    if L[x][y+1]==L[x][y]:
                       L[x][y+1]=L[x][y+1]+1
                       L[x][y]=0
    new_block(b)
    
   
def moved_left(c):
    for x in range(c):
        for y in range(c):
            if L[x][y] > 0:# On controle que le pixel ne soit pas une case vide
                while x>0 and L[x-1][y] == 0:# Si la case est vide 
                    L[x-1][y]=L[x][y]
                    L[x][y]=0
                    x=x-1
                if L[x-1][y]==L[x][y]:
                   L[x-1][y]=L[x-1][y]+1
                   L[x][y]=0
    new_block(c)

def moved_right(a):
    if a == 4:
        L = L4
    elif a == 8:
        L = L8
    for z in range(a-1):
        x=a-2-z
        for y in range(a):
            if L[x][y] > 0:# On controle que le pixel ne soit pas une case vide
                while x<(a-1) and L[x+1][y] == 0:# Si la case est vide 
                    L[x+1][y]=L[x][y]
                    L[x][y]=0
                    x=x+1
                if L[x+1][y]==L[x][y]:
                   L[x+1][y]=L[x+1][y]+1
                   L[x][y]=0
    new_block(a)
            

    




#-----Reactions du joystick-----
running= True

while running:
  for event in sense.stick.get_events():
      if event.action == 'pressed':
          if event.direction == 'up':
              moved_up(size)
          elif event.direction == 'down':
              moved_down(size)
          elif event.direction == 'right':
              moved_right(size)
          elif event.direction == 'left':
              moved_left(size)
          elif event.direction == 'middle':
              pass
