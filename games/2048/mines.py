# File: Démineur
# Author: Fabian Roulin et Mirko Pirona
# Date: 8.01.2019

# Il manque :nimation explode, win, lose, fontion qui compte de nombre de bombs around

from sense_hat import SenseHat
import pygame
from pygame.locals import *
from random import randint, choice
from time import sleep, time
from gamelib import *

# Drapeau (GREEN)
# Case non-découverte (GREY)
# Case vide = 0 bombe (WHITE)
# 1 bombe à proximité (YELLOW)
# 2 bombes à proximité (ORANGE)
# 3 bombes à proximité (CORAIL)
# 4 bombes à proximité (RED)
# 5 bombe à proximité (BORDEAU)
# Bombe (BLACK)

# On lance pygame :
pygame.init()
pygame.display.set_mode((90,5)) # Correspond à une petite fenêtre

# On lance sense hat :
sense = SenseHat()
sense.clear()

# On initialise les variables globals:

# On crée la variable qui contiendra les bombes :
List_bomb = []


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
#    print(T)


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

def choose_bomb(nb_bomb):
    """Chooses the bomb."""
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

def set_all_in_gray():
    """Initialises the board."""
    G = GRAY

    set_color_gray = [
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G
    ]

    sense.set_pixels(set_color_gray)

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
            sense.set_pixel(x, y, RED)
        
        # A finir ...


def main():
    # Début de game :
    new_game(5)

    # On crée les variables de déplacement :
    x = 0
    y = 0
    old_color = GRAY

    # Partie qui gère le déplacement via le joystick :
    game = True
    running = True
    
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
                    sense.set_pixel(x, y, GREEN)
            
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
                        
# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    main() 