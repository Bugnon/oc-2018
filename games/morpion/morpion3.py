from sense_hat import SenseHat
from time import sleep, time

sense = SenseHat()

#couleurs
X = (255, 255, 255)
O = (0, 0, 0)
P1 = (0, 0, 255)
P2 = (255, 255, 0)
colors = (O, P1, P2)
score1 = 0
score2 = 0

def init():
    global state   #utilisable dans tout le code
    global board  
    global state_to_board
    
    board = [
        O, O, X, O, O, X, O, O,
        O, O, X, O, O, X, O, O,
        X, X, X, X, X, X, X, X,
        O, O, X, O, O, X, O, O,
        O, O, X, O, O, X, O, O,
        X, X, X, X, X, X, X, X,
        O, O, X, O, O, X, O, O,
        O, O, X, O, O, X, O, O, 
        ]

    state_to_board = [[(0, 1, 8, 9), (3, 4, 11, 12), (6, 7, 14, 15)],
                      [(24, 25, 32, 33), (27, 28, 35, 36), (30, 31, 38, 39)],
                      [(48, 49, 56, 57), (51, 52, 59, 60), (54, 55, 62, 63)]]

    state =  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
  



def show_board(board, state):
    for y in range(len(state)):
        for x, s in enumerate(state[y]):  #pour mettre puxels entre les lignes
            c = colors[s]
            for index in state_to_board[y][x]:
                board[index] = c
    sense.set_pixels(board)
    
    

def is_winning(p, state):  # cas gagnant
    return  state[0][0] == state[0][1] == state[0][2] == p or \
            state[1][0] == state[1][1] == state[1][2] == p or \
            state[2][0] == state[2][1] == state[2][2] == p or \
            state[0][0] == state[1][0] == state[2][0] == p or \
            state[0][1] == state[1][1] == state[2][1] == p or \
            state[0][2] == state[1][2] == state[2][2] == p or \
            state[0][0] == state[1][1] == state[2][2] == p or \
            state[0][2] == state[1][1] == state[2][0] == p    

def is_draw(state): 
    for i in state:
        for s in i:
            if s == 0:
                return False
    return True
     
def play(p,board, state):
    (x, y) = (1, 1) 
    dirs = {'up':(0, -1), 'down':(0, 1),
            'right':(1, 0), 'left':(-1, 0)} 
    
    c = tuple(int(x/2) for x in colors[p])
    for index in state_to_board[y][x]:
        board[index] = c
    sense.set_pixels(board)
    
    while True :
        event = sense.stick.wait_for_event()
        if event.action == 'pressed':
            if event.direction in dirs:  
                (dx, dy) = dirs[event.direction]
                
                x = (x + dx) % len(state)    
                y = (y + dy) % len(state)
                
            
                           
                show_board(board, state)   # eviter de colorier le chemin
                
                c = tuple(int(x/2) for x in colors[p]) 
                for index in state_to_board[y][x]:
                    board[index] = c
                sense.set_pixels(board)   
            else:
                if state[y][x] == 0: 
                    state[y][x] = p
                    show_board(board, state)
                    return
def show_score(p):
    """Displays the score."""
    global score1, score2
    if p == 1:
        score1 += 1
    elif p == 2:
        score2 += 1
    msg = 'player1='+str(score1)+' player2='+str(score2)
    sense.show_message(msg)
                
def end_game(p):
    global running
    if p == 0:
        sense.show_message("draw")
    else:
        sense.show_letter(str(p))
        
    sleep(3)
    sense.show_message('press to play')
    
    while True:
        event = sense.stick.wait_for_event()
        if event.direction == "left":
            running = False
            return
        elif event.direction == 'right':
            show_score(p)
            init()
            show_board(board, state)
            return

running = True
init()
show_board(board, state)
player = 1

while running:
    play(player, board, state)
    if is_winning(player, state):
        end_game(player)
        
    elif is_draw(state):
        end_game(0)
        
    player = 3 - player    


                   
    
     