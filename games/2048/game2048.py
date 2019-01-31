"""
File: 2048_Game
Author: Massimo Stefani , Michael Greub
Date: 28.12.2018

This is a game of 2048 to be played on the Raspberry SenseHAT.
"""

# Importation des modules requis
from sense_hat import SenseHat
from random import randint
from time import sleep
from time import time

sense = SenseHat()
sense.clear(0, 0, 0)
size = 8


#-----Définition des couleurs-----

MESSAGE = (128, 124, 128)
BLACK_0 = (0, 0, 0)
BLUE_1 = (0, 255, 255)
GREEN_2 = (0, 255, 127)
GREEN_3 = (0, 255, 0)
GREEN_4 = (127, 255, 0)
YELLOW_5 = (255, 255, 0)
ORANGE_6 = (255, 127, 0)
RED_7 = (255, 0, 0)
PINK_8 = (255, 0, 127)
PINK_9 = (255, 0, 255)
PINK_10 = (127, 0, 255)
BLUE_11 = (0, 0, 255)
BLUE_12 = (0, 127, 255)
WHITE_13 = (255, 255, 255)
r = RED_7
o = BLACK
y = YELLOW_5

colors = [BLACK_0, BLUE_1, GREEN_2, GREEN_3, GREEN_4, YELLOW_5, ORANGE_6, RED_7,\
          PINK_8, PINK_9, PINK_10, BLUE_11, BLUE_12, WHITE_13,]

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

L_CROSS = [r, o, o, o, o, o, o, r,
           o, r, o, o, o, o, r, o,
           o, o, r, o, o, r, o, o,
           o, o, o, r, r, o, o, o,
           o, o, o, r, r, o, o, o,
           o, o, r, o, o, r, o, o,
           o, r, o, o, o, o, r, o,
           r, o, o, o, o, o, o, r
          ]
L_WIN = [ o, o, o, o, o, o, o, o,
          o, y, y, y, y, y, y, o,
          o, y, y, y, y, y, y, o,
          o, y, y, y, y, y, y, o,
          o, o, y, y, y, y, o, o,
          o, o, o, y, y, o, o, o,
          o, o, o, y, y, o, o, o,
          o, y, y, y, y, y, y, o,
        ]

#----- Définitionts des fonctions-----

    
def startup():
    global size
    for x in range(4):
        for y in range(4):
            L4[x][y] = 0
    for x in range(8):
        for y in range(8):
            L8[x][y] = 0
    sense.clear()
    sense.show_message('Choose your mode:',0.075, MESSAGE)
    modes = ['4X4', '8X8']
    mode = [4, 8]
    sleep(0.2)
    selecting = True
    i = 0
    while selecting:
        sense.show_message(modes[i], 0.1, MESSAGE)
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right' or event.direction == 'left':
                    i = (i + 1) % 2
                    sense.show_message(modes[i], 0.1, MESSAGE)
                elif event.direction == 'middle':
                    selecting = False
                    size = mode[i]
                
    new_block(size)



    

        
def set_pixels(n):
    if n == 8:
        for x in range(8):
            for y in range(8):
                sense.set_pixel(x, y, colors[L8[x][y]])
    elif n == 4:
        L8_affichage = [
                       [L4[0][0], L4[0][0], L4[0][1], L4[0][1], L4[0][2], L4[0][2], L4[0][3], L4[0][3]],
                       [L4[0][0], L4[0][0], L4[0][1], L4[0][1], L4[0][2], L4[0][2], L4[0][3], L4[0][3]],
                       [L4[1][0], L4[1][0], L4[1][1], L4[1][1], L4[1][2], L4[1][2], L4[1][3], L4[1][3]],
                       [L4[1][0], L4[1][0], L4[1][1], L4[1][1], L4[1][2], L4[1][2], L4[1][3], L4[1][3]],
                       [L4[2][0], L4[2][0], L4[2][1], L4[2][1], L4[2][2], L4[2][2], L4[2][3], L4[2][3]],
                       [L4[2][0], L4[2][0], L4[2][1], L4[2][1], L4[2][2], L4[2][2], L4[2][3], L4[2][3]],
                       [L4[3][0], L4[3][0], L4[3][1], L4[3][1], L4[3][2], L4[3][2], L4[3][3], L4[3][3]],
                       [L4[3][0], L4[3][0], L4[3][1], L4[3][1], L4[3][2], L4[3][2], L4[3][3], L4[3][3]]
                       ]
        for x in range(8):
            for y in range(8):
                sense.set_pixel(x,y, colors[L8_affichage[x][y]])




        

def new_block(n):
    sleep(0.25)
    i = 0
    L = L4 if n == 4 else L8
    for x in range(n):
        for y in range(n):
            if L[x][y] == 0:
                i = i+1
    if i > 1:
        r = randint(0,1)
        while r < 2: #tant qu'on en a pas créé 2
            x = randint(0, (n - 1))# 
            y = randint(0, (n - 1))
            # On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y] = 1 # On défini un bloc de couleur correspondant au chiffre 2
                r = r + 1# Si le bloc est créé on indente pour créé exactement 2 nouveaux pixels
    elif i == 1:
        r = randint(0, 1)
        while r < 1: #tant qu'on en a pas créé 2
            x = randint(0, (n - 1))# 
            y = randint(0, (n - 1))# On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y] = 1 # On défini un bloc de couleur correspondant au chiffre 2
                r = r + 1
    control_end(n)
    set_pixels(n)

