# Labyrinthe
# par Pierre et Jeremy
# 08.01.19
# 3M03

from sense_hat import SenseHat
from time import sleep, time

sense = SenseHat()
sense.clear()

white = (255, 255, 255)
lemon = (255, 255, 128)
pink = (255, 0, 128)
red = (255, 0, 0)
mint = (128, 255, 128)
blue = (0, 0, 255)

N1 = [[0,0],[0,1],[0,2],[0,3],
      [0,4],[0,5],[0,6],[0,7],
      [1,7],[2,7],[3,7],[4,7],
      [5,7],[6,7],[7,7],
      ]
N2 = [[0,0],[0,1],[0,2],[0,3],
      [0,4],[1,4],[2,4],[3,4],
      [4,4],[5,4],[6,4],[7,4],
      [7,5],[7,6],[7,7],
      ]
N3 = [[0,0],[1,0],[1,1],[1,2],
      [2,2],[3,2],[3,3],[3,4],
      [3,5],[4,5],[5,5],[6,5],
      [6,6],[6,7],[7,7],
      ]
N4 = [[0,0],[1,0],[1,1],[2,1],
      [3,1],[3,0],[4,0],[5,0],
      [5,1],[5,2],[5,3],[4,3],
      [3,3],[2,3],[1,3],[0,3],
      [0,4],[0,5],[0,6],[1,6],
      [2,6],[3,6],[4,6],[5,6],
      [6,6],[7,6],[7,7],
      ]
N5 = [[0,0]]
N6 = [[0,0]]
N7 = [[0,0]]
N8 = [[0,0]]
N9 = [[0,0]]


levels = [N1, N2, N3, N4, N5, N6, N7, N8, N9]

lvl_name = []
for i in range(len(levels)):
    a = str(i+1)
    lvl_name.append(a)

def patern_stage(niv):
    dist = len(niv)
    sense.show_message("Ready ? 3 2 1",
                       text_colour=white, scroll_speed=0.02)
    sense.clear(mint)
    sleep(1)
    for step in range(dist):
        sense.set_pixel(niv[step][0],niv[step][1], pink)
        sleep(1)
    sleep(3)
    sense.clear(mint)

def player_stage(niv):
    running = True
    (x, y) = (0, 0)
    state = [[0, 0]]
    while running:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'left':
                    x = min(x-1, 7)
                    state.append([x, y])
                elif event.direction == 'right':
                    x = max(x+1, 0)
                    state.append([x, y])
                if event.direction == 'down':
                    y = min(y+1, 7)
                    state.append([x, y])
                elif event.direction == 'up':
                    y = max(y-1, 0)
                    state.append([x, y])
                elif event.direction == 'middle':
                    running = False
        sense.set_pixel(x, y, red)
    if state[:] == niv[:]:
        sense.show_message("WINNER !",
                            text_colour=lemon, scroll_speed=0.02)
        sleep(2)
        start_game()
    else:
        sense.show_message("LOSER !",
                            text_colour=blue, scroll_speed=0.02)
        sleep(2)
        start_game()

def start_level(niv):
    patern_stage(niv)
    player_stage(niv)
    
def start_game():
    running = True
    sense.show_message("Please, select the level",
                       text_colour=white, scroll_speed=0.02)
    sleep(1)
    lvl = 1
    sense.show_letter(lvl_name[lvl],
                      text_colour=white)
    while running:
        for event in sense.stick.get_events():
                if event.action == 'pressed':
                    if event.direction == 'left':
                        if lvl >= 1:
                            lvl = lvl-1
                            sense.show_letter(lvl_name[lvl],
                                              text_colour=white)
                        else:
                            pass
                    elif event.direction == 'right':
                        if lvl <= len(lvl_name)-2:
                            lvl = lvl+1
                            sense.show_letter(lvl_name[lvl],
                                              text_colour=white)
                        else:
                            pass
                    if event.direction == 'down':
                        pass
                    elif event.direction == 'up':
                        pass
                    elif event.direction == 'middle':
                        running = False
                        start_level(levels[lvl])

start_game()