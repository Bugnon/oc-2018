# 05 : create a window and display the mouse actions
import pyglet

window = pyglet.window.Window(800, 200)
msg = 'Mouse input'
label = pyglet.text.Label(msg, font_size=36, x=20, y=20)

@window.event
def on_mouse_press(x, y, button, modifiers):
    msg = 'x={}, y={}, button={}, mod={}'.format(x, y, button, modifiers) 
    label.text = msg
    print(msg)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()