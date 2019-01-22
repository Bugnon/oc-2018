## Dossier : Programme du jeu Tetris sur le SenseHat
## Auteurs : Valentin Piquerez & Hugo Ducommun
## Date : Janvier 2019

from sense_hat import SenseHat
from time import sleep, time
from random import randint, choice

## Définition des couleurs

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
white = (255, 255, 255)
black = (0, 0, 0)

color = (0, 0, 0) # Couleur de la forme qui descend

score = 0 # Le nombre de lignes que le joueur aura réussi à faire disparaître

state = 0 # State = 0 quand le jeu est en statique et state = 1 quand il est en dynamique (la forme descend)

sense = SenseHat()
dx = 0 # Variable de déplacement sur l'axe X
dy = 0 # Variable de déplacement sur l'axe Y (+1 chaque seconde)
dt = 1 # Variable delta du temps (temps entre chaque descente)
## Définition des formes dans des matrices

sense.clear()

# La barre verticale de 3 en cyan
I=[[0, 1, 0],
   [0, 1, 0],
   [0, 1, 0]]
# Le L en rouge
L=[[1, 0],
   [1, 1]]
# Le carré 2x2 en jaune
O=[[1, 1],
   [1, 1]]

shapes = (I, L, O)

def matrix_print(M): ## Affiche une matrice en haut au milieu
    dx = 0 # Variable de déplacement sur l'axe X
    dy = 0 # Variable de déplacement sur l'axe Y (+1 chaque seconde)
    dt = 1 # Variable delta du temps (temps entre chaque descente)
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)
                    
def matrix_print_down(M): ## Déplace la matrice vers le bas
    global dy
    dy+=1
    n=len(M)
    for y in range(n): ## Supprime la matrice précédente
        for x in range(n):
            if 0 <= y+dy <= 7:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy-1, black)
            elif M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and y+dy == 8: # Permet à la barre tournée horizontalement de descendre jusqu'en bas
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy-1, black)
            else:
                dy -= 1
    for y in range(n): ## Affiche la nouvelle matrice descendue de 1
        for x in range(n):
            if 0 <= y+dy <= 7:   
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)
            elif M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and y+dy == 8:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)


def matrix_print_left(M): ## Fonction qui bouge la matrice sur la gauche
    global dx
    dx -= 1
    n = len(M)
    for y in range(n): ## Supprime la forme précédente
        for x in range(n):
            if 0 <= 4+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx+1, y+dy, black)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 4+x+dx == -1: # Permet à la barre verticale d'aller sur les côtés
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx+1, y+dy, black)
            else:
                dx += 1              
    
    for y in range(n): ## Affiche la nouvelle forme décalée à gauche
        for x in range(n):
            if 0 <= 4+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 4+x+dx == -1:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)

def matrix_print_right(M): ## Même principe que matrix_print_left mais à droite
    global dx
    dx += 1
    n = len(M)
    for y in range(n):
        for x in range(n):
            if 0 <= 4+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx-1, y+dy, black)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 4+x+dx == 8:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx-1, y+dy, black)
            else:
                dx -= 1

    for y in range(n):
        for x in range(n):
            if 0 <= 4+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 4+x+dx == 8:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)


def rotate_90(matrix): # Tourne la matrice carrée de 90 degrés vers la droite (fonction en partie empruntée sur internet)
    n = len(matrix)
    for y in range(n):
        for x in range(n):
            if matrix[y][x]==1:
                sense.set_pixel(4+x+dx, y+dy, black)
    for layer in range((n + 1) // 2):
        for index in range(layer, n - 1 - layer, 1):
            matrix[layer][index], matrix[n - 1 - index][layer], \
                matrix[index][n - 1 - layer], matrix[n - 1 - layer][n - 1 - index] = \
                matrix[n - 1 - index][layer], matrix[n - 1 - layer][n - 1 - index], \
                matrix[layer][index], matrix[index][n - 1 - layer]
    for y in range(n):
        for x in range(n):
            if matrix[y][x]==1:
                sense.set_pixel(4+x+dx, y+dy, color)
    return matrix

sense.clear()

state = 0 # Lance le moment où la forme commence à descendre (dymnaique)

t0 = time()

a = 0

while state==0:
    for i in range(8):
        a=0
        for j in range(8):
            if sense.get_pixel(7-j, 7-i) != [0, 0, 0]:
                a+=1
                if a==8:
                    score+=1
                    for k in range(8):
                        sense.set_pixel(k, 7-i, black)
                    for c in reversed(range(7-i)):
                        for d in range(8):
                            sense.set_pixel(d, c+1, (sense.get_pixel(d, c)))
                            sense.set_pixel(d, c, black)
    state=1
    a=0

while state == 1:
    if a==0:
        P = choice(shapes) ## Choisit une forme au hasard parmi les trois
        matrix_print(P)
        a=1
    if P == L:
        color = red
    elif P == I:
        color = cyan
    else:
        color = yellow
    for event in sense.stick.get_events():
         if event.action == 'pressed' and event.direction == 'middle':
            if P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]:
                if dx == -5 or dx == 2:
                    pass # Empêche de tourner la barre quand elle est verticale et dans un côté
                else:
                    rotate_90(P)
            elif P == [[0, 0, 0], [1, 1, 1], [0, 0, 0]]:
                if dy == 6:
                    pass # Empêche de tourner la barre quand elle est horizontale et tout en bas
                else:
                    rotate_90(P)
            else:
                rotate_90(P)
         elif event.direction == 'down' and event.action == 'held':
            matrix_print_down(P)
         elif event.direction == 'left' and event.action == 'pressed':
            matrix_print_left(P)
         elif event.direction == 'right' and event.action == 'pressed':
            matrix_print_right(P)

    if P == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and dy == 7:
        state=0
    elif P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and dy == 5:
        state=0
    elif P == O and dy == 6:
        state=0
    elif P == L and dy == 6:
        state=0
     
    t = time()
    if t > t0 + dt: 
        matrix_print_down(P)
        t0 = t
