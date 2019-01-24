from sense_hat import SenseHat
#from sense_emu import SenseHat
from time import sleep, time

sense = SenseHat()
##sense.set_rotation(180)

state =[[0] * 8] * 7
state

def init():
    global state
    state =[[0] * 8] * 7
    
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
    """move left/right and return when 'middle')
"""
    x =0
    selection =True
    while selection:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right':
                    x =(x + 1) % 8
                elif event.direction =='middle':
                    selection = False
        for i in range(8):
            if i ==x:
                sense.set_pixel(i, 0, colors[p])                
            else:    
                sense.set_pixel(i, 0, (0, 0, 0))
    return x                                


show(state)
print(cursor(1))
print(cursor(2))