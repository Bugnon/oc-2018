import pyglet
import math
from pyglet import font
from rotatingsprite import RotatingSprite

font.add_file('resources/Handwriting.ttf')
Handwriting = font.load('Janda Elegant Handwriting', 14)


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Set up a window
rapportparchemin = 3506/2480
game_window = pyglet.window.Window(fullscreen = True)
x = game_window.width
y = game_window.height
pyglet.gl.glClearColor(1,1,1,1)

parchemin_image = pyglet.resource.image('resources/parchemin2.png')
parchemin_image.lengh = y
parchemin_image.width = y/rapportparchemin
parchemin_sprite = pyglet.sprite.Sprite(img=parchemin_image, x=x-y/rapportparchemin, y=(game_window.height-parchemin_image.height)/2)

player_image = pyglet.resource.image("resources/encrier.png")
center_image(player_image)
player_ink = pyglet.sprite.Sprite(img=player_image, x=(x-y/rapportparchemin)/2, y=y/2)

# utilisation de la classe Sprite telquel
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/modules/sprite.html?highlight=sprites
circle_segment = pyglet.image.load("resources/circle_segment.png")
circle_segment.anchor_x = circle_segment.width//2
circle_segment.anchor_y = circle_segment.height//2

batch = pyglet.graphics.Batch()

segments = []
xc, yc = ((x-y/rapportparchemin)//2, y/2)
r = x/4
for i in range(15):
    angle_degrees = (360/15)*i
    angle_radians = math.radians(angle_degrees)

    segment = RotatingSprite(img=circle_segment, batch=batch)
    segment.angle = angle_radians
    segment.r = r
    segment.xc = xc
    segment.yc = yc
    segment.scale = 0.55*x/1200
    segments.append(segment)

words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

def write_words():
        i = 0
        for word in words:
                msg = '{}'.format(word)
                label = pyglet.text.Label(msg,
                          font_name='Times New Roman',
                          font_size=30,
                          color=(75, 0, 130, 255),
                          x=segments[i].x, y=segments[i].y,
                          anchor_x='center', anchor_y='center')
                label.text = msg
                i += 1
                label.draw()

def write_poetry():
    txt = open("resources/poeme.txt", "r")
    saut = 0
    for line in txt:
        saut = saut+15*x/800
        poeme = pyglet.text.Label(line,
                            font_name='Arial',
                            font_size=9*x/800,
                            color=(0, 0, 50, 255),
                            x=x-300*x/800, y=y-70*x/800-saut)
        poeme.draw()

@game_window.event
def on_draw():
    game_window.clear()
    player_ink.draw()
    parchemin_sprite.draw()
    write_poetry()
    batch.draw()
    write_words()

def update(dt):
    for segment in segments:
        segment.update(dt)

if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()