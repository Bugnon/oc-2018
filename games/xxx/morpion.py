<<<<<<< HEAD
=======
#Hélène Ardevol et Victoria Vila
#Bugnon 3M4
#5 Février 2019
#Jeu du morpion avec SenseHat
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
"""
Morpion is a game played by 2 players on a 3x3 board.
The goal is to align 3 symbols in a line, column or diagonal.
"""
<<<<<<< HEAD

=======
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
from sense_hat import SenseHat
from time import sleep, time
from gamelib import *

sense = SenseHat()

<<<<<<< HEAD
#couleurs
=======
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
X = WHITE
O = BLACK
P1 = BLUE
P2 = YELLOW
colors = (O, P1, P2)
score1 = 0
score2 = 0

def init():
<<<<<<< HEAD
    global state   #utilisable dans tout le code
    global board  
    global state_to_board
    
=======
    """Defines the intial state of the game, which will be modified
        by the following players."""
    global state   #utilisable dans tout le code
    global board
    global state_to_board
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    board = [
        O, O, X, O, O, X, O, O,
        O, O, X, O, O, X, O, O,
        X, X, X, X, X, X, X, X,
        O, O, X, O, O, X, O, O,
        O, O, X, O, O, X, O, O,
        X, X, X, X, X, X, X, X,
        O, O, X, O, O, X, O, O,
<<<<<<< HEAD
        O, O, X, O, O, X, O, O, 
=======
        O, O, X, O, O, X, O, O,
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
        ]

    state_to_board = [[(0, 1, 8, 9), (3, 4, 11, 12), (6, 7, 14, 15)],
                      [(24, 25, 32, 33), (27, 28, 35, 36), (30, 31, 38, 39)],
                      [(48, 49, 56, 57), (51, 52, 59, 60), (54, 55, 62, 63)]]

<<<<<<< HEAD
    state =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



def show_board(board, state):
    for y in range(len(state)):
        for x, s in enumerate(state[y]):  #pour mettre puxels entre les lignes
=======
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def show_board(board, state):
    """Shows the different states of the game that a player can make."""
    for y in range(len(state)):
        for x, s in enumerate(state[y]): #pour mettre pixels entre les lignes
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
            c = colors[s]
            for index in state_to_board[y][x]:
                board[index] = c
    sense.set_pixels(board)
<<<<<<< HEAD
    
    

def is_winning(p, state):  # cas gagnant
    return  state[0][0] == state[0][1] == state[0][2] == p or \
            state[1][0] == state[1][1] == state[1][2] == p or \
=======

def is_winning(p, state):
    """Defines all of the states where a player wins in function of morpions
        rules."""
    return  state[0][0] == state[0][1] == state[0][2] == p or \
             state[1][0] == state[1][1] == state[1][2] == p or \
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
            state[2][0] == state[2][1] == state[2][2] == p or \
            state[0][0] == state[1][0] == state[2][0] == p or \
            state[0][1] == state[1][1] == state[2][1] == p or \
            state[0][2] == state[1][2] == state[2][2] == p or \
            state[0][0] == state[1][1] == state[2][2] == p or \
<<<<<<< HEAD
            state[0][2] == state[1][1] == state[2][0] == p    

def is_draw(state):
    """"""
# Si il y en a qui sont à l'état 0
=======
            state[0][2] == state[1][1] == state[2][0] == p

def is_draw(state):
    """Returns True if no boxes are empty but nobody has won. If not returns False."""
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    for i in state:
        for s in i:
            if s == 0:
                return False
    return True
<<<<<<< HEAD
     
def play(p,board, state):
    """Definition that ables us to play the game. It can make our cursor,
        with the joystick, move within our board without leaving a trace behind it.
        It makes our cursor appear in the middle of the board when starting the game
        and when we start moving our cursor the color of it is divided by two,
        like that we can diffirenciate when we are moving to when we decided where
        to place our colored cursor."""
    (x, y) = (1, 1) # position initial du curseur 
    dirs = {'up':(0, -1), 'down':(0, 1),
            'right':(1, 0), 'left':(-1, 0)} # coordonées dx et dy
    
    c = tuple(int(x/2) for x in colors[p])
    for index in state_to_board[y][x]:      # pour afficher le cusreur dès la premiere fois au centre
        board[index] = c
    sense.set_pixels(board)
    
