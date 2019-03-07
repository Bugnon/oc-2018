# 04 : create a window and display the key pressed
import pyglet

window = pyglet.window.Window(800, 200)
msg = 'Keyboard input'
label = pyglet.text.Label(msg, font_size=36, x=20, y=20)

@window.event
def on_key_press(symbol, modifiers):
    msg = 'Symbol={}, mod={}'.format(symbol, modifiers) 
    label.text = msg
    print(msg)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()