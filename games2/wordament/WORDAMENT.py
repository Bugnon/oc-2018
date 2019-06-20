# File : Wordament Game
# Date : 31.03.2019
# Author : Mirko Pirona, Michael Greub et Fabian Roulin
# IMPORTANT: 0 = Menu, 1 = Normal Game, 2 = Random Game
###########################################
# Importation of the game modules
###########################################
import pyglet
from levels import levels
import codecs
from pathlib import Path
from random import randint
############################################
# Initialization of game variables
# ###########################################$


def init():
    '''game startpoint'''
    global fo, height, width, pattern_size, case_size, game_state
    global game_location, delta_center, dictionnary
    width = 800
    height = 850
    pattern_size = min(height - 55, width)
    game_location = str(Path(__file__).absolute().parent)
    game_state = 0
    delta_center = (width - pattern_size)/2
    case_size = pattern_size/4
    fo = codecs.open(game_location + '/levels/dico.txt', 'r', 'utf-8')
    dictionnary = set(fo.readlines())
    init_var()
    init_objects()


def init_var():
    '''Imported variables'''
    global new_word, score, word_coordinate, taken_words, old_case, word_state
    new_word = ''
    score = 0
    word_coordinate = []
    taken_words = []
    old_case = [-1, -1]
    word_state = 0


def random_level_generation():
    '''Create a random grid level'''
    all_letter = []
    grid = []
    for letter in levels.scrabble_letter:
        for i in range(levels.scrabble_letter[letter]):
            all_letter.append(letter)
    for i in range(4):
        line = []
        for j in range(4):
            changed_letter = all_letter.pop(randint(0, len(all_letter) -
                                                    1 - 4 * i - j))
            line.append(changed_letter)
        grid.append(line)
    return grid


def init_objects():
    global right, next_level_button, window, new_word_print, score_print
    global background_image, selected_button, random_button, menu_background
    '''Creation of different games objects and libraries'''
    window = pyglet.window.Window(width, height, resizable=True,
                                  caption='Wordament')
    # Set of the written items to initial form :
    new_word_print = pyglet.text.Label('Word : ', font_size=28, x=150, y=612)
    score_print = pyglet.text.Label('Score : 0', font_size=28, x=5, y=612)
    path = str(Path(game_location + '/images/Background.jpg'))
    background_image = pyglet.image.load(path)
    path = str(Path(game_location + '/images/bouton_selected.png'))
    selected_button = pyglet.sprite.Sprite(pyglet.image.load(path))
    path = str(Path(game_location + '/images/bouton_random.png'))
    random_button = pyglet.sprite.Sprite(pyglet.image.load(path))
    path = str(Path(game_location + '/images/next_level.png'))
    next_level_button = pyglet.sprite.Sprite(pyglet.image.load(path))
    path = str(Path(game_location + '/images/Menu_Background.jpg'))
    menu_background = pyglet.image.load(path)
    add_audio()


# Set of the music during the game :
def add_audio():
    '''Bring the music in the game through 3
       differents musics choosen randomly'''
    pyglet.options['audio'] = ('openal', 'pulse', 'directsound')
    num = randint(0, 2)
    path = str(Path(game_location + '/images/music_' + str(num) + '.wav'))
    music = pyglet.media.load(path)
    looper = pyglet.media.SourceGroup(music.audio_format, None)
    music_player = pyglet.media.Player()
    looper.queue(music)
    music_player.queue(looper)
    looper.loop = True
    music_player.play()
    music_player.volume = 0.25
init()


############################################
# Start of the game code
############################################

# Function that update the game board :


@window.event
def on_draw():
    if game_state == 0:
        # clears the screen
        window.clear()
        # draws the image on the screen
        menu_background.blit(x=0, y=0, height=window.height,
                             width=window.width)
        selected_button.update(x=window.width / 15, y=window.height / 2 - 130,
                               scale=window.width / 800 * 0.7)
        random_button.update(x=window.width - window.width / 15 -
                             selected_button.width, y=window.height / 2 - 130,
                             scale=window.width / 800 * 0.7)
        selected_button.draw()
        random_button.draw()
        title = pyglet.text.Label('Wordament', font_size=80, x=window.width//2,
                                  y=window.height / 2 + 50, anchor_x='center',
                                  font_name='Times New Roman', bold=True,
                                  color=[0, 0, 0, 255])
        title.draw()
    else:
        global word_state
        global word_coordinate
        window.clear()
        batch = pyglet.graphics.Batch()
        sprites = []
        # draws the image on the screen
        background_image.blit(x=0, y=0, height=window.height,
                              width=window.width)
        for u in range(4):
            for n in range(4):
                letter = image_store[ML[3 - n][u]]
                if word_state == 1 and [n, u] in word_coordinate:
                    letter_print = letter[1]
                    pint = pyglet.sprite.Sprite(letter_print, x=delta_center +
                                                case_size * u, y=case_size * n,
                                                batch=batch)
                    pint.update(scale=case_size / 400)
                    sprites.append(pint)
                elif word_state == 2 and [n, u] in word_coordinate:
                    letter_print = letter[3]
                    pint = pyglet.sprite.Sprite(letter_print, x=delta_center +
                                                case_size * u, y=case_size * n,
                                                batch=batch)
                    pint.update(scale=case_size / 400)
                    sprites.append(pint)
                elif [n, u] in word_coordinate:
                    letter_print = letter[2]
                    pint = pyglet.sprite.Sprite(letter_print, x=delta_center +
                                                case_size * u, y=case_size * n,
                                                batch=batch)
                    pint.update(scale=case_size / 400)
                    sprites.append(pint)
                else:
                    letter_print = letter[0]
                    pint = pyglet.sprite.Sprite(letter_print, x=delta_center +
                                                case_size * u, y=case_size * n,
                                                batch=batch)
                    pint.update(scale=case_size / 400)
                    sprites.append(pint)
        batch.draw()
        if game_state == 2:
            if window.width >= 800:
                next_level_button.update(x=delta_center + window.width -
                                         (window.width - window.height) - 145,
                                         y=window.height - 53)
            else:
                next_level_button.update(x=delta_center + window.width - 93,
                                         y=window.height - 53)
            next_level_button.draw()
        new_word_print.draw()
        score_print.draw()
        if word_state != 0:
            word_state = 0
            word_coordinate = []
            pyglet.clock.schedule_once(update, 1)


