# 02 : create a window and show an image
import pyglet

window = pyglet.window.Window(900, 900)
image = pyglet.resource.image('kitten.png')
image.width = 900
print(image)

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()