# 02 : create a window and show an image
import pyglet

window = pyglet.window.Window(800, 800)
image = pyglet.resource.image('kitten.png')
image.width=700
image.height=700
print(image)

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()