def moved_up(n):
    L = L4 if n == 4 else L8 
    for x in range(n): 
        for y in range(n):# Sur chaque pixel en prenantles pixels en ligne puis en colonne
            if L[x][y] > 0 and y >= 1:# On controle que le pixel ne soit pas une case vide
                while L[x][y - 1] == 0 and y >= 1:# Si la case est vide 
                L[x][y - 1] = L[x][y]
                L[x][y] = 0
                y = y - 1
            if L[x][y - 1] == L[x][y]:
                L[x][y - 1] = L[x][y - 1] + 1
                L[x][y] = 0
    set_pixels(n)
    new_block(n)
    

def moved_down(n):
    L = L4 if n == 4 else L8
    for x in range(n):
        for z in range(n - 1):
            y = n - 2 - z
            if L[x][y] > 0 and y <= (n - 2):# On controle que le pixel ne soit pas une case vide
                while y <= (n - 2) and L[x][y + 1] == 0:# Si la case est vide
                    L[x][y + 1] = L[x][y]
                    L[x][y] = 0
                    y = y + 1
                if y < (n - 1) and L[x][y + 1] == L[x][y]:
                    L[x][y + 1] = L[x][y + 1] + 1
                    L[x][y] = 0
    set_pixels(n)
    new_block(n)
    
   
def moved_left(n):
    """Reacts to the joystick pushed left."""
    L = L4 if n == 4 else L8
    for y in range(n):
        for x in range(n):
            if L[x][y] > 0:# On controle que le pixel ne soit pas une case vide
                while x > 0 and L[x - 1][y] == 0:# Si la case est vide 
                    L[x - 1][y] = L[x][y]
                    L[x][y] = 0
                    x = x - 1
                if L[x - 1][y] == L[x][y]:
                    L[x - 1][y] = L[x - 1][y] + 1
                    L[x][y] = 0 
    set_pixels(n)
    new_block(n)

def moved_right(n):
    """Reacts to the joystick pushed right."""
    L = L4 if n == 4 else L8
    for y in range(n):
        for z in range(n - 1):
            x = n - 2 - z
            if L[x][y] > 0 and x < (n - 1):
                while x < (n - 1) and L[x + 1][y] == 0:
                    L[x + 1][y] = L[x][y]
                    L[x][y] = 0
                    x = x + 1
                if x < (n - 1) and L[x + 1][y] == L[x][y]:
                    L[x + 1][y] = L[x + 1][y] + 1
                    L[x][y] = 0
    set_pixels(n)
    new_block(n)

def control_end(n):
    """Returns True when the game is finished."""
    end = True
    L = L4 if n == 4 else L8
        
    # check if there are empty cells        
    for x in range(n):
        for y in range(n):
            if L[x][y] == 0:
                end = False
     
    # check neighbors for center cells    
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            if L[x][y] == L[x][y + 1] or L[x][y] == L[x + 1][y] or L[x][y] == L[x - 1][y]\
                or L[x][y] == L[x][y - 1]:
                end = False
                break
    # check neigbors for border cells
    for x in range(n - 1):
        if L[0][x] == L[0][x + 1] or L[x][0] == L[x + 1][0] or L[n - 1][x] == L[n - 1][x + 1] \
            or L[x][n - 1] == L[x + 1][n - 1]:
            end = False
            break

    if end == True:
        set_pixels(n)
        sleep(3)
        r = red_7
        o = black
        sense.clear()
        for i in range(5):
            sense.set_pixels(L_CROSS)
            sleep(0.1)
            sense.clear()
            sleep(0.1)
        sense.set_pixels(L_CROSS)
        sleep(1)
        set_pixels(n)
        sleep(2)
        score = 0
        for x in range(n):
            for y in range(n):
                if L[x][y] != 0:
                    score = score + 2 ** L[x][y]
        sense.show_message('You lose... Your score is:', 0.075, MESSAGE)
        show = True
        while show:
            score = str(score)
            string = score + 'pts'
            sense.show_message(string, 0.1, MESSAGE)
            sense.show_message('Press to end', 0.075, MESSAGE)
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    show = False
        main()
    elif end == False:
        for x in range(n):
            for y in range(n):
                if L[x][y] == 14:
                    victory(n)

def exit():
    """Wait 1 second..."""
    t0 = time()
    while time() < t0 + 1:
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'middle':
                show_message = True
                while show_message:
                    sense.show_message('Press to return to the menu', 0.075, MESSAGE)
                    for event in sense.stick.get_events():
                        if event.action ==  'pressed':
                            show_message = False
                            main()
        
def victory(n):
    L = L4 if n == 4 else L8
    sense.set_pixels(L_WIN)
    sleep(10)
    sense.show_message('Congratulations, you just reached the highest block. Your score is :', 0.075, MESSAGE)
    for x in range(n):
        for y in range(n):
            if L[x][y] != 0:
                score = score + 2 ** L[x][y]
    while show:
        score = str(score)
        string = score + 'pts'
        sense.show_message(string, 0.1, MESSAGE)
        sense.show_message('Press to restart', 0.075, MESSAGE)
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                show = False
    main()

#-----Reactions du joystick-----
    
def main():
    startup()
    running = True

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
                    exit()


if __name__ == '__main__':
    main()
