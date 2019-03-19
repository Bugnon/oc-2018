import pyglet
from pyglet import font
font.add_file('resources/Handwriting.ttf')
Handwriting = font.load('Janda Elegant Handwriting', 16)

# Set up a window
rapportparchemin = 3506/2480
x = 500
y = x*9/16
game_window = pyglet.window.Window(x, y)
image = pyglet.resource.image('resources/parchemin.png')
image.height = y
image.width = y/rapportparchemin


@game_window.event
def on_draw():
    game_window.clear()
    image.blit(x-y/rapportparchemin, 0)
    label = pyglet.text.Label('Hello, world',
                          font_name='Janda Elegant Handwriting',
                          font_size=16,
                          x=0, y=0)
    label.draw()

pyglet.app.run()