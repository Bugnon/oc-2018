"""
File: 2048_Game
<<<<<<< HEAD
Author: Massimo ... , Michael Greub
=======
Author: Massimo Stefani , Michael Greub
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
Date: 28.12.2018

This is a game of 2048 to be played on the Raspberry SenseHAT.
"""

# Importation des modules requis
from sense_hat import SenseHat
from random import randint
from time import sleep
<<<<<<< HEAD
from gamelib import *

sense=SenseHat()
=======
from time import time

sense = SenseHat()
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
sense.clear(0, 0, 0)
size = 8


<<<<<<< HEAD
#-----Définition des couleurs-----
message = (128, 124, 128)
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
r = red_7
o = BLACK
y = yellow_5

colors = [BLACK, blue_1, green_2, green_3, green_4, yellow_5, orange_6, red_7,\
          pink_8, pink_9, pink_10, blue_11, blue_12, white_13]
=======
# -----Définition des couleurs-----

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
o = BLACK_0
y = YELLOW_5
end = True

colors = [BLACK_0, BLUE_1, GREEN_2, GREEN_3, GREEN_4, YELLOW_5, ORANGE_6,
          RED_7, PINK_8, PINK_9, PINK_10, BLUE_11, BLUE_12, WHITE_13]
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f

# ------Définition des matrices utilisées------


L4 = [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
<<<<<<< HEAD
      [0, 0, 0, 0], 
     ]
=======
      [0, 0, 0, 0],
      ]
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
L8 = [[0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0]
<<<<<<< HEAD
     ]

L_cross = [r, o, o, o, o, o, o, r,
=======
      ]

L_CROSS = [r, o, o, o, o, o, o, r,
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
           o, r, o, o, o, o, r, o,
           o, o, r, o, o, r, o, o,
           o, o, o, r, r, o, o, o,
           o, o, o, r, r, o, o, o,
           o, o, r, o, o, r, o, o,
           o, r, o, o, o, o, r, o,
           r, o, o, o, o, o, o, r
<<<<<<< HEAD
          ]
L_win = [ o, o, o, o, o, o, o, o,
          o, y, y, y, y, y, y, o,
          o, y, y, y, y, y, y, o,
          o, y, y, y, y, y, y, o,
          o, o, y, y, y, y, o, o,
          o, o, o, y, y, o, o, o,
          o, o, o, y, y, o, o, o,
          o, y, y, y, y, y, y, o,
        ]

#----- Définitionts des fonctions-----
    
def victory():
    global size
    if size ==4:
        L=L4
    elif size== 8:
        L=L8
    sense.set_pixels(L_win)
    sleep(10)
    sense.show_message('Congratulations, you just reached the highest block. Your score is :', 0.05)
    for x in range(size):
            for y in range(size):
                if L[x][y]!=0:
                    score = score + 2**L[x][y]
    while show:
            score = str(score)
            string = score + 'pts'
            sense.show_message(string, 0.05, text_colour = message)
            sense.show_message('Press to restart', scroll_speed = 0.05, text_colour = message)
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    show = False
    startup()


def control_end(e):
    """Returns True when the game is finished."""
    end = True
    if e == 8:
        L = L8
    elif e == 4:
        L = L4
        
    # check if there are empty cells        
    for x in range(e):
        for y in range(e):
            if L[x][y]==0:
                end=False
    
    print('empty', end)
    # check neighbors for center cells    
    for x in range(1, e-1):
        for y in range(1, e-1):
            if L[x][y]==L[x][y+1] or L[x][y]==L[x+1][y] or L[x][y]==L[x-1][y]\
            or L[x][y]==L[x][y-1]:
                end = False
                break
    print('neighbors', end)
    for x in range(e-1):
        if L[0][x] == L[0][x+1] or L[x][0] == L[x+1][0] or L[e-1][x] == L[e-1][x+1] \
        or L[x][e-1] == L[x+1][e-1]:
            end = False
            break
    print('borders', end)
    if end == True:
        set_pixels(e)
        sleep(3)
        r = red_7
        o = BLACK
        sense.clear()
        for i in range(5):
            sense.set_pixels(L_cross)
            sleep(0.1)
            sense.clear()
            sleep(0.1)
        sense.set_pixels(L_cross)
        sleep(1)
        set_pixels(e)
        sleep(2)
        score=0
        for x in range(e):
            for y in range(e):
                if L[x][y]!=0:
                    score = score + 2**L[x][y]
                print(L[x][y], score)
        sense.show_message('You lose... Your score is:',scroll_speed = 0.05, text_colour = message)
        show = True
        while show:
            score = str(score)
            string = score + 'pts'
            sense.show_message(string, 0.05, text_colour = message)
            sense.show_message('Press to end', scroll_speed = 0.05, text_colour = message)
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    show = False
        startup()
    
                                                            
