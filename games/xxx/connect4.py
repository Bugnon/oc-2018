"""
File: connect4.py
Date: 2019.02.04

Authors : Nissa and Terence

Connect 4
The goal is to place 4 discs in a row
"""


from sense_hat import SenseHat
#from sense_emu import SenseHat
from time import sleep, time
from gamelib import *

sense = SenseHat()
#sense.set_rotation(180)

repeat=1 #Repeats the program if launched as standalone
playerScore=[0,0] #Score of the players
turns=0 #Amount of turns passed
gameOver=0 #Is the game over?
stopGame=0 #=1 makes main() stop the game

#Creates two lists of 4 pixels to make winning streaks detection easier
fourYellow=[[248, 252, 0]]*4
fourRed=[[248, 0, 0]]*4

state =[[0] * 8] * 7 #Creates a list of 8*8 blank pixels for the default display

#Puts BLUE, RED and YELLOW from gamelib into a list
colors=(BLUE, RED, YELLOW)

def main():
    """
    Main function, initialises the game, starts it, and stops it when needed.
    """
    global gameOver
    global playerScore
    global stopGame
    global turns
    turns=0 #Resets the turns passed
    #Stops the game if a player has 2 points or if stop_game() set stopGame to 1
    #and the game is supposed to stop now
    if (playerScore[0]==2 or playerScore[1]==2 or stopGame==1) and repeat==0:
        stopGame=0 #Resets stopGame
        gameOver=0 #Resets gameOver
        return
    #If the game should continue, resets gameOver and playerScore to 0
    else:
        gameOver=0 #Resets gameOver
        if playerScore[0]==2 or playerScore[1]==2 or stopGame==1:
            stopGame=0 #Resets stopGame
            playerScore=[0,0] #Resets the playerScore
        show() #Resets the display for a new game
        turn() #Starts a new turn

def show():
    """
    Sets up the playing field : 6*7 blue pixels
    """
    sense.clear() #Resets the pixels
    #Creates the 6*7 blue playing field
    for y in range (6):
        for x in range(7):
            sense.set_pixel(x, 7-y, colors[0])

def turn():
    """
    Decides whose turn it is, then calls select_column(p) to allow the player p
    to make their selection
    """
    global turns
    if gameOver==0: #Checks that the game isn't over
        if turns%2==0 and turns!=42: #If the turn is even, it's p1's turn
            turns+=1 #Increments turns
            select_column(1) #Asks p1 to select a column for their token
        elif turns%2==1 and turns!=42: #If the turn is odd, it's p2's
            turns+=1 #Increments turns
            select_column(2) #Asks p2 to select a column for their token
        elif turns==42: #If 42 turns have passed..
            player_scored(0) #..then it's a draw

def player_scored(p):
    """
    Manages the scoring system.

    p in player_scored(p) is the player who just scored.
    p==0->draw
    p==1->p1 scored
    p==2->p2 scored

    If one of the players won the round, show their score in their color and
    prepare the field for the next round. If one of the players has two points,
    they win the game, the screen turns to their color and the game is reset.
    If it's a draw, no points are given and the field gets prepared for the
    next round.
    """
    global gameOver
    gameOver=1 #The game has ended
    global playerScore
    if p != 0: #Checks if it's a draw
        playerScore[p-1]+=1 #Increments the winner's score
        sense.show_letter(str(playerScore[p-1]),colors[p]) #Shows the score
    #Ends the game if the player already had a point
    if playerScore[0]==2 or playerScore[1]==2 or stopGame==1:
        sleep(1.5) #Pauses long enough to see the score
        sense.clear(colors[p]) #Turns the screen into the winner's color
    sleep(1.5) #Pauses long enough to see the winner's screen
    sense.clear() #Clears the display
    main() #Calls the main game function

def select_column(p):
    """
    Asks the player to select a column with the joystick, then calls for the
    function to drop the token if it is clear.

    p is the player whose turn it is.

    If the joystick is moved upwards, the game is ended.
    The function calls put_down(x,p) in order to drop the token down. If it
    turns out the column is full, put_down(x,p) will call select_column(p) back.
    show_selection(x,p) is used to show the current selection.

    Returns the selected column with x.
    """
    x = 3 #Starts the selection in the middle of the playing field for comfort
    selection = True #Is the player selecting?
    while selection:
        for event in sense.stick.get_events(): #Listens for joystick events
            if event.action == 'pressed': #When the joystick is moved..
                if event.direction == 'right': #..to the right..
                    x = (x + 1) % 7 #..then move the cursor to the right
                elif event.direction == 'left': #..to the left..
                    x = (x - 1) % 7 #..then move the cursor to the left
                elif event.direction =='down': #Pressing down confirms
                    selection = False #Ends selection
                    put_down(x,p) #Calls the function that drops the token
                elif event.direction == 'up': #Pressing up..
                    global stopGame
                    stopGame=1 #..will make main() end the game..
                    player_scored(0) #..and causes a draw
        show_selection(x,p) #Calls the function that shows the current selection
    return x #Returns which column was selected

