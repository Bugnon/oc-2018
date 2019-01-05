## File: 2048_Game
# Author: Massimo ... , Michael Greub
# Date: 28.12.2018

# Importation des modules requis
from sense_hat import SenseHat
from random import randint

sense=SenseHat()

#-----Définition des fonctions-----

def collision(pixel):# Définition redondante de la fonction permettant de monter en couleur (chiffre)
    pixelup = (0, 0, 0)
    if pixel == (0, 252, 248): # 2
        pixelup = (0, 252, 124) # 4
    elif pixel == (0, 252, 124): # 4
        pixelup = (0, 252, 0) # 8
    elif pixel == (0, 252, 0): # 8
        pixelup = (124, 252, 0) # 16
    elif pixel == (124, 252, 0): # 16
        pixelup = (248, 252, 0) # 32
    elif pixel == (248, 252, 0): # 32
        pixelup = (248, 126, 0) # 64
    elif pixel == (248, 126, 0): # 64
        pixelup = (248, 0, 0) # 128
    elif pixel == (248, 0, 0): # 128
        pixelup = (248, 0, 124) # 256
    elif pixel == (248, 0, 124): # 256
        pixelup = (248, 0, 248) # 512
    elif pixel == (248, 0, 248): # 512
        pixelup = (124, 0, 248) # 1024
    elif pixel == (124, 0, 248): # 1024
        pixelup = (0, 0, 248) # 2048
    elif pixel == (0, 0, 248): # 2048
        pixelup = (0, 126, 248) # 4096
    elif pixel == (0, 126, 248): # 4096
        pixelup = (248, 252, 248) # 8192
    elif pixel == (248, 252, 248): # 8192
        victory
    return pixelup
    
    
    
def new_block():
  i=0
  while i < 2: #tant qu'on en a pas créé 2
    x=randint(0, 7)# 
    y=randint(0, 7)# On choisis aléatoirement une ligne et une colonne
    if sense.get_pixel(x, y) == [0, 0, 0]:# On controle si ce pixel est vide
      start = (0, 255, 248)
      sense.set_pixel(x, y, start) # On défini un bloc de couleur correspondant au chiffre 2
      i=i+1 # Si le bloc est créé on indente pour créé exactement 2 nouveaux pixels

def moved_up():
  for y in range(8): 
    for x in range(8): # Sur chaque pixel en prenantles pixels en ligne puis en colonne
      if sense.get_pixel(x, y) != (0, 0, 0) and y > 0: # On controle que le pixel ne soit pas une case vide
          while sense.get_pixel(x, y-1) == (0, 0, 0): # Si la case est vide 
              pixel=sense.get_pixel(x, y)
              sense.set_pixel(x, y-1, pixel)
              sense.set_pixel(x, y, 0, 0, 0)
          else:
              pixel_to_upgrade = sense.get_pixel(x, y-1)
              pixel_upgraded = collision(pixel_to_upgrade)
              sense.set_pixel(x, y, 0, 0, 0)
              sense.set_pixel(x, y-1, pixel_upgraded)
  new_block()


#-----Reactions du joystick-----             
 def pushed_up(event):
    if event.action != ACTION_RELEASED:
        moved_up()

def pushed_down(event):
    if event.action != ACTION_RELEASED:
        moved_down()
        
def pushed_left(event):
    if event.action != ACTION_RELEASED:
        moved_left()

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        moved_right()
        
while True:
  sense.stick.direction_up = pushed_up
  sense.stick.direction_down = pushed_down
  sense.stick.direction_left = pushed_left
  sense.stick.direction_right = pushed_right