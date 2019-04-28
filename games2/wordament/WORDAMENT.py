# File : Wordament 
# Date : 31.03.2019
# Author : Mirko Pirona, Michael Greub et Fabian Roulin

###########################################
##### Importation of the game modules #####
###########################################

import pyglet
from levels import levels
import codecs
from pathlib import Path
from time import sleep
############################################
### Initialisation des variables de base ###
############################################

# Screen size :
height = 650
width = 600
pattern_size = min(height, width)
#pattern_size = min(window.height, window.width)

# Variable in game :
new_word = ''

M_NUL = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

score = 0

taken_words = []

old_case = [-1, -1]

# Imported variables :

game_location = str(Path(__file__).absolute().parent)
ML = (levels.L1)

window = pyglet.window.Window(width, height)

image_store = {}
for u in range(4):
        for n in range(4):
            init = pyglet.image.load(Path(game_location + '/images/' + ML[3-n][u] + '.png'))
            init_grid = pyglet.image.ImageGrid(init, 1, 4)
            image_store[ML[3-n][u]] = init_grid
#python C:\Users\micha\Documents\GitHub\oc-2018-master\games2\wordament\WORDAMENT.py
# Initialization of the game :
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
music = pyglet.media.load(game_location + '/images/music.wav')
looper = pyglet.media.SourceGroup(music.audio_format, None)
music_player = pyglet.media.Player()
looper.queue(music)
music_player.queue(looper)
looper.loop = True
music_player.play()
music_player.volume = 0.25
new_word_print = pyglet.text.Label('Word : ', font_size=28, x=5, y=612)
score_print = pyglet.text.Label('Score : 0', font_size=28, x=400, y=612)

############################################
########## Start of the game code ##########
############################################

# Actions when the game start to create the game board :
@window.event
def on_draw():
    window.clear()
    for u in range(4):
        for n in range(4):
            letter = image_store[ML[3-n][u]]
            if M_NUL[3-n][u] == 1:
                letter_print = letter[2]
                letter_print.blit(x= pattern_size/4 * u, y=pattern_size/4 * n, height=pattern_size/4, width=pattern_size/4)
            elif M_NUL[3-n][u] == 0:
                letter_print = letter[0]
                letter_print.blit(x= pattern_size/4 * u, y=pattern_size/4 * n, height=pattern_size/4, width=pattern_size/4)
    new_word_print.draw()
    score_print.draw()

# Actions when the click of the mouse is release :
@window.event 
def on_mouse_release(x, y, button, modifiers):
    global old_case
    global new_word
    global M_NUL
    global score
    M_NUL = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
    old_case = [-1,-1]
    if new_word not in taken_words and check_existence(new_word) and len(new_word) > 2:
            right = pyglet.media.load(Path(game_location + '/images/right.wav'))
            right.play()
            
            for letter in new_word:
                score += levels.score_number[letter]
            score += levels.length_bonus[len(new_word)]
            print('Bonus de longueur:', levels.length_bonus[len(new_word)])
            print(new_word)
            score_print.text = "Score : " + str(score)
            taken_words.append(new_word)
    new_word = ""
    new_word_print.text = "Word : " + new_word
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
                if pattern_size/40 + pattern_size/4 * k < y < ((k+1) * pattern_size/4 ) - pattern_size/40 and  pattern_size/40 + pattern_size/4 * i < x < ((i+1) * pattern_size/4) - pattern_size/40 and M_NUL[3-k][i] == 0:
                    if old_case == [-1, -1] or ((old_case[0] - 2) < k < (old_case[0] + 2) and (old_case[1] - 2) < i < (old_case[1] + 2)): 
#                        print(old_case)
                        # print(ML[3-k][i])
                        M_NUL[3-k][i] = 1
                        new_word += (ML[3-k][i])
                        old_case = [k, i]
                        new_word_print.text = "Word : " + new_word
                    

def check_existence(search):
    search = str(search + '\r\n')
    search = search.lower()
    fo = codecs.open(game_location + '/levels/dico.txt', 'r', 'utf-8')
    string = fo.readlines()
    string = set(string)
    if search in string:
        return True
###########################################
########## Launching of the game ##########
###########################################

pyglet.app.run()