def show_selection(x,p):
    """
    Shows the cursor for the column selection.

    x is the currently selected column
    p is the player playing

    Ensures that the replacement to black stops when the game is over in order
    to prevent conflict with the score display.
    """
    for i in range(7):
        if i ==x and gameOver==0: #Checks that i is within the playing field
            #Colors the selection with the player p's color
            sense.set_pixel(i, 0, colors[p])
        elif gameOver==0:
            #Resets the pixels once the cursor has moved
            sense.set_pixel(i, 0, (0, 0, 0))

def put_down(x,p):
    """
    Puts the token down in the selected column.

    x is the selected column
    p is the player playing

    If the selected column is full, select_column(p) is called back to ensure
    the player doesn't waste their turn.

    The token is animated down with animate_down(x,y,p) before being set.
    If the token is not a winning one, calls for the next turn with turn().
    """
    #Checks that the column is free (BLUE)
    if sense.get_pixel(x,2)==[0,0,248]:
        for y in range(7): #Finds the lowest available spot
            if sense.get_pixel(x,7-y)==[0,0,248]: #If it's free then..
                animate_down(x,y,p) #..calls for the animation down and..
                sense.set_pixel(x, 7-y, colors[p]) #..puts the token there
                #Checks if it's a winning move
                if check_connectfour(x,7-y)==False:
                    turn() #If not, starts the next turn
                    return
                return
    else:
        select_column(p) #If there is no free spot, restarts selection
    return

def animate_down(x,y,p):
    """
    Creates an animation that makes a pixel move down the selected column to
    the lowest available spot.

    x is the selected column
    y is the lowest available spot
    p is the player playing

    Ensures that the first two rows stay black, and that the others turn BLUE
    again after the animation.
    """
    #For each available spot from the top of the column
    for z in range(7-y):
        sense.set_pixel(x, z, colors[p]) #Set the pixel to the player's color
        sleep(0.03) #Wait long enough for it to be noticeable
        if z != 1 and z != 0: #If it's not the first two rows
            sense.set_pixel(x, z, colors[0]) #Set the pixel back to BLUE
        else: #Otherwise
            sense.set_pixel(x, 1, [0,0,0]) #Set it to black

def check_connectfour(x,y):
    """
    Checks if there is four same-colored token next to each other.

    x is the last played token's column
    y is the last played token's row

    Returns False if there is no winning move this turn. Return True and thus
    makes the game end if it was a winning move.
    """
    #First asks if there is a win horizontally and vertically
    if check_horizontal(x,y)==False and check_vertical(x,y)==False:
        #Then diagonally from the bottom left to the upper right
        if check_diagonal_downleft_upright(x,y)==False:
            #And then diagonally the other way
            if check_diagonal_downright_upleft(x,y)==False:
                #If not, then continue playing by returning False
                return(False)

def check_horizontal(x,y):
    """
    Checks if there is four same-colored tokens in the same row.

    x is the last played token's column
    y is the last played token's row

    Returns False if there isn't four same-colored tokens on the same row.
    Returns True if there are, and calls player_scored(p) for the appropriate
    player based on color (RED==p1, YELLOW==p2)
    """
    #Makes a list out of the row
    horizontal=sense.get_pixels()[8*y:8*y+7]
    for z in range(4): #Checks the row by four groups of four tokens
        if horizontal[z:z+4]==fourYellow: #Is there four yellow tokens?
            player_scored(2) #If yes, p2 scored
            return True #Returns that there was a winning move
        if horizontal[z:z+4]==fourRed: #Is there four red tokens?
            player_scored(1) #If yes, p1 scored
            return True #Returns that there was a winning move.
    return False #Returns that there were no winning move.

