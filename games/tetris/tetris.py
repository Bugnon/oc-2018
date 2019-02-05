"""
File : Tetris game on the Raspberry PI
Authors : Valentin Piquerez & Hugo Ducommun
Date : January 2019
---------------------------------
Move your shape with right/left button.
Rotate it with the middle button.
Complete a line to increase your score.
More infos : https://tetris.fandom.com/wiki/Tetris_Guideline
Good luck !
"""

from sense_hat import SenseHat
from time import sleep, time
from random import randint, choice
from gamelib import *

### Variables definition ###

color = (0, 0, 0)
state = 1  # When game is static: state = 0. When game is playing, state = 1.
game = 1  # If game = 1, the game doesn't stop. If game = 0, it's game over.
sense = SenseHat()

dx = 0  # Variable to move left and right on x axis
dy = 0  # Variable to move downwards on Y axis
dt = 1  # Time between each drop

score = 0

### Shapes definition in matrixes ###

# cyan horizontal or vertical bar
I = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
    ]

# red L
L = [
    [1, 0],
    [1, 1]
    ]

# 2x2 yellow square
o = [
    [1, 1],
    [1, 1]
    ]

shapes = (I, L, o)  # List with the three shapes

P = choice(shapes)

if P == L:  # Assign the right color tot he right shape
    color = RED
elif P == I:
    color = CYAN
else:
    color = YELLOW

### Functions definition ###


def delete_lines(i):
    """ Delete completed lines and move every line above one tile downward. """
    for k in range(8):
        sense.set_pixel(k, 7-i, BLACK)
    for c in reversed(range(7-i)):
        for d in range(8):
            sense.set_pixel(d, c+1, (sense.get_pixel(d, c)))
            sense.set_pixel(d, c, BLACK)

def check_if_lines_are_completed():
    """ Check if lines are completed to delete them and increase the score. """
    global score
    for g in range(8):
                for i in range(8):
                    a = 0
                    for j in range(8):
                        if sense.get_pixel(7-j, 7-i) != [0, 0, 0]:
                            a += 1
                            if a == 8:
                                score += 1 # Inscrease the score if the line is completed
                                delete_lines(i)


def print_matrix(M):
    """Print the tetris shape at the top in the middle."""
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x] == 1:
                sense.set_pixel(3+x, y, color)


def delete_matrix_when_down(M, dx, dy):
    """Delete the actual shape when it's moving down."""
    n = len(M)
    for y in range(n):  # Set every pixel of the matrix black
            for x in range(n):
                if 0 <= y+dy <= 7:
                    if M[y][x] == 1:
                        sense.set_pixel(3+x+dx, y+dy, BLACK) 
                elif M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and y+dy == 8:  # Delete horizontal bar when it's at bottom.
                    if M[y][x] == 1:
                        sense.set_pixel(3+x+dx, y+dy, BLACK)
                else:
                    dy -= 1  # If it can't delete the shape, we put dy at same value as before
                
def print_matrix_down(M):
    """Move shape down for 1 tile."""
    global dx, dy
    dy += 1  # Move the matrix one tile downward
    n = len(M)
    delete_matrix_when_down(M, dx, dy-1)
    for y in range(n):  # Print new matrix one tile downward
        for x in range(n):
            if 0 <= y+dy <= 7:   
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx, y+dy, color)
            elif M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and y+dy == 8:
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx, y+dy, color)
            else:
                state = 0
 
def print_new_matix_when_left(M, dx, dy, n):
    """Print a new matrix moved to the left."""
    for y in range(n):  # Print the new matrix one tile leftward
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx, y+dy, color)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == -1:
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx, y+dy, color)

def print_matrix_left(M):
    """ Move shape left for 1 tile. """
    global dx, dy
    dx -= 1
    n = len(M)
    for y in range(n):  # Stop the shape when it's against another one
        if M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and -1 <= 3+dx <= 7:
            if M[y][1] == 1 and sense.get_pixel(3+dx+1, y+dy)!=[0, 0, 0]:
                dx += 1
                return ;
        elif 0 <= 3+dx <= 7:
            if M[y][0] == 1 and sense.get_pixel(3+dx, y+dy) != [0, 0, 0]:
                dx += 1
                return ;

    for y in range(n):  # Set the pixel of the actual matrix to black (delete it)
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx+1, y+dy, BLACK)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == -1: # If the 'I' is vertical, it can move one more tile.
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx+1, y+dy, BLACK)
            else:
                dx +=  1
    print_new_matix_when_left(M, dx, dy, n)

def print_new_matix_when_right(M, dx, dy, n):
    """ Print a new matrix moved to the right. """
    for y in range(n):  # Print the new matrix one tile rightward
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx, y+dy, color)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == 8:
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx, y+dy, color)

def print_matrix_right(M):
    """ Move shape right for 1 tile. """
    global dx, dy
    dx += 1
    n = len(M)
    for y in range(n):  # Stop the shape when it's against another one
            if M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and -1 <= 3+dx <= 6:
                if M[y][1] == 1 and sense.get_pixel(3+dx+1, y+dy) != [0, 0, 0]:
                    dx -= 1
                    return ;
            if M == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and -1 <= 3+dx <= 5:
                if M[y][2] == 1 and sense.get_pixel(3+dx+2, y+dy) != [0, 0, 0]:
                    dx -= 1
                    return ;
            elif 0 <= 3+dx <= 6:
                if M[y][1] == 1 and sense.get_pixel(3+dx+1, y+dy) != [0, 0, 0]:
                    dx -= 1
                    return ;

    for y in range(n):  # Set the pixel of the actual matrix to black (delete it)
        for x in range(n):
            if 0 <= 3+x+dx <= 7:
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx-1, y+dy, BLACK)
            elif M == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and 3+x+dx == 8: # If the 'I' is vertical, it can move one more tile.
                if M[y][x] == 1:
                    sense.set_pixel(3+x+dx-1, y+dy, BLACK)
            else:
                dx -= 1            
    print_new_matix_when_right(M, dx, dy, n)

