<<<<<<< HEAD
#Author: Mirko Pirona
##Mines
##Date

import random

class Cell(object):
    def __init__(self, is_mine, is_visible=False, is_flagged=False):
        self.is_mine = is_mine
        self.is_visible = is_visible
        self.is_flagged = is_flagged

    def show(self):
        self.is_visible = True

    def flag(self):
        self.is_flagged = not self.is_flagged

    def place_mine(self):
        self.is_mine = True


class Board(tuple):
    def __init__(self, tup):
        super().__init__()
        self.is_playing = True

    def __str__(self):
        board_string = ("Mines: " + str(self.remaining_mines) + "\n  " +
                        "".join([str(i) for i in range(len(self))]))
        for (row_id, row) in enumerate(self):
            board_string += "\n" + str(row_id) + " "
            for (col_id, cell) in enumerate(row):
                if cell.is_visible:
                    if cell.is_mine:
                        board_string += "M"
                    else:
                        board_string += str(self.count_surrounding(row_id,
                                                                   col_id))
                elif cell.is_flagged:
                        board_string += "F"
                else:
                    board_string += "X"
            board_string += " " + str(row_id)
        board_string += "\n  " + "".join([str(i) for i in range(len(self))])
        return board_string

    def show(self, row_id, col_id):
        if not self[row_id][col_id].is_visible:
            self[row_id][col_id].show()

            if (self[row_id][col_id].is_mine and not
                self[row_id][col_id].is_flagged):
                self.is_playing = False

            elif self.count_surrounding(row_id, col_id) == 0:
                [self.show(surr_row, surr_col) for (surr_row, surr_col) in
                 self.get_neighbours(row_id, col_id) if
                 self.is_in_range(surr_row, surr_col)]

    def flag(self, row_id, col_id):
        if not self[row_id][col_id].is_visible:
            self[row_id][col_id].flag()
        else:
            print("Cannot add flag, cell already visible.")

    def place_mine(self, row_id, col_id):
        self[row_id][col_id].place_mine()

    def count_surrounding(self, row_id, col_id):
        count = 0
        for (surr_row, surr_col) in self.get_neighbours(row_id, col_id):
            if (self.is_in_range(surr_row, surr_col) and
                self[surr_row][surr_col].is_mine):
                count += 1
        return count

    def get_neighbours(self, row_id, col_id):
        SURROUNDING = ((-1, -1), (-1,  0), (-1,  1),
                       (0 , -1),           (0 ,  1),
                       (1 , -1), (1 ,  0), (1 ,  1))
        neighbours = []
        for (surr_row, surr_col) in SURROUNDING:
            neighbours.append((row_id + surr_row, col_id + surr_col))
        return neighbours

    def is_in_range(self, row_id, col_id):
        return 0 <= row_id < len(self) and 0 <= col_id < len(self)

    @property
    def remaining_mines(self):
        remaining = 0
        for row in self:
            for cell in row:
                if cell.is_mine:
                    remaining += 1
                if cell.is_flagged:
                    remaining -= 1
        return remaining

    @property
    def is_solved(self):
        for row in self:
            for cell in row:
                if not(cell.is_visible or cell.is_flagged):
                    return False
        return True


