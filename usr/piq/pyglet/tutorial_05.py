# 05 : create a window and display the mouse actions
import pyglet

window = pyglet.window.Window(1000, 600)
msg = 'BlueRay'
label = pyglet.text.Label(msg, font_size=15, x=20, y=20)

@window.event
def on_mouse_press(x, y, button, modifiers):
    msg = '({}; {})'.format(x, y)
    label.text = msg
    label.x = x
    label.y = y


@window.event
def on_draw():
    window.clear()
    if 100 <= label.x <= 200 and 100 <= label.y <= 200:
        label.draw()

pyglet.app.run()