def set_pixels(a):
    if a==8:
        for x in range(8):
            for y in range(8):
                sense.set_pixel(x, y, colors[L8[x][y]])
    elif a==4:
       L8_affichage = [[L4[0][0], L4[0][0], L4[0][1], L4[0][1], L4[0][2], L4[0][2], L4[0][3], L4[0][3]],
                       [L4[0][0], L4[0][0], L4[0][1], L4[0][1], L4[0][2], L4[0][2], L4[0][3], L4[0][3]],
                       [L4[1][0], L4[1][0], L4[1][1], L4[1][1], L4[1][2], L4[1][2], L4[1][3], L4[1][3]],
                       [L4[1][0], L4[1][0], L4[1][1], L4[1][1], L4[1][2], L4[1][2], L4[1][3], L4[1][3]],
                       [L4[2][0], L4[2][0], L4[2][1], L4[2][1], L4[2][2], L4[2][2], L4[2][3], L4[2][3]],
                       [L4[2][0], L4[2][0], L4[2][1], L4[2][1], L4[2][2], L4[2][2], L4[2][3], L4[2][3]],
                       [L4[3][0], L4[3][0], L4[3][1], L4[3][1], L4[3][2], L4[3][2], L4[3][3], L4[3][3]],
                       [L4[3][0], L4[3][0], L4[3][1], L4[3][1], L4[3][2], L4[3][2], L4[3][3], L4[3][3]]
                      ]
#       print(L8_affichage)
       for x in range(8):
            for y in range(8):
                 sense.set_pixel(x,y, colors[L8_affichage[x][y]])




        

def new_block(e):
    sleep(0.25)
    i=0
    if e==4:
        L=L4
    elif e==8:
        L=L8
    for x in range(e):
        for y in range(e):
            if L[x][y]==0:
                i=i+1
    if i>1:
        r=randint(0,1)
        while r<2: #tant qu'on en a pas créé 2
            x=randint(0, (e-1))# 
            y=randint(0, (e-1))
            # On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y]=1 # On défini un bloc de couleur correspondant au chiffre 2
                r=r+1# Si le bloc est créé on indente pour créé exactement 2 nouveaux pixels
    elif i==1:
        r=randint(0, 1)
        while r < 1: #tant qu'on en a pas créé 2
            x=randint(0, (e-1))# 
            y=randint(0, (e-1))# On choisis aléatoirement une ligne et une colonne
            if L[x][y] == 0:# On controle si ce pixel est vide
                L[x][y]=1 # On défini un bloc de couleur correspondant au chiffre 2
                r=r+1
#    print(L4)
    control_end(e)
    set_pixels(e)
    

def startup():
    global size
=======
           ]
L_WIN = [o, o, o, o, o, o, o, o,
         o, y, y, y, y, y, y, o,
         o, y, y, y, y, y, y, o,
         o, y, y, y, y, y, y, o,
         o, o, y, y, y, y, o, o,
         o, o, o, y, y, o, o, o,
         o, o, o, y, y, o, o, o,
         o, y, y, y, y, y, y, o,
         ]

# ----- Définitionts des fonctions-----


def startup():
    """Starts the game"""
    global size
    set_matrices_0()
    sense.clear()
    sense.show_message('Choose your mode:', 0.1, MESSAGE)
    modes = ['4X4', '8X8']
    mode = [4, 8]
    sleep(0.2)
    selecting = True
    i = 0
    selection_startup(selecting, modes, mode, i)
    new_block(size)


def set_matrices_0():
    """Setting matrixes"""
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    for x in range(4):
        for y in range(4):
            L4[x][y] = 0
    for x in range(8):
        for y in range(8):
            L8[x][y] = 0
