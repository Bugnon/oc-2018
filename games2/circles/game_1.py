import pyglet

# Set up a window
x = 1000
y = x*9/16
game_window = pyglet.window.Window(x, y)

@game_window.event
def on_draw():
    game_window.clear()


pyglet.app.run()