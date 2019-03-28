import pyglet
from pyglet import font, image
font.add_file('resources/Handwriting.ttf')
Handwriting = font.load('Janda Elegant Handwriting', 16)


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Set up a window
rapportparchemin = 3506/2480
x = 1000
y = int(x*9/16)
game_window = pyglet.window.Window(x, y)
pyglet.gl.glClearColor(1,1,1,1)

parchemin_image = pyglet.resource.image('resources/parchemin2.png')
parchemin_image.lengh = y
parchemin_image.width = y/rapportparchemin
parchemin_sprite = pyglet.sprite.Sprite(img=parchemin_image, x=x-y/rapportparchemin, y=0)

player_image = pyglet.resource.image("resources/encrier.png")
center_image(player_image)
player_ink = pyglet.sprite.Sprite(img=player_image, x=(x-y/rapportparchemin)/2, y=y/2)


@game_window.event
def on_draw():
    game_window.clear()
    player_ink.draw()
    parchemin_sprite.draw()
    label = pyglet.text.Label('Hello, world',
                          font_name='Janda Elegant Handwriting',
                          font_size=16,
                          x=0, y=0)
    label.draw()

pyglet.app.run()