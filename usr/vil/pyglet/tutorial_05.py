# 05 : create a window and display the mouse actions
import pyglet

window = pyglet.window.Window(800, 200)
msg = 'Mouse input'
label = pyglet.text.Label(msg, font_size=36, x=20, y=20)

@window.event
def on_mouse_press(x, y, button, modifiers):
    msg = '({}, {})'.format(x, y) 
    label.text = msg

    label.x = x
    label.y = y

    print(msg)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()