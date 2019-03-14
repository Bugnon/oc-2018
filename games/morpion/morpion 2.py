from sense_hat import SenseHat
#from sense_emu import SenseHat
from time import sleep, time

sense = SenseHat()
sense.set_rotation(180)

def init():
    global state
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

dark_blue = (0, 0, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = (dark_blue, red, green)

def show(state):
    sense.clear()
    for y in range(3):
        for x in range(3):
            s = state[y][x]  # s is 0, 1, or 2
            sense.set_pixel(x, y, colors[s])            

def winning(state, p):
    return  state[0][0] == state[0][1] == state[0][2] == p or \
            state[1][0] == state[1][1] == state[1][2] == p or \
            state[2][0] == state[2][1] == state[2][2] == p or \
            state[0][0] == state[1][0] == state[2][0] == p or \
             state[0][1] == state[1][1] == state[2][1] == p or \
            state[0][2] == state[1][2] == state[2][2] == p or \
            state[0][0] == state[1][1] == state[2][2] == p or \
            state[0][2] == state[1][1] == state[2][0] == p

def play(state, p):
    (x, y) = (1, 1)
    dirs = {'up':(0, 1), 'down':(0, -1),
            'right':(1, 0), 'left':(-1, 0)}
    
    while True :
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction in dirs:
                    (dx, dy) = dirs[event.direction]
                    
                    x = (x + dx) % 3
                    y = (y + dy) % 3
                    show(state)
                    sense.set_pixel(x, y, blue)
                else:
                    state[y][x] = p
                    show(state)
                    return     
init()
show(state)
win = False
player = 1

while True:
    play(state, player)
    if winning(state, player):
        sense.show_letter(str(player))
        sleep(3)
        init()
        show(state)
    player = 3 - player
