# 02 : create a window and show an image
import pyglet

window = pyglet.window.Window(500, 433)
image = pyglet.resource.image('kitten.png')
pyglet.gl.glClearColor(1,1,1,1)
print(image)

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()