def check_vertical(x,y):
    """
    Checks if there is four same-colored tokens in the same column.

    x is the last played token's column
    y is the last played token's row

    Returns False if there isn't four same-colored tokens in the column.
    Returns True if there are, and calls player_scored(p) for the appropriate
    player based on color (RED==p1, YELLOW==p2)
    """
    #Makes a list out of the column
    vertical=[sense.get_pixel(x,2),sense.get_pixel(x,3),sense.get_pixel(x,4),
           sense.get_pixel(x,5),sense.get_pixel(x,6),sense.get_pixel(x,7)]
    for z in range(3): #Checks the column by three groups of four tokens
        if vertical[z:z+4]==fourYellow: #Is there four yellow tokens?
            player_scored(2) #If yes, p2 scored
            return True #Returns that there was a winning move
        if vertical[z:z+4]==fourRed: #Is there four red tokens?
            player_scored(1) #If yes, p1 scored
            return True #Returns that there was a winning move
    return False #Returns that there were no winning move

def check_diagonal_downleft_upright(x,y):
    """
    Checks if there is four same-colored token in the bottom-left to
    upper-right diagonal.

    x is the last played token's column
    y is the last played token's row

    Calls create_diagonal_downleft_upright to create a list from the diagonal.

    Returns False if there isn't four same-colored tokens in the diagonal.
    Returns True if there are, and calls player_scored(p) for the appropriate
    player based on color (RED==p1, YELLOW==p2)
    """
    diagonal=[] #Resets the list
    #Calls a function to create a list from the pixels in a bottom-left to
    #upper-right diagonal
    create_diagonal_downleft_upright(diagonal,x,y)
    for z in range(4): #Checks the diagonal by four groups of four tokens
        if diagonal[z:z+4]==fourYellow: #Is there four yellow tokens?
            player_scored(2) #If yes, p2 scored
            return True #Returns that there was a winning move
        if diagonal[z:z+4]==fourRed: #Is there four red tokens?
            player_scored(1) #If yes, p1 scored
            return True #Returns that there was a winning move
    return False #Returns that there were no winning move

def create_diagonal_downleft_upright(diagonal,x,y):
    """
    Creates a list of seven pixels in a bottom left to upper right diagonal
    centered around the last placed token.

    diagonal is the list
    x is the last played token's column
    y is the last played token's row

    As the function might try to take into account pixels that are out of
    bounds, there is a try except ValueError in order to prevent out of bounds
    errors. The list might be shorter than seven pixels, but the function works
    anyway.

    Returns the list of diagonal pixels.
    """
    for z in range(7): #To have a 7 pixel list
        #Tries to get values that might be out of bounds, three pixels down
        #left and three pixels up right in a diagonal from the token
        try: diagonal.append(sense.get_pixel(x-z+3,y+z-3))
        except: ValueError #Catches out of bounds errors
    return(diagonal) #Returns the list of pixels

def check_diagonal_downright_upleft(x,y):
    """
    Checks if there is four same-colored token in the bottom-right to
    upper-left diagonal.

    x is the last played token's column
    y is the last played token's row

    Calls create_diagonal_downright_upleft to create a list from the diagonal.

    Returns False if there isn't four same-colored tokens in the diagonal.
    Returns True if there are, and calls player_scored(p) for the appropriate
    player based on color (RED==p1, YELLOW==p2)
    """
    diagonal=[] #Resets the list
    #Calls a function to create a list from the pixels in a bottom-right to
    #upper-left diagonal
    create_diagonal_downright_upleft(diagonal,x,y)
    for z in range(4): #Checks the diagonal by four groups of four tokens
        if diagonal[z:z+4]==fourYellow: #Is there four yellow tokens?
            player_scored(2) #If yes, p2 scored
            return True #Returns that there was a winning move
        if diagonal[z:z+4]==fourRed: #Is there four red tokens?
            player_scored(1) #If yes, p1 scored
            return True #Returns that there was a winning move
    return False #Returns that there were no winning move

def create_diagonal_downright_upleft(diagonal,x,y):
    """
    Creates a list of seven pixels in a bottom right to upper left diagonal
    centered around the last placed token.

    diagonal is the list
    x is the last played token's column
    y is the last played token's row

    As the function might try to take into account pixels that are out of
    bounds, there is a try except ValueError in order to prevent out of bounds
    errors. The list might be shorter than seven pixels, but the function works
    anyway.

    Returns the list of diagonal pixels.
    """
    for z in range(7): #To have a 7 pixel list
        #Tries to get values that might be out of bounds, three pixels down
        #right and three pixels up left in a diagonal from the token
        try: diagonal.append(sense.get_pixel(x-z+3,y-z+3))
        except: ValueError #Catches out of bounds errors
    return(diagonal) #Returns the list of pixels

# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)
print(repeat)

if __name__ == '__main__':
    main()
    global repeat
    repeat=1 #If the game is played as standalone, make it repeat
else:
    global repeat
    repeat=0 #If the game is played as a module, make it quit when over
