# Labyrinthe
# par Pierre et Jeremy
# 08.01.19
# 3M03
<<<<<<< HEAD
=======
"""
Labyrinthe is a game for one player that has to reproduce differents pattern
"""
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f

from sense_hat import SenseHat
from time import sleep, time

sense = SenseHat()
sense.clear()

<<<<<<< HEAD
white = (255, 255, 255)
lemon = (255, 255, 128)
pink = (255, 0, 128)
red = (255, 0, 0)
mint = (128, 255, 128)
blue = (0, 0, 255)

=======
#Colours
WHITE = (255, 255, 255)
LEMON = (255, 255, 128)
PINK = (255, 0, 128)
RED = (255, 0, 0)
MINT = (128, 255, 128)
BLUE = (0, 0, 255)

#Levels
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
N1 = [[0,0],[0,1],[0,2],[0,3],
      [0,4],[0,5],[0,6],[0,7],
      [1,7],[2,7],[3,7],[4,7],
      [5,7],[6,7],[7,7]]

N2 = [[0,0],[0,1],[0,2],[0,3],
      [0,4],[1,4],[2,4],[3,4],
      [4,4],[5,4],[6,4],[7,4],
      [7,5],[7,6],[7,7]]

N3 = [[0,0],[1,0],[2,0],[3,0],
      [4,0],[5,0],[6,0],[7,0],
      [7,1],[7,2],[7,3],[6,3],
      [5,3],[4,3],[3,3],[2,3],
      [1,3],[0,3],[0,4],[0,5],
      [1,5],[2,5],[3,5],[4,5],
      [5,5],[6,5],[7,5],[7,6],
      [7,7]]

N4 = [[0,0],[0,1],[0,2],[0,3],
      [0,4],[0,5],[0,6],[0,7],
      [1,7],[2,7],[3,7],[3,6],
      [3,5],[3,4],[3,3],[4,4],
      [4,5],[4,6],[4,7],[5,7],
      [6,7],[7,7],[7,6],[7,5],
      [7,4],[7,3],[7,2],[7,1],
      [7,0]]

N5 = [[0,0],[1,0],[1,1],[2,1],
      [3,1],[3,2],[4,2],[4,3],
      [4,4],[3,4],[2,4],[2,5],
      [3,5],[4,5],[5,5],[5,6],
      [4,6],[4,7],[5,7],[6,7],
      [7,7]]

N6 = [[0,0],[0,1],[1,1],[2,1],
      [2,2],[3,2],[3,1],[3,0],
      [4,0],[4,1],[4,2],[4,3],
      [3,3],[3,4],[3,5],[2,5],
      [2,6],[3,6],[4,6],[5,6],
      [6,6],[7,6],[7,7]]
<<<<<<< HEAD
=======

>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
N7 = [[1,4],[1,3],[1,2],[2,2],
      [2,3],[3,3],[3,2],[3,1],
      [4,1],[5,1],[5,2],[5,3],
      [5,4],[5,5],[6,5],[6,4],
      [6,3],[6,2],[6,1],[6,0],
      [5,0],[4,0],[3,0],[2,0],
      [1,0],[0,0],[0,1],[0,2],
      [0,3],[0,4],[0,5],[1,5],
      [2,5],[2,6],[2,7],[3,7],
      [4,7],[4,6],[5,6],[6,6],
      [6,7],[7,7]]
<<<<<<< HEAD
N8 = [[0,0]]
N9 = [[0,0]]


levels = [N1, N2, N3, N4, N5, N6, N7, N8, N9]


lvl_name = []
for i in range(len(levels)):
    a = str(i+1)
    lvl_name.append(str(i+1))

def patern_stage(niv):
    for event in sense.stick.get_events():
        pass
    dist = len(niv)
    sense.show_message("Ready ? 3 2 1",
                       text_colour=white, scroll_speed=0.05)
    sense.clear(mint)
    sleep(1)
    for step in range(dist):
        sense.set_pixel(niv[step][0],niv[step][1], pink)
        sleep(0.5)
    sleep(1.5)
    sense.clear(mint)

def player_stage(niv):
    playing = True
    a = niv[0][0]
    b = niv[0][1]
    (x, y) = (a, b)
    state = [[a, b]]
    sense.stick.get_events()
    while playing:
        for event in sense.stick.get_events():
