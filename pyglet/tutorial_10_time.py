# Keeping track of time
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/time.html

import pyglet
from random import randint
from pyglet.window import key

words = ['Mario', 'Zelda', 'Donkey', 'Kong', 'Super', 'Yoshi', 'Pikachu', 'Luigi', 'Sonic', 'Link', 'Peach']

#window = pyglet.window.Window(800, 600)
window = pyglet.window.Window(fullscreen=True)  # quit game with Escape key

msg = 'Press Escape to quit'
message = pyglet.text.Label(msg, font_size=12, x=10, y=10)
music = pyglet.resource.media('SuperMario.mp3')
player = music.play()
fps_display = pyglet.window.FPSDisplay(window)
dt = 0.1
dx = 50

# create a list of labels
labels = []
for word in words:
    dx = 50
    x = randint(0, window.width)
    y = randint(0, window.height)
    size = randint(12, 36)
    col = (randint(0, 255), randint(0, 255), randint(0, 255), 255)
    label = pyglet.text.Label(word, font_size=size, x=x, y=y, color=col, anchor_x='center', anchor_y='center')
    label.dx = randint(-dx, dx)
    label.dy = randint(-dx, dx)
    labels.append(label)

def init_size(labels):
    for label in labels:
        label.font_size = randint(12, 36)

def init_position(labels):
    for label in labels:
        label.x = randint(0, window.width)
        label.y = randint(0, window.height)

def init_speed(labels):
    for label in labels:
        label.dx = randint(-dx, dx)
        label.dy = randint(-dx, dx)

def modify_speed(d):
    for label in labels:
        label.dx *= d
        label.dy *= d

@window.event
def on_key_press(symbol, modifiers):
    global player, window

    if symbol == key.R:
        message.text = 'Random position'
        init_position(labels)

    elif symbol == key.RIGHT:
        message.text = 'Random displacement'
        d = 50
        for label in labels:
            label.x += randint(-d, d)
            label.y += randint(-d, d)

    elif symbol == key.LEFT:
        message.text = 'Random size'
        for label in labels:
            label.font_size = randint(12, 36)

    elif symbol == key.UP:
        message.text = 'Zoom in'
        for label in labels:
            label.font_size = int(1.2 * label.font_size)

    elif symbol == key.DOWN:
        message.text = 'Zoom out'
        for label in labels:
            label.font_size = int(0.8 * label.font_size)

    elif symbol == key.C:
        message.text = 'Random color'
        for label in labels:
            label.color = (randint(0, 255), randint(0, 255), randint(0, 255), 255)
    
    elif symbol == key.D:
        message.text = 'New directions'
        init_speed(labels)

    elif symbol == key.S:
        message.text = 'Pause music'
        player.pause()

    elif symbol == key.P:
        message.text = 'Play music'
        player.play()

    elif symbol == key.M:
        message.text = 'Reload music'
        player = music.play()

@window.event
def update(dt):
    for label in labels:
        label.x += label.dx * dt
        label.y += label.dy * dt
        if label.x < 0 or label.x > window.width:
            label.dx *= -1
        if label.y < 0 or label.y > window.height:
            label.dy *= -1

@window.event
def on_draw():
    window.clear()
    fps_display.draw()
    for label in labels:
        label.draw()
    message.draw()

pyglet.clock.schedule_interval(update, dt)
pyglet.app.run()