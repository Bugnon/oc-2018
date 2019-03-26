import pyglet
import math
from pyglet import font
font.add_file('resources/Handwriting.ttf')
Handwriting = font.load('Janda Elegant Handwriting', 16)

rapportparchemin = 3506/2480
x = 500
y = int(x*9/16)

game_window = pyglet.window.Window(x, y)

parchemin = pyglet.resource.image('resources/parchemin.png')
parchemin.height = y
parchemin.width = y/rapportparchemin

def write_poetry():
    txt = open("resources/poeme.txt", "r")
    poetry = pyglet.text.Label(str(txt.read()),
                          font_name='Janda Elegant Handwriting',
                          font_size=16,
                          x=0, y=0)
    poetry.draw()

def spawn_circle():
    global x, y
    circle_segment = pyglet.resource.image("resources/circle_segment.png")
    circle_center_x = (x-(y/rapportparchemin))/2 - circle_segment.width/2
    circle_center_y = y/2 - circle_segment.height/2
    segment_x = (circle_center_x)*math.sin(360/15)
    segment_y = (circle_center_y+100)*math.cos(360/15)
    circle_segment.blit(segment_x, segment_y)

@game_window.event
def on_draw():
    game_window.clear()
    parchemin.blit(x-y/rapportparchemin, 0)
    write_poetry()
    spawn_circle()

pyglet.app.run()