=======

N8 = [[3,3],[3,2],[2,2],[2,3],
      [2,4],[2,5],[2,6],[2,7],
      [3,7],[3,6],[3,5],[3,4],
      [4,4],[4,3],[5,3],[6,3],
      [6,2],[6,1],[6,0],[5,0],
      [5,1],[5,2],[4,2],[4,1],
      [4,0],[3,0],[2,0],[1,0],
      [1,1],[1,2],[0,2],[0,3],
      [0,4],[0,5],[0,6],[1,6],
      [2,6],[3,6],[4,6],[5,6],
      [5,5],[5,4],[6,4],[7,4],
      [7,5],[7,6],[7,7]]

N9 = [[7,1],[7,0],[6,0],[6,1],
      [6,2],[7,2],[7,1],[6,1],
      [5,1],[4,1],[3,1],[3,2],
      [3,3],[3,4],[3,5],[3,6],
      [4,6],[5,6],[5,5],[5,4],
      [5,3],[5,2],[5,1],[5,0],
      [4,0],[3,0],[2,0],[1,0],
      [0,0],[0,1],[0,2],[0,3],
      [0,4],[0,5],[1,5],[1,4],
      [2,4],[3,4],[4,4],[5,4],
      [6,4],[7,4],[7,3],[6,3],
      [5,3],[4,3],[4,2],[3,2],
      [2,2],[2,3],[2,4],[2,5],
      [2,6],[1,6],[1,7],[2,7],
      [3,7],[4,7],[4,6],[4,5],
      [5,5],[6,5],[6,6],[7,6],
      [7,5],[7,6],[6,6],[6,7],
      [7,7]]

#List of the Levels
levels = [N1, N2, N3, N4, N5, N6, N7, N8, N9]

#Create a list of the name of each level by their ranks and order.
lvl_name = []
for i in range(len(levels)):
    lvl_name.append(str(i+1))

#Main menu, the selection of the level.
def main():
    """
    Definition that allows the player to select his/her level using the joystick to the right or the left 
    after a short message that invites him/her to choose. 
    To stop the game, the player has to use the joystick to the top or to the bottom.
    """
    running = True
    sense.show_message("Select the level",
                       text_colour=WHITE, scroll_speed=0.05)
    sleep(0.5)
    lvl = 0 #(0 = level 1, 1 = level 2, etc.)
    sense.show_letter(lvl_name[lvl],
                      text_colour=WHITE)
    while running:
        for event in sense.stick.get_events():
                if event.action == 'pressed':
                    if event.direction == 'left':   #select a lower level.
                        if lvl >= 1:
                            lvl = lvl-1
                            sense.show_letter(lvl_name[lvl],
                                              text_colour=WHITE)
                        else:
                            pass
                    elif event.direction == 'right':    #select a higher level.
                        if lvl <= len(lvl_name)-2:
                            lvl = lvl+1
                            sense.show_letter(lvl_name[lvl],
                                              text_colour=WHITE)
                        else:
                            pass
                    elif event.direction == 'down':#turn off the game
                        running = False
                        sense.clear()
                    elif event.direction == 'up':#turn off the game
                        running = False
                        sense.clear()
                    elif event.direction == 'middle':#start the selected level
                        running = False
                        start_level(levels[lvl])
                        
#Brings together the 2 functions of the level game. There is 2 stages: Demonstration and Reproduction. 
def start_level(niv):
    """ Allows to execute the levels in the propper order."""
    patern_stage(niv)
    player_stage(niv)
      
#Demonstration of the patern:
def patern_stage(niv):
    """ Definition that execute the pattern that the player must reproduce."""
    for event in sense.stick.get_events():#IMPORTANT: reset the manipulation of the player. 
        pass                              #If not, can fail the level without starting it.
    dist = len(niv)
    sense.show_message("Ready ? 3 2 1",
                       text_colour=WHITE, scroll_speed=0.05)
    sense.clear(MINT)
    sleep(1)
    for step in range(dist):                            #It shows one by one the pixel of the selected level patern.
        sense.set_pixel(niv[step][0],niv[step][1], PINK)
        sleep(0.5)                                      
    sleep(1.5) #Time to memorizing
    sense.clear(MINT)  
      