def print_rotated_matrix(n, matrix):
    """ Print the matrix after the rotation. """
    for y in range(n): 
        for x in range(n):
            if matrix[y][x] == 1:
                sense.set_pixel(3+x+dx, y+dy, color)

def rotate_90(matrix):
    """ Turn the shape 90 degrees right. """
    delete_matrix_when_down(matrix, dx, dy)
    n = len(matrix)
    for layer in range((n + 1) // 2):  # Rotate the matrix (borrowed on internet)
        for index in range(layer, n-1-layer, 1):
            matrix[layer][index], matrix[n-1-index][layer], \
                matrix[index][n-1-layer], matrix[n-1-layer][n-1-index] = \
                matrix[n-1-index][layer], matrix[n-1-layer][n-1-index], \
                matrix[layer][index], matrix[index][n-1-layer]
    print_rotated_matrix(n, matrix)
    return matrix

def main():
    """ The core of the game. """
    global x, y, dx, dy, color, score
    
    sense.clear()
    
    P = choice(shapes)
    
    if P == L:
        color = RED
    elif P == I:
        color = CYAN
    else:
        color = YELLOW
    
    t0 = time()
    
    game = 1
    
    state = 1
    
    print_matrix(P)
    
    while game == 1:
        while state == 1:
            for event in sense.stick.get_events():
                if event.action == 'pressed' and event.direction == 'middle':
                    if P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]:
                        if dx == -4 or dx == 3:
                            pass  # The vertical 'I' can not rotate when it's in the ribbs
                        elif sense.get_pixel(3+dx, dy+1) != [0, 0, 0] or sense.get_pixel(3+dx+2, dy+1) != [0, 0, 0]:
                            pass
                        else:
                            rotate_90(P)
                    elif P == [[0, 0, 0], [1, 1, 1], [0, 0, 0]]:
                        if dy == 6:
                            pass  # The horizontal 'I' can not rotate when it's at the bottom
                        else:
                            rotate_90(P)
                    else:
                        rotate_90(P)
                 elif event.direction == 'down' and event.action == 'pressed':
                    print_matrix_down(P)
                 elif event.direction == 'left' and event.action == 'pressed':
                    print_matrix_left(P)
                 elif event.direction == 'right' and event.action == 'pressed':
                    print_matrix_right(P)
                 elif event.direction == 'up' and event.action == 'held':
                     game = 0
                     state = 0

            if P == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] and dy == 6:  # If the shape is at the bottom we turn the game on static
                state=0
            elif P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and dy == 5:
                state=0
            elif P == o and dy == 6:
                state=0
            elif P == L and dy == 6:
                state=0
        
            n=len(P)
            for x in range(n):  # Check if the shape can drop
                if P == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] and dy < 5:
                    if sense.get_pixel(dx+4, dy+3) != [0, 0, 0]:
                        if dy == 0:
                            game = 0
                        state = 0
                elif dy < 6 and P != [[0, 1, 0], [0, 1, 0], [0, 1, 0]]:
                    if P[1][x] == 1 and sense.get_pixel(x+dx+3, dy+2) != [0, 0, 0]:
                        if dy == 0:  # If the shape is blocked just after spawning, game over
                            game = 0
                        state = 0
                        
            Lcomplet = 0  # Check if the shape 'L' is completed by another external pixel, if yes the game is set on static
            for x in range (n):
                for y in range(n):
                    if P == [[1, 1],[0, 1]] or P == [[1, 1],[1, 0]]:
                        if sense.get_pixel(x+dx+3, y+dy) != [0, 0, 0]:
                            Lcomplet += 1
                        if Lcomplet == 4:
                            state = 0
            
            t = time()  # Every second, moves the shape one tile downward
            if t > t0 + dt:
                print_matrix_down(P)
                t0 = t


        while state == 0:

            check_if_lines_are_completed()
                                        
            P = choice(shapes)  # Pick randomly a shape for one round
            
            if P == L:
                color = RED
            elif P == I:
                color = CYAN
            else:
                color = YELLOW
                
            t0 = time()
            
            dx = 0  # Set back the position where we print the matrix to original settings
            dy = 0

            print_matrix(P)

            if game == 0:  # When game is over, displays the score
                sense.show_message('Game over ! Score :', scroll_speed=0.05)
                sense.show_message(str(score), scroll_speed=0.2)
                t0 = time()
                active = True
                while active: # Play again
                    sense.show_letter('?')
                    for event in sense.stick.get_events():
                        if event.direction == 'middle' and event.action == 'pressed':
                            game = 1
                            active = False
                            sense.clear()
                            score = 0
                            main()
                    t = time()
                    if t > t0 + 3: # After 3 seconds if the player did nothing or press another button, leave the program
                        sense.clear()
                        return ;
            else:
                state = 1


# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    main()