import pyglet
from pyglet import font, image
from rotatingsprite import RotatingSprite, Player
font.add_file('resources/Angelface.otf')
Angelface = font.load('Angelface', 16)


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Set up a window
rapportparchemin = 3506/2480
x = 1200
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

def write_poetry():
    txt = open("resources/poeme.txt", "r")
    saut = 0
    for line in txt:
        saut = saut+15*x/800
        poeme = pyglet.text.Label(line,
                            font_name='Angelface',
                            font_size=14*x/800,
                            color=(0, 0, 50, 255),
                            x=x-290*x/800, y=y-30*x/800-saut)
        poeme.draw()


game_window.push_handlers(player_ink)


@game_window.event
def on_draw():
    game_window.clear()
    player_ink.draw()
    parchemin_sprite.draw()
    write_poetry()

def update(dt):
    player_ink.update(dt)

if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    # Tell pyglet to do its thing
    pyglet.app.run()