# Labyrinthe
# par Pierre et Jeremy
# 08.01.19
# 3M03

from sense_hat import SenseHat

from time import sleep, time

sense = SenseHat()
sense.set_rotation(90)
sense.clear()


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 128)
orange = (255, 128, 0)
white = (255, 255, 255)
black = (0, 0, 0)
colors = (red, magenta, blue, cyan, green, yellow, white, orange)

N1 = [[0,0],[0,1],[0,2],[0,3],
      [0,4],[1,4],[2,4],[3,4],
      [4,4],[5,4],[6,4],[7,4],
      [7,5],[7,6],[7,7],]
N2 = [[0,0]]
N3 = [[0,0]]
N4 = [[0,0]]

levels = [N1, N2, N3, N4,]


def patern_stage(niv):
    dist = len(niv)
    sense.show_message("Ready?  3   2   1", text_colour=blue, scroll_speed=0.1)
    for step in range(dist):
        sense.set_pixel(niv[step][0],niv[step][1], yellow)
        sleep(1)
    sleep(3)
    sense.clear()


def player_stage(niv):
    running = True
    (x, y) = (0, 0)
    state = [[0, 0]]
    while running:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'up':
                    x = min(x-1, 7)
                    state.append([x, y])
                elif event.direction == 'down':
                    x = max(x+1, 0)
                    state.append([x, y])
                if event.direction == 'left':
                    y = min(y+1, 7)
                    state.append([x, y])
                elif event.direction == 'right':
                    y = max(y-1, 0)
                    state.append([x, y])
                elif event.direction == 'middle':
                    running = False
        sense.set_pixel(x, y, red)
    if state[:] == niv[:]:
        sense.show_message("WINNER", text_colour=yellow, scroll_speed=0.1)
        start_game()
    else:
        sense.show_message("LOSER", text_colour=yellow, scroll_speed=0.1)
        start_game()

def start_level(niv):
    patern_stage(niv)
    player_stage(niv)
    
def start_game():
    running = True
    sense.show_message("Please, select the level", text_colour=yellow, scroll_speed=0.1)
    sleep(1)
    lvl = 0
    lvl_name = ["1","2","3","4"]
    sense.show_letter("1", text_colour=yellow)
    while running:
        for event in sense.stick.get_events():
                if event.action == 'pressed':
                    if event.direction == 'up':
                        if lvl >= 1:
                            lvl = lvl-1
                            sense.show_letter(lvl_name[lvl], text_colour=yellow)
                        else:
                            pass
                    elif event.direction == 'down':
                        if lvl <= 2:
                            lvl = lvl+1
                            sense.show_letter(lvl_name[lvl], text_colour=yellow)
                        else:
                            pass
                    if event.direction == 'left':
                        pass
                    elif event.direction == 'right':
                        pass
                    elif event.direction == 'middle':
                        running = False
                        start_level(levels[lvl])
start_game()      
