##from sense_hat import SenseHat
from sense_emu import SenseHat
from time import sleep, time

sense = SenseHat()
##sense.set_rotation(180)


active =True

def init():
    global state
    state =[
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0]]
    
blue = (0, 0, 255)
red =(255, 0, 0)
yellow=(255, 255, 0)
colors=(blue, red, yellow)


def show(state):
    sense.clear()
    for y in range (7):
        for x in range(8):
            s = state [y][x]
            sense.set_pixel(x, 7-y, colors[s])
        
def cursor(p):
    """move left/right and return when 'middle'"""
    global active
    
    x =0
    selection =True
    while selection:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right':
                    x =(x + 1) % 8
                elif event.direction == 'left':
                    x = (x - 1) % 8 
                elif event.direction =='middle':
                    selection = False
                elif event.direction == 'up':
                    active = False
                    
        for i in range(8):
            if i ==x:
                sense.set_pixel(i, 0, colors[p])                
            else:    
                sense.set_pixel(i, 0, (0, 0, 0))
    return x                                

def descend(x, p):
    if state[5][x] > 0: 
        state[6][x] =p
    elif state[4][x] > 0: 
        state[5][x] =p
    elif state [3][x] > 0:
        state [4][x] =p
    elif state[2][x] > 0:
        state [3][x] =p
    elif state[1][x]> 0:
        state[2][x] =p
    else:
        state[0][x] =p
        
    

init()
show(state)
while active:
    x =cursor(1)
    descend(x, 1)
    show(state)
    x =cursor(2)
    descend(x, 2)
    show(state)   