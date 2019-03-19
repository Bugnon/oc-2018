import pyglet

# Set up a window
x = 500
y = x*9/16
game_window = pyglet.window.Window(x, y)
image = pyglet.resource.image('resources/parchemin.png')
image.height = y
image.width = y/1.4137


@game_window.event
def on_draw():
    game_window.clear()
    image.blit(x-y/1.4137, 0)


pyglet.app.run()