## Dossier : Programme du jeu Tetris sur le SenseHat
## Auteurs : Valentin Piquerez & Hugo Ducommun
## Date : Janvier 2019

from sense_hat import SenseHat
from time import sleep, time
from random import randint, choice

## Définition des variables classiques

red = (255, 0, 0)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

sense = SenseHat()

### Définition des variables propres à notre jeu ###

color = (0, 0, 0) # Couleur de la forme qui descend

score = 0 # Le nombre de lignes que le joueur aura réussi à faire disparaître

state = 1 # State = 0 quand le jeu est en statique (entre les apparitions de formes) et state = 1 quand il est en dynamique (la forme descend)

game = 1 # Si game = 1 alors le jeu contine sinon c'est game over

t0 = time() # Variable de temps qui nous servira pour la descente des formes

dx = 0 # Variable de déplacement sur l'axe X
dy = 0 # Variable de déplacement sur l'axe Y (+1 chaque seconde)
dt = 1 # Temps entre chaque descente en seconde

### Définition des formes dans des matrices ###

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

shapes = (I, L, O) # Variable contenant les 3 formes

P = choice(shapes) # Choisit une forme au hasard parmi les trois et la stock dans la variable P

if P == L: # Assigne la couleur de la forme choisie à la variable color
    color = red
elif P == I:
    color = cyan
else:
    color = yellow
    
### Définition des fonctions ###

def matrix_print(M): ## Affiche une matrice en haut au milieu
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                sense.set_pixel(3+x, y, color)

def matrix_print_down(M): ## Déplace la matrice vers le bas
    global state
    global dy
    global dx
    if state==1:
        dy+=1
        n=len(M)
        for y in range(n): ## Supprime la matrice précédente
            for x in range(n):
                if 0 <= y+dy <= 7:
                    if M[y][x]==1:
                        sense.set_pixel(3+x+dx, y+dy-1, black)
                elif M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and y+dy == 8: # Permet à la barre tournée horizontalement de descendre jusqu'en bas
                    if M[y][x]==1:
                        sense.set_pixel(3+x+dx, y+dy-1, black)
                else:
                    dy -= 1
        for y in range(n): ## Affiche la nouvelle matrice descendue de 1
            for x in range(n):
                if 0 <= y+dy <= 7:   
                    if M[y][x]==1:
                        sense.set_pixel(3+x+dx, y+dy, color)
                elif M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and y+dy == 8:
                    if M[y][x]==1:
                        sense.set_pixel(3+x+dx, y+dy, color)
                else:
                    state=0


def matrix_print_left(M): ## Fonction qui bouge la matrice sur la gauche
    global dx
    dx -= 1
    n = len(M)
    for y in range(n): ## Stop la forme quand elle est contre une autre forme
        if M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and -1 <= 3+dx <= 7:
            if M[y][1]==1 and sense.get_pixel(3+dx+1, y+dy)!=[0, 0, 0]:
                dx+=1
                return ;
        elif 0 <= 3+dx <= 7:
            if M[y][0]==1 and sense.get_pixel(3+dx, y+dy)!=[0, 0, 0]:
                dx+=1
                return ;
    for y in range(n): ## Supprime la forme précédente
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx+1, y+dy, black)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == -1: # Permet à la barre verticale d'aller sur les côtés
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx+1, y+dy, black)
            else:
                dx += 1              
    
    for y in range(n): ## Affiche la nouvelle forme décalée à gauche
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx, y+dy, color)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == -1:
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx, y+dy, color)

def matrix_print_right(M): ## Même principe que matrix_print_left mais à droite
    global dx
    dx += 1
    n = len(M)
    for y in range(n): ## Empeche de continuer quand elle est en colision avec une forme 
            if M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and -1 <= 3+dx <= 6:
                if M[y][1]==1 and sense.get_pixel(3+dx+1, y+dy)!=[0, 0, 0]:
                    dx-=1
                    return ;
            if M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and -1 <= 3+dx <= 5:
                if M[y][2]==1 and sense.get_pixel(3+dx+2, y+dy)!=[0, 0, 0]:
                    dx-=1
                    return ;
            elif 0 <= 3+dx <= 6:
                if M[y][1]==1 and sense.get_pixel(3+dx+1, y+dy)!=[0, 0, 0]:
                    dx-=1
                    return ;
    for y in range(n): ## Supprime la forme
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx-1, y+dy, black)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == 8:
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx-1, y+dy, black)
            else:
                dx -= 1

    for y in range(n): ##Affiche laf orme un pixel plus bas
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx, y+dy, color)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == 8:
                if M[y][x]==1:
                    sense.set_pixel(3+x+dx, y+dy, color)


