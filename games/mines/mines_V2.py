# File: Mines Game
# Autors: Fabian Roulin and Mirko Pirona
# Date: 8.01.2019

#############################################
#             Mines and weeper:             #
#############################################
"""
Minesweeper is a single-player puzzle video game.
The objective of the game is to clear a rectangular
board containing hidden "mines" or bombs without
detonating any of them, with help from clues about
the number of neighboring mines in each field. The
game originates from the 1960s, and has been written
for many computing platforms in use today. It has many
variations and offshoots. Minesweeper is a single-player
video game.

https://en.wikipedia.org/wiki/Minesweeper_(video_game)
"""
#############################################
#       Import the different modules        #
#############################################

# Import the library "Sensehat"
from sense_emu import SenseHat

from random import randint, choice
from time import sleep, time

#############################################
#     Definition of the game variables      #
#############################################

# Definition of the colors of the game:
GREEN = (0, 255, 0)       # Flag
GREY = (90, 94, 107)      # Box undiscoveRED
WHITE = (255, 255, 255)   # Box without bomb
YELLOW = (247, 255, 60)   # 1 bomb around
ORANGE = (255, 127, 0)    # 2 bombs around
CORAIL = (231, 62, 1)     # 3 bombs around
RED = (248, 0, 0)         # 4 bombs around
BORDEAU = (91, 60, 19)    # 5 bombs around
BLACK = (0, 0, 0)         # Bomb

COLORS = [GREEN, GREY, WHITE, YELLOW, ORANGE, CORAIL, RED, BORDEAU, BLACK]

# Initialization of the module "sense hat" in the variable "sense":
sense = SenseHat()
sense.clear()

#############################################
#    Initialization of golbal variables     #
#############################################

# The variable containing the flags list:
flags = []

# The variable containing the bombs list:
bombs = []

# The variable containing the checked boxes:
checks = []

# The variable containing the number of bombs:
nb_bombs = 7

# Displacement variables:
game = True
running = True
x = 0
y = 0

# Color of the board:
old_color = COLORS[1]

#############################################
#     Definition of the game functions      #
#############################################

# Functions that count the number of bomb around:
def count_bombs_around(x, y):
    """ This function analyse the number of bombs around a case and return this number. """
    global bombs
    nb = 0
    
    x_check = x + 1
    y_check = y
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
        
    x_check = x
    y_check = y + 1
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
        
    x_check = x + 1
    y_check = y + 1
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
        
    x_check = x - 1
    y_check = y
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
    
    x_check = x
    y_check = y - 1
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
    
    x_check = x - 1
    y_check = y - 1
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
    
    x_check = x + 1
    y_check = y - 1
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
        
    x_check = x - 1
    y_check = y + 1
    xy_ckeck = 10 * x_check + y_check
    
    if xy_ckeck in bombs:
        nb += 1
    
    return nb;

# Function that choose the places of the bombs:
def choose_bomb(nb_bomb):
    """ This function takes as an argument the number of bombs and it place the bombs on the game board. """
    bombs = []
    
    i = 0
    while i < nb_bomb :
        x_bomb = randint(0, 7)
        y_bomb = randint(0, 7)
        xy_bomb = 10 * x_bomb + y_bomb
        if(xy_bomb in bombs):
            i = i
            
        else:
            i += 1
            bombs.append(xy_bomb)

    return bombs;

# Initialization of game board:
def set_all_in_gray():
    """ This function initialize the game board with the grey color. """
    G = COLORS[1]

    set_color_grey = [
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G]

    sense.set_pixels(set_color_grey)

# Function that color the box during the spread
def color_case(list):
    """ This function take a list of case as argument and color all this cases with the good color. """
    i = 0
    while i < len(list):
        y = list[i] % 10
        x = int((list[i] - y) / 10)
        i += 1
        print(x)
        print(y)
        
        nb = count_bombs_around(x, y)
        
        if -1 < x < 8 and -1 < y < 8:
            if nb == 0:
                sense.set_pixel(x, y, COLORS[2])
                
            elif nb == 1:
                sense.set_pixel(x, y, COLORS[3])
                
            elif nb == 2:
                sense.set_pixel(x, y, COLORS[4])
                
            elif nb == 3:
                sense.set_pixel(x, y, COLORS[5])
                
            elif nb == 4:
                sense.set_pixel(x, y, COLORS[6])
                
            elif nb == 5:
                sense.set_pixel(x, y, COLORS[7])
                
            else:
                sense.set_pixel(x, y, COLORS[8])