<<<<<<< HEAD
    sense.clear()
    sense.show_message('Choose your mode:',0.001)
    modes= ['4X4', '8X8']
    mode=[4, 8]
    sleep(0.2)
    selecting=True
    i=0
    while selecting:
        sense.show_message(modes[i])
=======


def selection_startup(selecting, modes, mode, i):
    """Navigation to select the mode"""
    global size
    while selecting:
        sense.show_message(modes[i], 0.1, MESSAGE)
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right' or event.direction == 'left':
                    i = (i + 1) % 2
<<<<<<< HEAD
                    sense.show_message(modes[i])
                elif event.direction == 'middle':
                    selecting = False
                    size=mode[i]
                
    new_block(size)
        
        
                

def moved_up(d):
    if d == 4:
        L = L4
    elif d == 8:
        L = L8  
    for x in range(d): 
       for y in range(d):# Sur chaque pixel en prenantles pixels en ligne puis en colonne
          if L[x][y] > 0 and y>=1:# On controle que le pixel ne soit pas une case vide
             while L[x][y-1] == 0 and y>=1:# Si la case est vide 
                L[x][y-1]=L[x][y]
                L[x][y]=0
                y=y-1
             if L[x][y-1]==L[x][y]:
                L[x][y-1]=L[x][y-1]+1
                L[x][y]=0
    set_pixels(d)
    new_block(d)
    

def moved_down(b):
    if b == 4:
        L = L4
    elif b == 8:
        L = L8
    for x in range(b):
        for z in range(b-1):
            y=b-2-z
            if L[x][y] > 0 and y<=(b-2):# On controle que le pixel ne soit pas une case vide
                while y<=(b-2) and L[x][y+1] == 0:# Si la case est vide
                   L[x][y+1]=L[x][y]
                   L[x][y]=0
                   y=y+1
                if y<(b-1) and L[x][y+1]==L[x][y]:
                   L[x][y+1]=L[x][y+1]+1
                   L[x][y]=0
    set_pixels(b)
    new_block(b)
    
   
def moved_left(size):
    """Reacts to the joystick pushed left."""
    if size == 4:
        L = L4
    elif size == 8:
        L = L8
    for y in range(size):
        for x in range(size):
            if L[x][y] > 0:# On controle que le pixel ne soit pas une case vide
                while x>0 and L[x-1][y] == 0:# Si la case est vide 
                    L[x-1][y]=L[x][y]
                    L[x][y]=0
                    x=x-1
                if L[x-1][y]==L[x][y]:
                   L[x-1][y]=L[x-1][y]+1
                   L[x][y]=0
    set_pixels(size)
    new_block(size)
=======
                    sense.show_message(modes[i], 0.1, MESSAGE)
                elif event.direction == 'middle':
                    selecting = False
                    size = mode[i]


def set_pixels(n):
    """Game is played normaly in a 8x8 mode"""
    if n == 4:
        set_pixels_4()
    else:
        for x in range(8):
            for y in range(8):
                sense.set_pixel(x, y, colors[L8[x][y]])