#Reproduction by the player    
def player_stage(niv):
    """ Allows the player to reproduce the pattern that has been shown.""" 
    playing = True
    a = niv[0][0]    
    b = niv[0][1]    
    (x, y) = (a, b)    
    state = [[a, b]] #Create a list with the starting point of the selected level patern.
    sense.stick.get_events()
    while playing:
        for event in sense.stick.get_events():      #It moves the pixel with the player moves and add the point passed by the player in the state[].
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
            if event.action == 'pressed':
                if event.direction == 'left':
                    if x > 0:
                        x = min(x-1, 7)
                        state.append([x, y])
                elif event.direction == 'right':
                    if x < 7:
                        x = max(x+1, 0)
                        state.append([x, y])
                if event.direction == 'down':
                    if y < 7:
                        y = min(y+1, 7)
                        state.append([x, y])
                elif event.direction == 'up':
                    if y > 0:
                        y = max(y-1, 0)
                        state.append([x, y])
                elif event.direction == 'middle':
                    playing = False
<<<<<<< HEAD
        sense.set_pixel(x, y, red)
    if state[:] == niv[:]:
        sense.show_message("WINNER !",
                            text_colour=lemon, scroll_speed=0.05)
        sleep(2)
        start_game()
    else:
        sense.show_message("LOSER !",
                            text_colour=blue, scroll_speed=0.05)
        sleep(2)
        try_again(niv)
        
def try_again(niv):
    wait = True
    answer = 0
    sense.show_message('Try again?',text_colour=white,scroll_speed=0.05)
    sense.show_letter('Y',text_colour=white)
    while wait == True:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'left':
                    if answer >= 1:
                        answer = answer - 1
                        sense.show_letter('Y',text_colour=white)
                    else:
                            pass
                elif event.direction == 'right':
                    if answer <= 0:
                        answer = answer + 1
                        sense.show_letter('N',text_colour=white)
                    else:
                        pass
                elif event.direction == 'middle':
=======
        sense.set_pixel(x, y, RED)
    if state[:] == niv[:]:              #Compare the way choosen by the player with the selected level patern. Results of the try.
        sense.show_message("WINNER !",
                            text_colour=LEMON, scroll_speed=0.05)
        sleep(2)
        main()    #brings back to the level selection.
    else:
        sense.show_message("LOSER !",
                            text_colour=BLUE, scroll_speed=0.05)
        sleep(2)
        try_again(niv)  #cf. try_again() function

            
            
#Ask the player if he wants to try again or go back to level selection.
def try_again(niv):
    """ Allows the player if he loses to try again the stage."""
    wait = True
    answer = 0 #(0 = Yes , 1 = No)
    sense.show_message('Try again?',
                       text_colour=WHITE,scroll_speed=0.05)
    sense.show_letter('Y',
                      text_colour=WHITE)
    while wait == True:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'left': #select to try again by clicking on the left
                    if answer >= 1:
                        answer = answer - 1
                        sense.show_letter('Y',
                                          text_colour=WHITE)
                    else:
                            pass
                elif event.direction == 'right': #select to go back to main menuby clicking on the right
                    if answer <= 0:
                        answer = answer + 1
                        sense.show_letter('N',
                                          text_colour=WHITE)
                    else:
                        pass
                elif event.direction == 'middle': #applies the selection by clicking on the middle.
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
                    wait = False
                    if answer == 0:
                        start_level(niv)
                    elif answer == 1:
<<<<<<< HEAD
                        start_game()
                else:
                    start_game()
                            
   
def start_level(niv):
    patern_stage(niv)
    player_stage(niv)
    
def start_game():
    running = True
    sense.show_message("Select the level",
                       text_colour=white, scroll_speed=0.05)
    sleep(0.5)
    lvl = 0
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
                    elif event.direction == 'down':
                        pass
                    elif event.direction == 'up':
                        pass
                    elif event.direction == 'middle':
                        running = False
                        start_level(levels[lvl])

start_game()
=======
                        main()
                else: #If the player moves up or down, it goes back to main menu.
                    main()

main()
>>>>>>> d7109e730d9f15aa4366100c361c0832936ee66f
