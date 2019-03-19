import pyglet
from pyglet.window import key
from pyglet.window import mouse

print('pyglet', pyglet.version)

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world', font_name='zapfino', font_size=36, x=100, y=15)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        label.x = x
        label.y = y

@window.event
def on_mouse_scroll(x, y, dx, dy):
    x += dx
    y += dy
    label.x = x
    label.y = y

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()