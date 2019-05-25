import pyglet, random, math, time, inktilities, inkgame
from pyglet.window import key, mouse
from pyglet import clock
from random import randint

pyglet.options['audio'] = ('openal', 'silent')

window = inkgame.CurrentWindow.window
batch = inkgame.CurrentWindow.batch
keys = key.KeyStateHandler()
window.push_handlers(keys)
pyglet.gl.glLineWidth(4)

class MainSequence():
    
    def game():
        inkgame.SoundPlayer.playMusic('1')
        inkgame.GameWindow.level_creation()
        inkgame.CurrentWindow.window = inkgame.GameWindow.window
        inkgame.CurrentWindow.batch = inkgame.GameWindow.batch

    def resume():
        inkgame.CurrentWindow.window = inkgame.GameWindow.window
        inkgame.CurrentWindow.batch = inkgame.GameWindow.batch

    def pause():
        inkgame.CurrentWindow.window = inkgame.PauseWindow.window
        inkgame.CurrentWindow.batch = inkgame.PauseWindow.batch
    
    def main_menu():
        inkgame.SoundPlayer.playMusic('menu')
        inkgame.CurrentWindow.window = inkgame.MenuWindow.window
        inkgame.CurrentWindow.batch = inkgame.MenuWindow.batch



@window.event
def on_draw():
    global window
    global batch
    inkgame.CurrentWindow.update(keys)
    window = inkgame.CurrentWindow.window
    batch = inkgame.CurrentWindow.batch
    window.push_handlers(keys)
    window.clear()
    batch.draw()

def update(x):
    #inkgame.CurrentWindow.update(keys)
    pass

@window.event
def on_mouse_press(x, y, button, modifiers):
    if inkgame.CurrentWindow.window == inkgame.MenuWindow.window :
        MainSequence.game()

@window.event
def on_key_press(pressed_key, modifiers):
    inkgame.CurrentWindow.keypress(pressed_key)
    if pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.PauseWindow.window:
        MainSequence.resume()
    elif pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.GameWindow.window:
        MainSequence.pause()
    elif pressed_key == pyglet.window.key.ESCAPE:
        exit()


pyglet.clock.schedule_interval(update, 1/60)
MainSequence.main_menu()
pyglet.app.run()
