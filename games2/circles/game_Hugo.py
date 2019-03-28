import pyglet
import math
from pyglet import font
from rotatingsprite import RotatingSprite

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

    segment = RotatingSprite(img=circle_segment, batch=batch)
    segment.angle = angle_radians
    segment.r = r
    segment.xc = xc
    segment.yc = yc
    segment.scale = 0.55*x/1200
    segments.append(segment)


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

def update(dt):
    for segment in segments:
        segment.update(dt)

if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()