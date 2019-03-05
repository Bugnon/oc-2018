# File: Démineur
# Author: Fabian Roulin et Mirko Pirona
# Date: 8.01.2019

#Il manque :animation explode, win, lose, fontion qui compte de nombre de bombs around

# On importe le module Sensehat
from sense_hat import SenseHat

# On importe la librairie pygame
import pygame
from pygame.locals import *

# On importe le module random
from random import randint, choice

#On importe le module time
from time import sleep, time

#On définit nos couleurs :

green = (0, 255, 0)       #Drapeau
grey = (90,94,107)        #Case non-découverte
white = (255, 255, 255)   #Case vide = 0 bombe
yellow = (247, 255, 60)   #1 bombe à proximité
orange = (255, 127, 0)    #2 bombes à proximité
corail = (231, 62, 1)     #3 bombes à proximité
red = (248, 0, 0)         #4 bombes à proximité
bordeau = (91, 60, 19)    #5 bombe à proximité
black = (0, 0, 0)         #Bombe

# On lance pygame :
pygame.init()
pygame.display.set_mode((90,5)) # Correspond à une petite fenêtre

# On lance sense hat :
sense = SenseHat()
sense.clear()

# On initialise les variables globals:

# On crée la variable qui contiendra les bombes :
List_bomb = []

list_checked = []

nb_bombs = 12
# On crée les variables de déplacement :
game = True
running = True
x = 0
y = 0

old_color = grey


# Définition des fonctions du programme :

# Fonction qui compte le nombre de bombes à proximité :
def count_bombs_around(x,y):
    
    global List_bomb
    
    nb = 0
    
    x_check = x+1
    y_check = y
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
        
    x_check = x
    y_check = y+1
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
        
    x_check = x+1
    y_check = y+1
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
        
    x_check = x-1
    y_check = y
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
    
    x_check = x
    y_check = y-1
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
    
    x_check = x-1
    y_check = y-1
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
    
    x_check = x+1
    y_check = y-1
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
        
    x_check = x-1
    y_check = y+1
    xy_ckeck = 10*x_check + y_check
    
    if xy_ckeck in List_bomb:
        nb += 1
    
    return nb;

# Fonction qui choisi les bombes :
def choose_bomb(nb_bomb):
  
  sense.clear()
  
  list_bomb = []
    
  i=0
  while i < nb_bomb :
    x_bomb = randint(0, 7)
    y_bomb = randint(0, 7)
    xy_bomb = 10*x_bomb + y_bomb
    if(xy_bomb in list_bomb):
      i = i
    else:
      i += 1
      list_bomb.append(xy_bomb)

  return list_bomb;

# Initialisation du plateau de jeu :
def set_all_in_gray():
    G = grey

    set_color_grey = [
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G
    ]

    sense.set_pixels(set_color_grey)

def color_case(list):
    
    i = 0
    while i < len(list):
        y = list[i] % 10
        x = int((list[i]- y)/10)
        i += 1
        print(x)
        print(y)
        
        nb = count_bombs_around(x,y)
        
        if -1 < x < 8 and -1 < y < 8:
            if nb == 0:
                sense.set_pixel(x, y, white)
            elif nb == 1:
                sense.set_pixel(x, y, yellow)
            elif nb == 2:
                sense.set_pixel(x, y, orange)
            elif nb == 3:
                sense.set_pixel(x, y, corail)
            elif nb == 4:
                sense.set_pixel(x, y, red)
            elif nb == 5:
                sense.set_pixel(x, y, bordeau)
            else:
                sense.set_pixel(x, y, black)
    
# Fonction pour une nouvelle partie :
def new_game(nb):
    
    # On séléctionne la variable externe qui contiendra les bombes
    global List_bomb
    
    # Création aléatoire des bombes
    List_bomb = choose_bomb(nb)
    
    print(List_bomb)
    
    # On réinitialise le plateau de jeu.
    set_all_in_gray()
    

# Initialisation des variables de déplacement.
    global x
    global y
    
    x = 0
    y = 0

