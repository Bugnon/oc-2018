import pyglet

# Set up a window
game_window = pyglet.window.Window(800, 600)

@game_window.event
def on_draw():
    game_window.clear()


pyglet.app.run()