def check_case(x, y):
    """ This function create the list of the case concerned by spread. """
    global checks
    if ((x + 1) * 10 + y) not in checks:
        if count_bombs_around(x + 1, y) == 0 and -1 < (x + 1) < 8 and -1 < y < 8:
            checks.append((x + 1) * 10 + y)
            check_case(x + 1, y)
            
        else:
            checks.append((x + 1) * 10 + y)
 
    
    if ((x + 1) * 10 + y + 1) not in checks:
        if count_bombs_around(x + 1, y + 1) == 0 and -1 < (x + 1) < 8 and -1 < (y + 1) < 8:
            checks.append((x + 1) * 10 + (y + 1))
            check_case(x + 1, y + 1)
            
        else:
            checks.append((x + 1) * 10 + (y + 1))
    
    if (x * 10 + y + 1) not in checks:
        if count_bombs_around(x, y + 1) == 0 and -1 < x < 8 and -1 < (y + 1) < 8:
            checks.append(x * 10 + (y + 1))
            check_case(x, y + 1)
            
        else:
            checks.append(x * 10 + (y + 1))
            
    if ((x - 1) * 10 + y + 1) not in checks:
        if count_bombs_around(x - 1, y + 1) == 0 and -1 < (x - 1)<8 and -1 < (y + 1)<8:
            checks.append((x - 1) * 10 + (y + 1))
            check_case(x - 1, y + 1)
            
        else:
            checks.append((x - 1) * 10 + (y + 1))
        
    if ((x - 1) * 10 + y) not in checks:
        if count_bombs_around(x - 1, y) == 0 and -1 < (x - 1) < 8 and -1 < y < 8:
            checks.append((x - 1) * 10 + y)
            check_case(x - 1, y)
            
        else:
            checks.append((x - 1) * 10 + y)
        
    if ((x - 1) * 10 + y - 1) not in checks:
        if count_bombs_around(x - 1, y - 1) == 0 and -1 < (x - 1)< 8 and -1 < (y - 1) < 8:
            checks.append((x - 1) * 10 + (y - 1))
            check_case(x - 1, y - 1)
            
        else:
            checks.append((x - 1) * 10 + (y - 1))
        
    if (x * 10 + y - 1) not in checks:
        if count_bombs_around(x, y - 1) == 0 and -1 < x < 8 and -1 < (y - 1) < 8:
            checks.append(x * 10 + (y - 1))
            check_case(x, y - 1)
            
        else:
            checks.append(x*10+(y-1))
        
    if ((x + 1) * 10 + y - 1) not in checks:
        if count_bombs_around(x + 1, y - 1) == 0 and -1 < (x + 1) < 8 and -1 < (y - 1) < 8:
            checks.append((x + 1) * 10 + (y - 1))
            check_case(x + 1, y - 1)
            
        else:
            checks.append((x + 1) * 10 + (y - 1))
            
    return checks;

def help():
    """
    This function can help the player to play this game.
    List of the game functions:
    
    help
    count_bombs_around
    choose_bomb
    set_all_in_gray
    color_case
    check_case
    new_game
    end_game
    use_case
    
    """
    return;

# Function that start a new game:
def new_game(nb):
    """ This function initialize all the game vriables when the game start or restart. """
    # Importation of the external variable that will contain the bombs list
    global bombs
    
    # Random placement of bombs
    bombs = choose_bomb(nb)
    
    print(bombs)
    
    # Initialization of the game board
    set_all_in_gray()
    
    # Initialization of deplacement variables
    global x
    global y
    
    x = 0
    y = 0

# Function that check for every action if the game is over:
def end_game():
    """ This function check if the game is over. If it's true, it show a message. """
    x = -1
    y = -1
    nb = 0
    
    for i in range(8):
        x += 1
        for j in range(8):
            y += 1
            if sense.get_pixel(x, y) == [88, 92, 104]:
                nb += 1
        y = -1
        
    if nb == nb_bombs:
        sense.show_message("You won")
        # Restarting the game:
        new_game(nb_bombs)

def use_case(x, y):
""" This function performs the action on the selected cell. """
    global bombs
    
    xy = x * 10 + y
    
    if sense.get_pixel(x, y) == [88, 92, 104]:
        # Checking if it is a bomb :
        if xy in bombs and xy not in flags:
            sense.clear(255, 0, 0)
            sleep(5)
            # Restarting the game:
            new_game(nb_bombs)
            
        else:
            # If there is no bomb around, the spread start :
            if count_bombs_around(x, y) == 0:
                list_case_checked = check_case(x, y)
                
            else:
                xy = x * 10 + y
                list_case_checked = [xy]
            # After the end of the spread, setting a color to all the boxes
            color_case(list_case_checked)
            # At the end of use_case reset the list for the next use :
            checks = []           
            # At the end of use_case check if the game is over
            end_game()            

#############################################
#            Start of the game              #
#############################################

# Calling of the function game start:
new_game(nb_bombs)

def main():
    # Core of the game that manages the deplacement with joystick:
    global x,y, flags, old_color, COLORS, running
    while game:
        while running:
            for event in sense.stick.get_events():         
                if event.action == 'held' and event.direction == 'middle':   
                    xy_flag = x * 10 + y
                    if xy_flag not in flags:
                        flags.append(xy_flag)
                        sense.set_pixel(x, y, COLORS[0])
                        
                    else:
                         flags.remove(xy_flag)
                        
                if event.action == 'pressed':
                    sense.set_pixel(x, y, old_color)
                    if event.direction == 'down' and y < 7: 
                        y += 1
                        old_color = sense.get_pixel(x, y)
                        
                    elif event.direction == 'up' and y > 0:
                        y -= 1
                        old_color = sense.get_pixel(x, y)
                        
                    elif event.direction == 'right' and x < 7:
                        x += 1
                        old_color = sense.get_pixel(x, y)
                        
                    elif event.direction == 'left' and x > 0:
                        x -= 1
                        old_color = sense.get_pixel(x, y)
                        
                    elif event.direction == 'middle':
                        use_case(x, y)
                        running = False
                        
            if running:        
                # Blinking creation :
                t = int(3 * time())
                if t % 2 == 0:
                    sense.set_pixel(x, y, old_color)
                    
                else:
                    sense.set_pixel(x, y, COLORS[0])
            
        if not running:
            for event in sense.stick.get_events():
                if event.action == 'pressed':
                    if event.direction == 'down' or event.direction == 'up' or event.direction == 'right' or event.direction == 'left':
                        running = True
                        
                        if event.direction == 'down' and y < 7:
                            y += 1
                            
                        elif event.direction == 'up' and y > 0:
                            y -= 1
                            
                        elif event.direction == 'right' and x < 7:
                            x += 1
                            
                        elif event.direction == 'left' and x > 0:
                            x -= 1
                        
# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    
    main()