def create_board(size, mines):
    board = Board(tuple([tuple([Cell(False) for i in range(size)])
                         for j in range(size)]))
    available_pos = list(range((size-1) * (size-1)))
    for i in range(mines):
        new_pos = random.choice(available_pos)
        available_pos.remove(new_pos)
        (row_id, col_id) = (new_pos % 9, new_pos // 9)
        board.place_mine(row_id, col_id)
    return board

def get_move(board):
    INSTRUCTIONS = ("First, enter the column, followed by the row. To add or "
                    "remove a flag, add \"f\" after the row (for example, 64f "
                    "would place a flag on the 6th column, 4th row). Enter "
                    "your move: ")

    move = input("Enter your move (for help enter \"H\"): ")
    if move == "H":
        move = input(INSTRUCTIONS)

    while not is_valid(move, board):
        move = input("Invalid input. Enter your move (for help enter \"H\"): ")
        if move == "H":
            move = input(INSTRUCTIONS)

    return (int(move[1]), int(move[0]), True if move[-1] == "f" else False)

def is_valid(move_input, board):
    if move_input == "H" or (len(move_input) not in (2, 3) or
                             not move_input[:1].isdigit() or
                             int(move_input[0]) not in range(len(board)) or
                             int(move_input[1]) not in range(len(board))):
        return False

    if len(move_input) == 3 and move_input[2] != "f":
        return False

    return True

def main():
    SIZE = 10
    MINES = 9
    board = create_board(SIZE, MINES)
    print(board)
    while board.is_playing and not board.is_solved:
        (row_id, col_id, is_flag) = get_move(board)
        if not is_flag:
            board.show(row_id, col_id)
        else:
            board.flag(row_id, col_id)
        print(board)

    if board.is_solved:
        print("Well done! You solved the board!")
    else:
        print("Uh oh! You blew up!")

if __name__ == "__main__":
=======
# File: Mines Game
# Autors: Fabian Roulin and Mirko Pirona
# Date: 8.01.2019

#############################################
#      We import the different modules      #
#############################################

# We import the library "Sensehat"
from sense_emu import SenseHat

# We import the module "random"
from random import randint, choice

# We import the module "time"
from time import sleep, time

#############################################
#     Definition of the game variables      #
#############################################

# We define the colors of the game:
green = (0,255,0)       # Flag
grey = (90,94,107)      # Box undiscovered
white = (255,255,255)   # Box without bomb
yellow = (247,255,60)   # 1 bomb around
orange = (255,127,0)    # 2 bombs around
corail = (231,62,1)     # 3 bombs around
red = (248,0,0)         # 4 bombs around
bordeau = (91,60,19)    # 5 bombs around
black = (0,0,0)         # Bomb

# We initialize the module "sense hat" in the variable "sense":
sense = SenseHat()
sense.clear()

#############################################
#    Initialization of golbal variables     #
#############################################

# The variable containing the flags list:
list_flag = []

# The variable containing the bombs list:
List_bomb = []

# The variable containing the checked boxes:
list_checked = []

# The variable containing the number of bombs:
nb_bombs = 7

# Displacement variables:
game = True
running = True
x = 0
y = 0

# Color of the board:
old_color = grey

#############################################
#     Definition of the game functions      #
#############################################

# Functions that count the number of bomb around:
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

# Function that choose the places of the bombs:
def choose_bomb(nb_bomb):
  
    list_bomb = []
    
    i = 0
    while i < nb_bomb :
        x_bomb = randint(0,7)
        y_bomb = randint(0,7)
        xy_bomb = 10 * x_bomb + y_bomb
        if(xy_bomb in list_bomb):
            i = i
        else:
            i += 1
            list_bomb.append(xy_bomb)

    return list_bomb;

# Initialization of game board:
def set_all_in_gray():
    G = grey

    set_color_grey = [
    G,G,G,G,G,G,G,G,
    G,G,G,G,G,G,G,G,
    G,G,G,G,G,G,G,G,
    G,G,G,G,G,G,G,G,
    G,G,G,G,G,G,G,G,
    G,G,G,G,G,G,G,G,
    G,G,G,G,G,G,G,G,
    G,G,G,G,G,G,G,G]

    sense.set_pixels(set_color_grey)

# Function that color the box during the spread
def color_case(list):
    
    i = 0
    while i < len(list):
        y = list[i] % 10
        x = int((list[i] - y) / 10)
        i += 1
        print(x)
        print(y)
        
        nb = count_bombs_around(x,y)
        
        if -1 < x < 8 and -1 < y < 8:
            if nb == 0:
                sense.set_pixel(x,y,white)
            elif nb == 1:
                sense.set_pixel(x,y,yellow)
            elif nb == 2:
                sense.set_pixel(x,y,orange)
            elif nb == 3:
                sense.set_pixel(x,y,corail)
            elif nb == 4:
                sense.set_pixel(x,y,red)
            elif nb == 5:
                sense.set_pixel(x,y,bordeau)
            else:
                sense.set_pixel(x,y,black)


def check_case(x,y):
    global list_checked
    
    if ((x + 1)*10 + y) not in list_checked:
        if count_bombs_around(x + 1,y) == 0 and -1 < (x + 1) < 8 and -1 < y < 8:
            list_checked.append((x + 1)*10 + y)
            check_case(x + 1,y)
        else:
            list_checked.append((x + 1)*10 + y)
 
    
    if ((x + 1)*10 + y + 1) not in list_checked:
        if count_bombs_around(x + 1,y + 1) == 0 and -1 < (x + 1) < 8 and -1 < (y + 1) < 8:
            list_checked.append((x + 1) * 10 + (y + 1))
            check_case(x + 1,y + 1)
        else:
            list_checked.append((x + 1) * 10 + (y + 1))
    
    if (x * 10 + y + 1) not in list_checked:
        if count_bombs_around(x,y + 1) == 0 and -1 < x < 8 and -1 < (y + 1) < 8:
            list_checked.append(x * 10 + (y + 1))
            check_case(x,y + 1)
        else:
            list_checked.append(x * 10 + (y + 1))
            
    if ((x - 1) * 10 + y + 1) not in list_checked:
        if count_bombs_around(x - 1,y + 1) == 0 and -1 < (x - 1)<8 and -1 < (y + 1)<8:
            list_checked.append((x - 1) * 10 + (y + 1))
            check_case(x - 1,y + 1)
        else:
            list_checked.append((x - 1) * 10 + (y + 1))
        
    if ((x - 1) * 10 + y) not in list_checked:
        if count_bombs_around(x - 1,y) == 0 and -1 < (x - 1) < 8 and -1 < y < 8:
            list_checked.append((x - 1) * 10 + y)
            check_case(x - 1,y)
        else:
            list_checked.append((x - 1) * 10 + y)
        
    if ((x - 1) * 10 + y - 1) not in list_checked:
        if count_bombs_around(x - 1,y - 1) == 0 and -1 < (x - 1)< 8 and -1 < (y - 1) < 8:
            list_checked.append((x - 1) * 10 + (y - 1))
            check_case(x - 1,y - 1)
        else:
            list_checked.append((x - 1) * 10 + (y - 1))
        
    if (x * 10 + y - 1) not in list_checked:
        if count_bombs_around(x,y - 1) == 0 and -1 < x < 8 and -1 < (y - 1) < 8:
            list_checked.append(x * 10 + (y - 1))
            check_case(x,y - 1)
        else:
            list_checked.append(x*10+(y-1))
        
    if ((x + 1) * 10 + y - 1) not in list_checked:
        if count_bombs_around(x + 1,y - 1) == 0 and -1 < (x + 1) < 8 and -1 < (y - 1) < 8:
            list_checked.append((x + 1) * 10 + (y - 1))
            check_case(x + 1,y - 1)
        else:
            list_checked.append((x + 1) * 10 + (y - 1))
            
    return list_checked;

# Function that start a new game:
def new_game(nb):
    
    # We select the external variable that will contain the bombs list
    global List_bomb
    
    # Random placement of bombs
    List_bomb = choose_bomb(nb)
    
    print(List_bomb)
    
    # We initialize the game board
    set_all_in_gray()
    

    # Initialization of deplacement variables
    global x
    global y
    
    x = 0
    y = 0

# Function that check for every action if the game is over:
def end_game():
    
    x = -1
    y = -1
    nb = 0
    
    for i in range(8):
        x += 1
        for j in range(8):
            y += 1
            if sense.get_pixel(x,y) == [88,92,104]:
                nb += 1
        y = -1
        
    if nb == nb_bombs:
        sense.show_message("You won")
        # We restart the game:
        new_game(nb_bombs)

# Function that performs the action on the selected cell:
def use_case(x,y):

    global List_bomb
    
    xy = x * 10 + y
    
    if sense.get_pixel(x,y) == [88,92,104]:
        # We check if it is a bomb :
        if xy in List_bomb and xy not in list_flag:
            sense.clear(255,0,0)
            sleep(5)
            # We restart the game:
            new_game(nb_bombs)
        else:
            # If there is no bomb around, we start the spread :
            if count_bombs_around(x,y) == 0:
                list_case_checked = check_case(x,y)
            else:
                xy = x * 10 + y
                list_case_checked = [xy]
            # After the end of the spread, we set a color to all the boxes
            color_case(list_case_checked)
            # At the end of use_case we reset the list for the next use :
            list_checked = []           
                
            # At the end of use_case we check if the game is over
            end_game()            

#############################################
#            Start of the game              #
#############################################

# We use the function of game start:
new_game(nb_bombs)

# Part that manages the deplacement with joystick:
while game:
    while running:
        for event in sense.stick.get_events():         
            if event.action == 'held' and event.direction == 'middle':   
                xy_flag = x * 10 + y
                if xy_flag not in list_flag:
                    list_flag.append(xy_flag)
                    sense.set_pixel(x,y,green)
                else:
                     list_flag.remove(xy_flag)
                    
            if event.action == 'pressed':
                sense.set_pixel(x,y,old_color)
                if event.direction == 'down' and y < 7: 
                    y = y + 1
                    old_color = sense.get_pixel(x,y)     
                elif event.direction == 'up' and y > 0:
                    y = y - 1
                    old_color = sense.get_pixel(x,y)    
                elif event.direction == 'right' and x < 7:
                    x = x + 1
                    old_color = sense.get_pixel(x,y)  
                elif event.direction == 'left' and x > 0:
                    x = x - 1
                    old_color = sense.get_pixel(x,y) 
                elif event.direction == 'middle':
                    use_case(x,y)
                    running = False
                    
        if running == True:        
            # On crée le clignotement :
            t = int(3 * time())
            if t % 2 == 0:
                sense.set_pixel(x,y,old_color)
            else:
                sense.set_pixel(x,y,green)
        
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
                        

if __name__ == '__main__':
    
    main()
if __name__ == '__main__':
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    main()