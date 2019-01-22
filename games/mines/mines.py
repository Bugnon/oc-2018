# File: Démineur
# Author: Fabian Roulin et Mirko Pirona
# Date: 8.01.2019

# Il manque :nimation explode, win, lose, fontion qui compte de nombre de bombs around

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

# On crée les variables de déplacement :
game = True
running = True
x = 0
y = 0

old_color = grey

# Définition des fonctions du programme :

# Fonction qui compte le nombre de bombes à proximité :
def create_map(bombs):
    T = [[0] *10] * 10
    print(bombs)
    for (x, y) in bombs:
        print(x, y)
        T[x][y] += 1
        T[x+1][y] += 1
        T[x][y+1] += 1
        T[x+2][y] += 1
        T[x][y+2] += 1
        T[x+2][y+2] += 1
        T[x+1][y+2] += 1
        T[x+2][y+1] += 1
        
    
    print(T)


def count_bombs_around(x,y):
    
    global List_bomb
    
    nb = 0
    
    xy = x*10 + y
    
    xy += 10
    
    if xy in List_bomb:
        nb += 1
        
    xy += 1
    
    if xy in List_bomb:
        nb += 1
        
    xy -= 10
    
    if xy in List_bomb:
        nb += 1
        
    xy -= 10
    
    if xy in List_bomb:
        nb += 1
        
    xy -= 1
    
    if xy in List_bomb:
        nb += 1
        
    xy -= 1
    
    if xy in List_bomb:
        nb += 1
        
    xy += 10
    
    if xy in List_bomb:
        nb += 1
        
    xy += 10
    
    if xy in List_bomb:
        nb += 1
    
    return nb;

# Fonction qui choisi les bombes :
def choose_bomb(nb_bomb):
  
  sense.clear()
  
  liste = []
    
  i=0
  while i < nb_bomb :
    x = randint(0, 7)
    y = randint(0, 7)
    if (x, y) not in liste:
        liste.append((x, y))
        i = i + 1

  return liste;

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

# Fonction pour une nouvelle partie :
def new_game(nb):
    
    # On séléctionne la variable externe qui contiendra les bombes
    global List_bomb
    
    # Création aléatoire des bombes
    List_bomb = choose_bomb(nb)
    
    print(List_bomb)
    create_map(List_bomb)
    
    # On réinitialise le plateau de jeu.
    set_all_in_gray()
    

# Initialisation des variables de déplacement.
    global x
    global y
    
    x = 0
    y = 0

# Fonction qui effectue l'action sur la case selectionnée :
def use_case(x, y):

    global List_bomb

    if (x, y) in List_bomb:
        sense.clear(255,0,0)
        #explode(x,y) # Fonction à créer
    else:
        nb = count_bombs_around(x,y) # Fonction à créer
    
        if nb == 0:
            sense.set_pixel(x, y, white)
        elif nb == 1:
            sense.set_pixel(x, y, red)
        
        # A finir ...

# Début de game :
new_game(5)
# Partie qui gère le déplacement via le joystick :

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