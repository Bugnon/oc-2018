# 06 : create a window and play music
import pyglet

window = pyglet.window.Window(800, 200)
msg = 'Play music'
label = pyglet.text.Label(msg, font_size=36, x=20, y=20)
music = pyglet.resource.media('soundbible-person-whistling-at-girl-daniel_simon.mp3')
player = music.play()

@window.event
def on_key_press(symbol, modifiers):
    label.text = 'Stop music'
    player.pause()

@window.event
def on_draw():
    window.clear()
    label.draw()



pyglet.app.run()