def rotate_90(matrix): # Tourne la forme de 90 degrés vers la droite (fonction en partie empruntée sur internet)
    n = len(matrix)
    for y in range(n): # Supprime la forme
        for x in range(n):
            if matrix[y][x]==1:
                sense.set_pixel(3+x+dx, y+dy, black)
    for layer in range((n + 1) // 2): # Tourne la matrice carrée de 90 degrés vers la droite
        for index in range(layer, n - 1 - layer, 1):
            matrix[layer][index], matrix[n - 1 - index][layer], \
                matrix[index][n - 1 - layer], matrix[n - 1 - layer][n - 1 - index] = \
                matrix[n - 1 - index][layer], matrix[n - 1 - layer][n - 1 - index], \
                matrix[layer][index], matrix[index][n - 1 - layer]
    for y in range(n): # Affiche la nouvelle forme à partir de la matrice tournée
        for x in range(n):
            if matrix[y][x]==1:
                sense.set_pixel(3+x+dx, y+dy, color)
    return matrix

sense.clear()

matrix_print(P)

while game == 1:
    while state == 1:
        for event in sense.stick.get_events():
             if event.action == 'pressed' and event.direction == 'middle':
                if P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]:
                    if dx == -4 or dx == 3:
                        pass # Empêche de tourner la barre quand elle est verticale et dans un côté
                    elif sense.get_pixel(3+dx, dy+1)!=[0, 0, 0] or sense.get_pixel(3+dx+2, dy+1)!=[0, 0, 0]:
                        pass
                    else:
                        rotate_90(P)
                elif P == [[0, 0, 0], [1, 1, 1], [0, 0, 0]]:
                    if dy == 6:
                        pass # Empêche de tourner la barre quand elle est horizontale et tout en bas
                    else:
                        rotate_90(P)
                else:
                    rotate_90(P)
             elif event.direction == 'down' and event.action == 'pressed':
                matrix_print_down(P)
             elif event.direction == 'left' and event.action == 'pressed':
                matrix_print_left(P)
             elif event.direction == 'right' and event.action == 'pressed':
                matrix_print_right(P)

        if P == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and dy == 6: # Si la forme est en bas, on passe en state=0
            state=0
        elif P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and dy == 5:
            state=0
        elif P == O and dy == 6:
            state=0
        elif P == L and dy == 6:
            state=0
    
        n=len(P)
        for x in range(n): # Check si la forme peut descendre ou pas. Si elle ne peut pas descendre à son apparition, game over
            if P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and dy < 5:
                if sense.get_pixel(dx+4, dy+3) != [0, 0, 0]:
                    if dy==0:
                        game=0
                    state=0
            elif dy < 6 and P != [[0, 1, 0], [0, 1, 0], [0, 1, 0]]:
                if P[1][x]==1 and sense.get_pixel(x+dx+3, dy+2) != [0, 0, 0]:
                    if dy==0: # Si la forme est bloquée juste après être apparue
                        game=0
                    state=0
                    
        Lcomplet=0 # Check si la forme L est complétée par un autre pixel, ce qui fait passer le jeu en state=0
        for x in range (n):
            for y in range(n):
                if P == [[0, 1],[1, 1]] or P == [[1, 0],[1, 1]] or P == [[1, 1],[0, 1]] or P == [[1, 1],[1, 0]]:
                    if sense.get_pixel(x+dx+3, y+dy)!=[0, 0, 0]:
                        Lcomplet+=1
                    if Lcomplet==4:
                        state=0
        
        t = time() # Descend la forme chaque seconde
        if t > t0 + dt:
            matrix_print_down(P)
            t0 = t

    while state == 0:
        sleep(1)
        for g in range(8): # Supprime les lignes complétées et incrémente le score de 1
            for i in range(8):
                a = 0
                for j in range(8):
                    if sense.get_pixel(7-j, 7-i) != [0, 0, 0]:
                        a += 1
                        if a == 8:
                            score += 1
                            for k in range(8):
                                sense.set_pixel(k, 7-i, black)
                            for c in reversed(range(7-i)):
                                for d in range(8):
                                    sense.set_pixel(d, c+1, (sense.get_pixel(d, c)))
                                    sense.set_pixel(d, c, black)
                                    
        P = choice(shapes) # Choisit une forme au hasard
        
        dx = 0 # Remet les variables de position a 0
        dy = 0
        
        if P == L:
            color = red
        elif P == I:
            color = cyan
        else:
            color = yellow
            
        t0=time()
        
        matrix_print(P)

        if game == 0: # Si la partie est terminée, on affiche le score
            sense.show_message('Game over ! Score :', scroll_speed=0.05)
            sense.show_message(str(score), scroll_speed=0.2)
        else:
            state = 1
        