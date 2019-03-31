# File : Wordament 
# Date : 31.03.2019
# Author : Mirko Pirona, Michael Greub et Fabian Roulin

###########################################
##### Importation of the game modules #####
###########################################

import pyglet
from levels import levels

############################################
### Initialisation des variables de base ###
############################################

# Screen size :
height = 650
width = 600
pattern_size = min(height, width)
#pattern_size = min(window.height, window.width)

# Variable in game :
new_word = ""

M_NUL = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

old_case = [-1, -1]

# Select of the level imported :
ML = (levels.L1)

window = pyglet.window.Window(width, height)

# Initialization of labels of the game :
new_word_print = pyglet.text.Label('Word : -', font_size=30, x=0, y=610)
score_print = pyglet.text.Label('Score : 0', font_size=30, x=400, y=610)

############################################
########## Start of the game code ##########
############################################

# Actions when the game start to create the game board :
@window.event
def on_draw():
    global ML
    window.clear()
    for u in range(4):
        for n in range(4):
            letter = "images/" + ML[3-n][u] + ".png"
            letter_print = pyglet.image.load(letter)
            letter_print.blit(x= pattern_size/4 * u, y=pattern_size/4 * n, height=pattern_size/4, width=pattern_size/4)
    new_word_print.draw()
    score_print.draw()

# Actions when the click of the mouse is release :
@window.event 
def on_mouse_release(x, y, button, modifiers):
    global old_case
    global new_word
    global M_NUL
    M_NUL = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
    old_case = [-1, -1]
    new_word = ""

# Actions when the mouse is moving :
@window.event  
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global new_word
    global M_NUL
    global old_case
    if buttons & pyglet.window.mouse.LEFT:
    #print(x, y, dx, dy, buttons, modifiers)
        for k in range(4):
            for i in range(4):
                if pattern_size/4 * k < y < ((k+1) * pattern_size/4 ) and  pattern_size/4 * i < x < ((i+1) * pattern_size/4) and M_NUL[3-k][i] == 0:
                    if old_case == [-1, -1] or ((old_case[0] - 2) < k < (old_case[0] + 2) and (old_case[1] - 2) < i < (old_case[1] + 2)): 
                        print(old_case)
                        # print(ML[3-k][i])
                        M_NUL[3-k][i] = 1
                        new_word += (ML[3-k][i])
                        old_case = [k, i]
                        print(new_word)
                        new_word_print.text = "Word : " + new_word

###########################################
########## Launching of the game ##########
###########################################

pyglet.app.run()