=======

def play(p, board, state):
    """Definition that ables us to play the game. It can make our cursor,
        with the joystick, move within our board without leaving a trace behind
        it by changing our cursors coordinates. It makes our cursor appear in the
        middle of the board when startin the game and when we start moving our
        cursor, the color of it is divided by two, like that we can diffirenciate
        when we are moving to when we decided where to place our colored cursor."""
    (x,y) = (1,1) # position intitiale du curseur
    dirs = {'up':(0, -1), 'down':(0, 1),
            'right':(1, 0), 'left':(-1, 0)} #coordonees des x et des y
    c = tuple(int(x/2) for x in colors[p])
    for index in state_to_board[y][x]:
        board[index] = c
        sense.set_pixels(board)

>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    while True :
        event = sense.stick.wait_for_event()
        if event.action == 'pressed':
            if event.direction in dirs:  # si c'est dans le dictionnaire = un déplacement
                (dx, dy) = dirs[event.direction]
<<<<<<< HEAD
                
                x = (x + dx) % len(state)    # modifie coord du curseur 
                y = (y + dy) % len(state)
                
            
##                print(x, y)                
                show_board(board, state)   # eviter de colorier le chemin
                
                c = tuple(int(x/2) for x in colors[p]) # permet de diviser le curseur oar 2
                for index in state_to_board[y][x]:
                    board[index] = c
                sense.set_pixels(board)   # réflichie le curseru
            else:
                if state[y][x] == 0:  # seulemnt mettre sur une case libre
                    state[y][x] = p
                    show_board(board, state)
                    return
def show_score(p):
    """Displays the score"""
    global score1, score2
    if p==1:
        score1 +=1
    elif p == 2:
        score2 +=1
    msg = 'player1='+str(score1)+' player2='+str(score2)
    sense.show_message(msg)
    
def end_game(p):
    """Display the result ask for continuation to the game.
    If the player presses any button within 3 seconds, the function
    returns True, otherwise the function returns False."""
=======

                x = (x + dx) % len(state)    # modifie les  coord. du curseur
                y = (y + dy) % len(state)

                show_board(board, state)   # eviter de colorier le chemin
                c = tuple(int(x/2) for x in colors[p]) # permet de diviser le curseur par 2

                for index in state_to_board[y][x]:
                    board[index] = c
                sense.set_pixels(board)   # réflichi le curser
            else:
                if state[y][x] == 0:  # seulement mettre sur une case libre
                    state[y][x] = p
                    show_board(board, state)
                    return

def show_score(p):
    """Displays the score"""
    global score1, score2
    if p == 1:
        score1 += 1
    elif p == 2:
        score2 += 1
    msg = 'player1=' + str(score1) + ' player2=' + str(score2)
    sense.show_message(msg)

def end_game(p):
    """Displays the result and asks for continuation to the game."""
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    if p == 0:
        sense.show_message("draw")
    else:
        sense.show_letter(str(p))
    sleep(3)
    show_score(p)
    return continue_game()
<<<<<<< HEAD
    
def continue_game():
    """Return True if player wants to continue."""
=======

def continue_game():
    """If the player presses any button within 3 seconds, the function
    returns True, otherwise the function returns False."""
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    sense.show_letter('?')
    sense.stick.get_events()
    t0 = time()
    while time() < t0 + 3:
        for event in sense.stick.get_events():
            init()
            show_board(board, state)
            print('continue')
            return True
    print('timeout')
    return False

def main():
    """Play the game until player decides to stop."""
    init()
    show_board(board, state)
    player = 1
    playing = True
<<<<<<< HEAD

=======
    
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
    while playing:
        play(player, board, state)
        if is_winning(player, state):
            playing = end_game(player)
            
        elif is_draw(state):
            playing = end_game(0)
            
        player = 3 - player    
<<<<<<< HEAD


=======
        
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
<<<<<<< HEAD
    main() 
=======
    main()
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
