import pyglet
import math
from pyglet import font
font.add_file('resources/Handwriting.ttf')
Handwriting = font.load('Janda Elegant Handwriting', 16)


rapportparchemin = 3506/2480
x = 1400
y = int(x*9/16)
game_window = pyglet.window.Window(x, y)
pos = x-y/rapportparchemin

parchemin = pyglet.resource.image('resources/parchemin.png')
parchemin.height = y
parchemin.width = y/rapportparchemin

# utilisation de la classe Sprite telquel
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/modules/sprite.html?highlight=sprites
circle_segment = pyglet.resource.image("resources/circle_segment.png")
circle_segment.anchor_x = circle_segment.width//2
circle_segment.anchor_y = circle_segment.height//2

batch = pyglet.graphics.Batch()

segments = []
xc, yc = ((x-y/rapportparchemin)//2, y/2)
r = x/4
for i in range(15):
    angle_degrees = (360/15)*i
    angle_radians = math.radians(angle_degrees)
    x_segment = xc + r * math.sin(angle_radians)
    y_segment = yc + r * math.cos(angle_radians)
    segment = pyglet.sprite.Sprite(img=circle_segment, x=x_segment, y=y_segment, batch=batch)
    segment.rotation = angle_degrees
    segment.scale = 0.55*x/1200
    segments.append(segment)

def update(dt):
    global angle_degrees
    angular_velocity = 15 # degrees per second
    angle_degrees += angular_velocity



# définition d'une nouvelle classe
class FloatingSprites(pyglet.sprite.Sprite):
    def __init__(self):
        pass


def write_poetry():
    txt = open("resources/poeme.txt", "r")
    poetry = pyglet.text.Label(str(txt.read()),
                          font_name='Janda Elegant Handwriting',
                          font_size=16,
                          x=0, y=0)
    poetry.draw()

@game_window.event
def on_draw():
    game_window.clear()
    parchemin.blit(pos, 0)
    write_poetry()
    batch.draw()

pyglet.app.run()