def set_pixels_4():
        """Game is shown in 4x4. 1 pixel = 4 pixels"""
        L8_affichage = []
        for i in range(8):
            line = []
            for j in range(8):
                line.append(L4[i//2][j//2])
            L8_affichage.append(line)
        for x in range(8):
            for y in range(8):
                sense.set_pixel(x, y, colors[L8_affichage[x][y]])


def new_block(n):
    """Create a new block"""
    sleep(0.25)
    i = number_empty_block(n)
    print (i)
    if i > 1:
        two_new_blocks(n)
    elif i == 1:
        one_new_block(n)
    control_end(n)
    set_pixels(n)


def number_empty_block(n):
    """Number of empty block"""
    L = L4 if n == 4 else L8
    i = 0
    for x in range(n):
        for y in range(n):
            if L[x][y] == 0:
                i = i + 1
    return i


def two_new_blocks(n):
    """Add two new blocks"""
    r = randint(0, 1)
    L = L4 if n == 4 else L8
    while r < 2:  # Tant qu'on en a pas créé 2
        x = randint(0, (n - 1))
        y = randint(0, (n - 1))
        # On choisis aléatoirement une ligne et une colonne
        if L[x][y] == 0:  # On controle si ce pixel est vide
            L[x][y] = 1
            # On défini un bloc de couleur correspondant au chiffre 2
            r = r + 1
# Si le bloc est créé on indente pour créé exactement 2 nouveaux pixels


def one_new_block(n):
    """Add only one block"""
    r = randint(0, 1)
    L = L4 if n == 4 else L8
    while r < 1:  # Tant qu'on en a pas créé 2
        x = randint(0, (n - 1))
        y = randint(0, (n - 1))
        # On choisis aléatoirement une ligne et une colonne
        if L[x][y] == 0:  # On controle si ce pixel est vide
            L[x][y] = 1
            # On défini un bloc de couleur correspondant au chiffre 2
            r = r + 1


def moved_up(n):
    """Reacts to the joystick pushed up."""
    print(L4)
    L = L4 if n == 4 else L8
    for x in range(n):
        for y in range(n):  # Sur chaque pixel en prenantles pixels en ligne puis en colonne
            if L[x][y] > 0 and y >= 1:  # On controle que le pixel ne soit pas une case vide
                move_pixel_up(x, y, n)
    set_pixels(n)
    print(L4)
    new_block(n)
    
def move_pixel_up(x, y, n):
    """Move up the pixel in the matrix"""
    L = L4 if n == 4 else L8
    while L[x][y - 1] == 0 and y >= 1:# Si la case est vide 
        L[x][y - 1] = L[x][y]
        L[x][y] = 0
        y = y - 1
    if L[x][y - 1] == L[x][y]:
        L[x][y - 1] = L[x][y - 1] + 1
        L[x][y] = 0
        
def moved_down(n):
    """Reacts to the joystick pushed down."""
    L = L4 if n == 4 else L8
    for x in range(n):
        for z in range(n - 1):
            y = n - 2 - z
            if L[x][y] > 0 and y <= (n - 2):# On controle que le pixel ne soit pas une case vide
                move_pixel_down(x, y, n)
    set_pixels(n)
    new_block(n)

def move_pixel_down(x, y, n):
    """Move down the pixel in the matrix"""
    L = L4 if n == 4 else L8
    while y <= (n - 2) and L[x][y + 1] == 0:# Si la case est vide
        L[x][y + 1] = L[x][y]
        L[x][y] = 0
        y = y + 1
    if y < (n - 1) and L[x][y + 1] == L[x][y]:
        L[x][y + 1] = L[x][y + 1] + 1
        L[x][y] = 0
                    
def moved_left(n):
    """Reacts to the joystick pushed left."""
    L = L4 if n == 4 else L8
    for y in range(n):
        for x in range(n):
            if L[x][y] > 0:# On controle que le pixel ne soit pas une case vide
                move_pixel_left(x, y, n)
    set_pixels(n)
    new_block(n)

def move_pixel_left(x, y, n):
    """Move left the pixel in the matrix"""
    L = L4 if n == 4 else L8
    while x > 0 and L[x - 1][y] == 0:# Si la case est vide 
        L[x - 1][y] = L[x][y]
        L[x][y] = 0
        x = x - 1
    if L[x - 1][y] == L[x][y]:
        L[x - 1][y] = L[x - 1][y] + 1
        L[x][y] = 0 
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f

def moved_right(n):
    """Reacts to the joystick pushed right."""
    L = L4 if n == 4 else L8
<<<<<<< HEAD
##    if a == 4:
##        L = L4
##    elif a == 8:
##        L = L8
    for y in range(n):
        for z in range(n-1):
            x=n-2-z
            if L[x][y] > 0 and x<(n-1):# On controle que le pixel ne soit pas une case vide
                while x<(n-1) and L[x+1][y] == 0:# Si la case est vide 
                    L[x+1][y]=L[x][y]
                    L[x][y]=0
                    x=x+1
                if x<(n-1) and L[x+1][y]==L[x][y]:
                   L[x+1][y]=L[x+1][y]+1
                   L[x][y]=0
    set_pixels(n)
    new_block(n)

def main():
    """Main loop to play the game."""
    startup()

    #-----Reactions du joystick-----
    running= True

    while running:
      for event in sense.stick.get_events():
          print(event, running)
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
                  running = False
    sense.clear()

# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    main()
=======
    for y in range(n):
        for z in range(n - 1):
            x = n - 2 - z
            if L[x][y] > 0 and x < (n - 1):
                move_pixel_right(x, y, n)
    set_pixels(n)
    new_block(n)

def move_pixel_right(x, y, n):
    """Move right the pixel in the matrix"""
    L = L4 if n == 4 else L8
    while x < (n - 1) and L[x + 1][y] == 0:
        L[x + 1][y] = L[x][y]
        L[x][y] = 0
        x = x + 1
    if x < (n - 1) and L[x + 1][y] == L[x][y]:
        L[x + 1][y] = L[x + 1][y] + 1
        L[x][y] = 0

def control_end(n):
    """Returns True when the game is finished."""
    global end
    end = True
    L = L4 if n == 4 else L8
    check_empty_cells(n)
    check_neigbors_cells_for_center(n)
    check_neigbors_cells_for_border(n)
    if end == True:
        end_animation(n)
    else:
        control_victory(n)
                    
def check_empty_cells(n):
    global end
    """Check if a cell is empty or not"""
    L = L4 if n == 4 else L8
    for x in range(n):
        for y in range(n):
            if L[x][y] == 0:
                end = False

def check_neigbors_cells_for_center(n):
    global end
    """Check the state of neighbours cells (only cells in the center)"""
    L = L4 if n == 4 else L8
    if end == True:
        for x in range(1, n - 1):
            for y in range(1, n - 1):
                if L[x][y] == L[x][y + 1] or L[x][y] == L[x + 1][y] \
                    or L[x][y] == L[x - 1][y] or L[x][y] == L[x][y - 1]:
                    end = False
            
def check_neigbors_cells_for_border(n):
    global end
    """Check the state of neighbours cells (only cells in the border)"""
    L = L4 if n == 4 else L8
    if end == True:
        for y in range(n - 1):
            for x in range(n - 1):
                if L[0][x] == L[0][x + 1] or L[x][0] == L[x + 1][0] \
                    or L[n - 1][x] == L[n - 1][x + 1] or L[x][n - 1] == L[x + 1][n - 1]:
                    end = False
            
def end_animation(n):
    """Show a message when the player loses the game and show the score"""
    loser_animation_part_1(n)
    score_calculator(n)
    sense.show_message('You lose... Your score is:', 0.075, MESSAGE)
    show = True
    show_score()
    main()
    
def loser_animation_part_1(n):
    """First animation of a game lost"""
    set_pixels(n)
    sleep(3)
    r = RED_7
    o = BLACK_0
    sense.clear()
    loser_animation_part_2(n)
    
def loser_animation_part_2(n):
    """Animation of a red cross when the game is over"""
    for i in range(5):
        sense.set_pixels(L_CROSS)
        sleep(0.1)
        sense.clear()
        sleep(0.1)
    sense.set_pixels(L_CROSS)
    sleep(1)
    set_pixels(n)
    sleep(2)
    
def score_calculator(n):
    """Calculate the score shown"""
    L = L4 if n == 4 else L8
    score = 0
    for x in range(n):
        for y in range(n):
            if L[x][y] != 0:
                score = score + 2 ** L[x][y]
                
def show_score():
    """Show the score"""
    while show:
        score = str(score)
        string = score + 'pts'
        sense.show_message(string, 0.1, MESSAGE)
        sense.show_message('Press to end', 0.075, MESSAGE)
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                show = False
                
def exit():
    """Use to exit the game"""
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
                            
def control_victory(n):
    """Control if the maximum is reached (14th block)"""
    L = L4 if n == 4 else L8
    for x in range(n):
        for y in range(n):
            if L[x][y] == 14:
                sense.set_pixels(L_WIN)
                victory(n)
    set_pixels(n)
    
        
def victory(n):
    """Show the message when the player wins"""
    sleep(9)
    score_calculator(n)
    sense.show_message('Congratulations, you just reached the highest block. Your score is :', 0.075, MESSAGE)
    show_score
    main()
    
def joystick_direction():
    """Definition of direction"""
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
    
#-----Reactions du joystick-----
    
def main():
    """Main menu"""
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

>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
