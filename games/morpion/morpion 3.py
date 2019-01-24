from sense_emu import SenseHat
from time import sleep, time

sense = SenseHat()

#couleurs
X = (255, 255, 255)
O = (0, 0, 0)
P1 = (0, 0, 255)
P2 = (255, 255, 0)
colors = (O, P1, P2)

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

def is_draw(state): # Si il y en a qui sont à l'état 0
    for i in state:
        for s in i:
            if s == 0:
                return False
    return True
     
def play(p,board, state):
    (x, y) = (1, 1) # position initial du curseur 
    dirs = {'up':(0, -1), 'down':(0, 1),
            'right':(1, 0), 'left':(-1, 0)} # coordonées dx et dy
    
    c = tuple(int(x/2) for x in colors[p])
    for index in state_to_board[y][x]:      # pour afficher le cusreur dès la premiere fois au centre
        board[index] = c
    sense.set_pixels(board)
    
    while True :
        event = sense.stick.wait_for_event()
        if event.action == 'pressed':
            if event.direction in dirs:  # si c'est dans le dictionnaire = un déplacement
                (dx, dy) = dirs[event.direction]
                
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
                
def end_game(p):
    if p == 0:
        sense.show_message("draw")
    else:
        sense.show_letter(str(p))
        
    sleep(3)
    sense.show_message('press to play')
    
    while True:
        event = sense.stick.wait_for_event()
        if event.action == "pressed":   # besoin d'une action pr réinit la partie
            init()
            show_board(board, state)
            return

init()
show_board(board, state)
player = 1

while True:
    play(player, board, state)
    if is_winning(player, state):
        end_game(player)
        
    elif is_draw(state):
        end_game(0)
        
    player = 3 - player    


                   
    
    