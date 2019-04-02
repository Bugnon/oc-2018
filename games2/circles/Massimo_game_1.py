import pyglet, random
from pyglet import font

font.add_file('resources/Angelface.otf')
Angelface = font.load('Angelface', 14)

# Set up a window
rapportparchemin = 3506/2480
x = 800
y = x*9/16
game_window = pyglet.window.Window(x, y)
image = pyglet.resource.image('resources/parchemin.png')
image.height = y
image.width = y/rapportparchemin
poetry = open("resources/poeme.txt")

def split_poetry():
        ListLines = poetry.readlines()
        ListWords = []
        for line in ListLines:
                words = line.split(' ')
                ListWords.append(words)

def choose_words():
        random.choice(ListWords)
def write_poetry():
        saut = 0
        for line in poetry:
                saut = saut+17
                poeme = pyglet.text.Label(line,
                                font_name='Angelface',
                                font_size=16,
                                color=(75, 0, 130, 255),
                                x=x-300, y=y-30-saut)
                poeme.draw()
def all_poetry():
        split_poetry()


@game_window.event
def on_draw():
    game_window.clear()
    image.blit(x-y/rapportparchemin, 0)
    write_poetry()
    all_poetry()


pyglet.app.run()