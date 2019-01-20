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

color = (0, 0, 0)

score = 0

state = 0

sense = SenseHat()

## Définition des formes dans la variables shapes = I, L et O

sense.clear()

I=[[0, 1, 0],
   [0, 1, 0],
   [0, 1, 0]]

L=[[1, 0],
   [1, 1]]

O=[[1, 1],
   [1, 1]]

shapes = (I, L, O)

P = choice(shapes) ## Choisit une forme au hasard

if P == L:
    color = red
elif P == I:
    color = cyan
else:
    color = yellow

dx = 0
dy = 0

def matrix_print(M): ## Affiche une matrice
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)
                    
def matrix_print_down(M):
    global dy
    dy+=1
    n=len(M)
    for y in range(n): ## Supprime la forme précédente
        for x in range(n):
            if 0 <= 4+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy-1, black)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 4+x+dx == -1:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy-1, black)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                sense.set_pixel(4+x+dx, y+dy, color)


def matrix_print_left(M): ## Fonction qui bouge la forme sur la gauche
    global dx
    dx -= 1
    n = len(M)
    for y in range(n): ## Supprime la forme précédente
        for x in range(n):
            if 0 <= 4+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(4+x+dx+1, y+dy, black)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 4+x+dx == -1:
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


def rotate_90(matrix): # Tourne la matrice carrée de 90 degrés vers la droite (fonction empruntée sur internet)
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

matrix_print(P)

state=1

while state == 1:
    for event in sense.stick.get_events():
         if event.action == 'pressed' and event.direction == 'middle':
            if P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]:
                if dx == -5 or dx == 2:
                    pass
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

while state==1:
    dy += 1
    sleep(1)
    n = len(P)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy-1, black)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                    sense.set_pixel(4+x+dx, y+dy, color)

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
