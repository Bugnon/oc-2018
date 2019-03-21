print('hello wolrd')

import pyglet 
print('pyglet', pyglet.version)

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world', font_name='Zapinfo', 
            font_size=48, x=100, y=100)

image = pyglet.resource.image('kitten.png')

@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0, 100)

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

@window.event
def on_draw():
    window.clear()

from pyglet.window import key

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

from pyglet.window import mouse

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')


window.push_handlers(pyglet.window.event.WindowEventLogger())

pyglet.app.run()
