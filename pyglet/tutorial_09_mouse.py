# 09: Working with the mouse
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/mouse.html

import pyglet
from pyglet.window import key

window = pyglet.window.Window()
message = pyglet.text.Label('Status message', x=10, y=10)
sprite = pyglet.text.Label()
mouse_visible = True
cursors = [c for c in dir(window) if c.startswith('CURSOR')]
i = 0

@window.event
def on_mouse_motion(x, y, dx, dy):
    message.text = 'mouse motion at ({}, {})'.format(x, y)
    sprite.text = '({}, {})'.format(x, y)
    sprite.x = x
    sprite.y = y

@window.event
def on_mouse_press(x, y, button, modifiers):
    message.text = 'mouse press at ({}, {}), button={}, mod={}'.format(x, y, button, modifiers)

@window.event
def on_mouse_release(x, y, button, modifiers):
    message.text = 'mouse release at ({}, {}), button={}, mod={}'.format(x, y, button, modifiers)

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
     message.text = 'mouse drag at ({}, {}), button={}, mod={}'.format(x, y, buttons, modifiers)   

@window.event
def on_mouse_scroll(x, y, dx, dy):
    message.text = 'mouse scroll at ({}, {}), scroll=({}, {})'.format(x, y, dx, dy)
    sprite.x += dx
    sprite.y += dy

@window.event
def on_key_press(symbol, modifiers):
    global mouse_visible, cursors, i

    if symbol == key.V:
        mouse_visible = not mouse_visible
        window.set_mouse_visible(mouse_visible)
    elif symbol == key.UP:
        i = (i + 1) % len(cursors)
        c = cursors[i]
        message.text = 'cursor: ' + c
        cursor = window.get_system_mouse_cursor(eval('window.'+c))
        window.set_mouse_cursor(cursor)
    elif symbol == key.DOWN:
        i = (i - 1) % len(cursors)
        c = cursors[i]
        message.text = 'cursor: ' + c
        cursor = window.get_system_mouse_cursor(eval('window.'+c))
        window.set_mouse_cursor(cursor)

@window.event
def on_draw():
    window.clear()
    sprite.draw()
    message.draw()

pyglet.app.run()

