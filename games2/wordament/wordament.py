# File : Wordament Game
# Date : 31.03.2019
# Author : Mirko Pirona, Michael Greub et Fabian Roulin

###########################################
##### Importation of the game modules #####
###########################################

word_state = 0
import pyglet
from levels import levels
import codecs
from pathlib import Path
############################################
###   Initialization of game variables   ###
############################################

# Screen size variables :
height = 650
width = 600
pattern_size = min(height, width)
case_size = pattern_size/4

# Variable in game :
new_word = ''
score = 0

word_coordinate = []
taken_words = []
old_case = [-1, -1]

# Imported variables :
game_location = str(Path(__file__).absolute().parent)
ML = (levels.L1)

# Creation of the window and the game board:
window = pyglet.window.Window(width, height, resizable = True)
image_store = {}
for u in range(4):
        for n in range(4):
            init = pyglet.image.load(Path(game_location + '/images/' + ML[3 - n][u] + '.png'))
            init_grid = pyglet.image.ImageGrid(init, 1, 4)
            image_store[ML[3 - n][u]] = init_grid
            
# Set of the music during the game :
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
music = pyglet.media.load(game_location + '/images/music.wav')
looper = pyglet.media.SourceGroup(music.audio_format, None)
music_player = pyglet.media.Player()
looper.queue(music)
music_player.queue(looper)
looper.loop = True
music_player.play()
music_player.volume = 0.25

# Set of the written items to initial form :
new_word_print = pyglet.text.Label('Word : ', font_size = 28, x = 5, y = 612)
score_print = pyglet.text.Label('Score : 0', font_size = 28, x = 400, y = 612)

############################################
########## Start of the game code ##########
############################################

# Function that update the game board :
def update(dt):
    on_draw()

# Actions when the game start to create the game board :
@window.event
def on_draw():
    global word_state
    global word_coordinate
    window.clear()
    print(word_state)
    for u in range(4):
        for n in range(4):
            letter = image_store[ML[3 - n][u]]
            if word_state == 1 and [n, u] in word_coordinate:
                letter_print = letter[1]
                letter_print.blit(x = case_size * u, y = case_size * n, height = case_size, width = case_size)
            elif word_state == 2 and [n, u] in word_coordinate:
                letter_print = letter[3]
                letter_print.blit(x = case_size * u, y = case_size * n, height = case_size, width = case_size)
            elif [n,u] in word_coordinate :
                letter_print = letter[2]
                letter_print.blit(x = case_size * u, y = case_size * n, height = case_size, width = case_size)
            else:
                letter_print = letter[0]
                letter_print.blit(x = case_size * u, y = case_size * n, height = case_size, width = case_size)
    new_word_print.draw()
    score_print.draw()
    if word_state != 0:
        word_state = 0
        word_coordinate = []
        pyglet.clock.schedule_once(update, 1)

# Actions when the click of the mouse is release :
@window.event
def on_mouse_release(x, y, button, modifiers):
    global old_case
    global new_word
    global word_coordinate
    global score
    global word_state
    old_case = [-1, -1]
    if new_word not in taken_words and check_existence(new_word) and len(new_word) > 2:
        right = pyglet.media.load(Path(game_location + '/images/right.wav'))
        right.play()
        for letter in new_word:
            score += levels.score_number[letter]
        score += levels.length_bonus[len(new_word)]
        score_print.text = "Score : " + str(score)
        taken_words.append(new_word)
        word_state = 1  
    else:
        word_state = 2

    new_word = ""
    new_word_print.text = "Word : " + new_word
    
    
# Actions when the mouse is moving :


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global new_word
    global word_coordinate
    global old_case
    if buttons & pyglet.window.mouse.LEFT:
    #print(x, y, dx, dy, buttons, modifiers)
        for k in range(4):
            for i in range(4):
                if case_size / 10 + case_size * k < y < ((k + 1) * case_size ) - case_size / 10 and  case_size / 10 + case_size * i < x < ((i + 1) * case_size) - case_size / 10:
                    if [k, i] not in word_coordinate and (word_coordinate == [] or ((word_coordinate[-1][0] - 2) < k < (word_coordinate[-1][0] + 2) and (word_coordinate[-1][1] - 2) < i < (word_coordinate[-1][1] + 2))): 
                            word_coordinate.append([k, i])
                            new_word += (ML[3 - k][i])
                            new_word_print.text = "Word : " + new_word
                    elif len(word_coordinate) > 1:
                            if word_coordinate[-2][0] == k and word_coordinate[-2][1] ==i:
                                del word_coordinate[-1]
                                new_word = new_word[:-1]
                                new_word_print.text = "Word : " + new_word

@window.event 
def on_resize(width, height):
    global pattern_size, new_word_print, score_print
    pattern_size = min(width, height - 50)
    new_word_print = pyglet.text.Label('Word : ', font_size = 28, x = 5, y = height - 38)
    score_print = pyglet.text.Label('Score : ' + str(score), font_size =28, x = pattern_size - 200, y = height - 38)
    
    

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