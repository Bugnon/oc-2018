"""
pyglet examples

Raphael Holzer
14. 2. 2019

Tutorial:
https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html
"""

import pyglet
from pyglet.window import key
from pyglet.window import mouse


print(dir(key))

# create a window object
window = pyglet.window.Window()
# print(dir(window))

win2 = pyglet.window.Window()

# create a text label object
label = pyglet.text.Label('Hello world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


image = pyglet.resource.image('kitten2.png')


@window.event
def on_draw():
    window.clear()
    label.draw()
    
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('A was pressed')
    elif symbol == key.LEFT:
        print('LEFT arrow was pressed')
    elif symbol == key.ENTER:
        print('ENTER was pressed')
        
   
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('the LEFT mouse button was pressed.')
        
@win2.event
def on_draw():
    win2.clear()
    image.blit(0, 0)


window.push_handlers(pyglet.window.event.WindowEventLogger())

pyglet.app.run()

