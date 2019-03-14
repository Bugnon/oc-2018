# 02 : create a window and place a label
import pyglet

window = pyglet.window.Window(800, 200)
label = pyglet.text.Label('Hello world', font_size=64)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()