def check_case(x,y):
    global list_checked
    
    if ((x+1)*10 + y) not in list_checked:
        if count_bombs_around(x+1,y) == 0 and -1<(x+1)<8 and -1<y<8:
            list_checked.append((x+1)*10+y)
            print(list_checked)
            check_case(x+1,y)
            
            
        else:
            list_checked.append((x+1)*10+y)
 
    
    if ((x+1)*10 + y+1) not in list_checked:
        if count_bombs_around(x+1,y+1) == 0 and -1<(x+1)<8 and -1<(y+1)<8:
            list_checked.append((x+1)*10+(y+1))
            check_case(x+1,y+1)
        else:
            list_checked.append((x+1)*10+(y+1))
    
    if ((x)*10 + y+1) not in list_checked:
        if count_bombs_around(x,y+1) == 0 and -1<x<8 and -1<(y+1)<8:
            list_checked.append(x*10+(y+1))
            check_case(x,y+1)
        else:
            list_checked.append(x*10+(y+1))
            
    if ((x-1)*10 + y+1) not in list_checked:
        if count_bombs_around(x-1,y+1) == 0 and -1<(x-1)<8 and -1<(y+1)<8:
            list_checked.append((x-1)*10+(y+1))
            check_case(x-1,y+1)
        else:
            list_checked.append((x-1)*10+(y+1))
        
    if ((x-1)*10 + y) not in list_checked:
        if count_bombs_around(x-1,y) == 0 and -1<(x-1)<8 and -1<y<8:
            list_checked.append((x-1)*10+y)
            check_case(x-1,y)
        else:
            list_checked.append((x-1)*10+y)
        
    if ((x-1)*10 + y-1) not in list_checked:
        if count_bombs_around(x-1,y-1) == 0 and -1<(x-1)<8 and -1<(y-1)<8:
            list_checked.append((x-1)*10+(y-1))
            check_case(x-1,y-1)
        else:
            list_checked.append((x-1)*10+(y-1))
        
    if ((x)*10 + y-1) not in list_checked:
        if count_bombs_around(x,y-1) == 0 and -1<x<8 and -1<(y-1)<8:
            list_checked.append(x*10+(y-1))
            check_case(x,y-1)
        else:
            list_checked.append(x*10+(y-1))
        
    if ((x+1)*10 + y-1) not in list_checked:
        if count_bombs_around(x+1,y-1) == 0 and -1<(x+1)<8 and -1<(y-1)<8:
            list_checked.append((x+1)*10+(y-1))
            check_case(x+1,y-1)
        else:
            list_checked.append((x+1)*10+(y-1))
            
    return list_checked;
            

def end_game():
    
    x=-1
    y=-1
    nb = 0
    
    for i in range(8):
        x += 1
        for j in range(8):
            y += 1
            if sense.get_pixel(x,y) == [88,92,104]:
                nb += 1
        y = -1
        
    if nb == nb_bombs:
        sense.show_message("Tu as gagne")
        

def color_case(list):
    i=0
    while i<len(list):
        y = list[i] % 10
        x = int((list[i] - y)/10)
        nb = count_bombs_around(x,y)
        
        if nb == 0:
            sense.set_pixel(x, y, white)
        elif nb == 1:
            sense.set_pixel(x, y, yellow)
        elif nb == 2:
            sense.set_pixel(x, y, orange)
        elif nb == 3:
            sense.set_pixel(x, y, corail)
        elif nb == 4:
            sense.set_pixel(x, y, red)
        elif nb == 5:
            sense.set_pixel(x, y, bordeau)
        else:
            sense.set_pixel(x, y, black)

# Fonction qui effectue l'action sur la case selectionnée :
def use_case(x, y):

    global List_bomb
    
    xy = x*10 + y
    
    if sense.get_pixel(x,y) == [88,92,104]:
        if xy in List_bomb:
            appear_explosion()
##            sense.clear(255,0,0)
            #explode(x,y) # Fonction à créer
        else:
##            appear_explosion()
            
        
            list_case_checked = check_case(x,y)
            # Quand la propagation est terminée on met toutes les cases propagées avec de la couleur.
            color_case(list_case_checked)
            # A la fin de use_case on remet la liste à zéro pour la prochaine utilisation :
            list_checked = []

                
                
            # A la fin de use case on check si c'est fini
            
            end_game()            

# Début de game :
new_game(nb_bombs)

# Animation d'explosion:
def appear_explosion():
    for x in range(5):
        x.square(image, [0,0], [7,0], [7,7],[0,7],[randint(0,255),randint(0,255),randint(0,255)],.01)
        x.square(image, [1,1], [6,1], [6,6],[1,6],[randint(0,255),randint(0,255),randint(0,255)],.01)
        x.square(image, [2,2], [5,2], [5,5],[2,5],[randint(0,255),randint(0,255),randint(0,255)],.01)
    
    
# Partie qui gère le déplacement via le joystick :

M = [
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]

for x in range(8):
    for y in range(8):
        M[x][y] = count_bombs_around(x, y)
for line in M:
    print(line)

while game:
    while running:
        for event in sense.stick.get_events():         
            if event.action == 'pressed':
                #print(event) Pour voir sur la console les events executés.
                
                sense.set_pixel(x, y, old_color)
                if event.direction == 'down' and y < 7:
                    
                    y = y + 1
                    old_color =sense.get_pixel(x, y)
                        
                elif event.direction == 'up' and y > 0:
                    
                    y = y - 1
                    old_color =sense.get_pixel(x, y)
                        
                elif event.direction == 'right' and x < 7:
                    
                    x = x + 1
                    old_color =sense.get_pixel(x, y)
                        
                elif event.direction == 'left' and x > 0:
                    
                    x = x - 1
                    old_color =sense.get_pixel(x, y)
                        
                elif event.direction == 'middle':
                    
                    use_case(x,y)
                    running = False
                    
        if running == True:        
            # On crée le clignotement :
            t = int(3*time())
            if t%2 == 0:
                sense.set_pixel(x, y, old_color)
            else:
                sense.set_pixel(x, y, green)
        
    if running == False:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'down' or event.direction == 'up' or event.direction == 'right' or event.direction == 'left':
                    
                    running = True
                    
                    if event.direction == 'down' and y < 7:
                        
                        y = y + 1
                        
                    elif event.direction == 'up' and y > 0:
                    
                        y = y - 1
                        
                    elif event.direction == 'right' and x < 7:
                    
                        x = x + 1
                        
                    elif event.direction == 'left' and x > 0:
                    
                        x = x - 1
                        
                        

