# File: 2048_Game
# Author: Massimo ... , Michael Greub
# Date: 28.12.2018

# Importation des modules requis
from sense_hat import SenseHat
from random import randint

s=SenseHat()
#-----Définition des fonctions-----

def new_block():
  while i < 2:
    x=randint(0, 7)
    y=randint(0, 7)
   if s.get_pixel(x, y) == [0, 0, 0]:
     x.setpixel(x, y, 255, 0, 0)
     i=i+1



#-----Reactions du joystick-----
while True:
  s.stick.direction_up = move_up
  s.stick.direction_down = move_down
  s.stick.direction_right = move_right
  s.stick.direction_left = move_left