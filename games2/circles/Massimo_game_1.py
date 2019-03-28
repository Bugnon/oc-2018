import pyglet
from pyglet import font

font.add_file('resources/Handwriting.ttf')
Handwriting = font.load('Janda Elegant Handwriting', 14)

# Set up a window
rapportparchemin = 3506/2480
x = 800
y = x*9/16
game_window = pyglet.window.Window(x, y)
image = pyglet.resource.image('resources/parchemin.png')
image.height = y
image.width = y/rapportparchemin

def write_poetry():
    txt = open("resources/poeme.txt", "r")
    saut = 0
    for line in txt:
        saut = saut+15
        poeme = pyglet.text.Label(line,
                            font_name='Arial',
                            font_size=9,
                            color=(75, 0, 130, 255),
                            x=x-300, y=y-30-saut)
        poeme.draw()

@game_window.event
def on_draw():
    game_window.clear()
    image.blit(x-y/rapportparchemin, 0)
    write_poetry()

pyglet.app.run()