@window.event
def on_mouse_press(x, y, button, modifiers):
    global game_state, ML, image_store, level
    width, height = window.width, window.height
    if game_state == 0:
        if width / 15 < x < width / 15 + selected_button.width:
            if (height / 2 - 130 < y < height / 2 - 130 +
                    selected_button.height):
                game_state = 1
                ML = levels.L1
                level = 1
                image_store = create_image_store(ML)
        if width - width / 15 - random_button.width < x < width + width / 15:
            if height / 2 - 130 < y < height / 2 - 130 + random_button.height:
                game_state = 2
                ML = random_level_generation()
                image_store = create_image_store(ML)
    if game_state == 2:
        if (window.width - (window.width - window.height) - 145 +
                delta_center < x < window.width -
                (window.width - window.height) - 145 +
                next_level_button.width + delta_center and
                window.height - 53 < y < window.height - 53 +
                next_level_button.height):
            new_level()


# Actions when the click of the mouse is release :
@window.event
def on_mouse_release(x, y, button, modifiers):
    if game_state != 0:
        global old_case, new_word, word_coordinate, score, word_state, right
        old_case = [-1, -1]
        if (new_word not in taken_words and check_existence(new_word) and
                len(new_word) > 2):
            path = str(Path(game_location + '/images/right.wav'))
            right = pyglet.media.load(path)
            right.play()
            for letter in new_word:
                score += levels.score_number[letter]
            score += levels.length_bonus[len(new_word)]
            score_print.text = "Score : " + str(score)
            taken_words.append(new_word)
            word_state = 1
        else:
            word_state = 2
        new_word_print.text = "Word : " + new_word
        new_word = ""
        if score >= 30:
            new_level()


# Actions when the mouse is moving :

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if game_state != 0:
        global new_word
        global word_coordinate
        global old_case
        if buttons & pyglet.window.mouse.LEFT:
            for k in range(4):
                if (case_size / 10 + case_size * k < y < ((k + 1) *
                                                          case_size) -
                        case_size / 10):
                    for i in range(4):
                        if (case_size / 10 + case_size * i + delta_center < x <
                                ((i + 1) * (case_size)) - case_size / 10 +
                                delta_center):
                            if coordinate_checker(k, i):
                                word_coordinate.append([k, i])
                                new_word += (ML[3 - k][i])
                                new_word_print.text = "Word : " + new_word
                            elif len(word_coordinate) > 1:
                                    if (word_coordinate[-2][0] == k and
                                            word_coordinate[-2][1] == i):
                                        del word_coordinate[-1]
                                        new_word = new_word[:-1]
                                        new_word_print.text = ("Word : " +
                                                               new_word)


@window.event
def on_resize(width, height):
    global case_size, new_word_print, score_print, delta_center
    pattern_size = min(width, height - 55)
    delta_center = (width - pattern_size)/2
    new_word_print = pyglet.text.Label('Word : ', font_size=28,
                                       x=delta_center + 9 / 23 * pattern_size,
                                       y=height - 38)
    score_print = pyglet.text.Label('Score : ' + str(score), font_size=28,
                                    x=delta_center + 5, y=height - 38)
    case_size = pattern_size / 4


def check_existence(search):
    search = str(search + '\r\n')
    search = search.lower()
    if search in dictionnary:
        return True


def create_image_store(ML):
    image_store = {}
    for u in range(4):
        for n in range(4):
            init = pyglet.image.load(str(Path(
                game_location + '/images/' + ML[3 - n][u] + '.png')))
            init_grid = pyglet.image.ImageGrid(init, 1, 4)
            image_store[ML[3 - n][u]] = init_grid
    return image_store


def coordinate_checker(k, i):
    return ([k, i] not in word_coordinate and (word_coordinate == [] or
            ((word_coordinate[-1][0] - 2) < k <
            (word_coordinate[-1][0] + 2) and
            (word_coordinate[-1][1] - 2) < i < (word_coordinate[-1][1] + 2))))


def new_level():
    global image_store, level, ML
    init_var()
    if game_state == 1:
        level += 1
        var = "L" + str(level)
        ML = getattr(levels, var)
    else:
        ML = random_level_generation()
    image_store = {}
    image_store = create_image_store(ML)
    new_word_print.text = "Word : "
    score_print.text = "Score : "
    on_draw()


def update(dt):
    on_draw()
###########################################
# Launching of the game
###########################################
pyglet.app.run()
