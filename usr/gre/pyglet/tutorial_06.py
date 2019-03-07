import pyglet
import pyglet

window = pyglet.window.Window(800, 200)
label = pyglet.text.Label('Play Bullet sound', font_size=64)




music = pyglet.resource.media('game/resources/bullet.wav')
@window.event
def on_draw():
    window.clear()
    label.draw()

   @window.event
def on_mouse_press():
    music.play()

@window.event
def on_key_press():
    music.play()
    
pyglet.app.run()