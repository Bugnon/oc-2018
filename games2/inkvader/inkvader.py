import pyglet, random, math, time, inktilities, inkgame, gc, time
from time import sleep
from pyglet.window import key, mouse
from pyglet import clock
from random import randint

# Sets the drivers for the sound and music
pyglet.options['audio'] = ('openal', 'silent')

window = inkgame.CurrentWindow.window
batch = inkgame.CurrentWindow.batch
keys = key.KeyStateHandler()
window.push_handlers(keys)
pyglet.gl.glLineWidth(4)

class MainSequence():
    '''Handles the setting up and switching of windows, soundtracks and batches between different game states'''
    def game():
        inkgame.SoundPlayer.playMusic('game')
        inkgame.GameWindow.level_creation()
        inkgame.CurrentWindow.window = inkgame.GameWindow.window
        inkgame.CurrentWindow.batch = inkgame.GameWindow.batch

    def resume():
        inkgame.CurrentWindow.window = inkgame.GameWindow.window
        inkgame.CurrentWindow.batch = inkgame.GameWindow.batch

    def pause():
        inkgame.CurrentWindow.window = inkgame.PauseWindow.window
        inkgame.CurrentWindow.batch = inkgame.PauseWindow.batch
    
    def win():
        inkgame.SoundPlayer.playMusic('win')
        inkgame.GameWindow.won = 0
        inkgame.CurrentWindow.window = inkgame.WinWindow.window
        inkgame.CurrentWindow.batch = inkgame.WinWindow.batch

    def reset():
        inkgame.GameWindow.pen.delete()
        for obj in inkgame.GameWindow.object_list:
            try: obj.delete()
            except: pass
            try: GameWindow.object_list.remove(obj)
            except: pass

    def main_menu():
        inkgame.SoundPlayer.playMusic('menu')
        inkgame.CurrentWindow.window = inkgame.MenuWindow.window
        inkgame.CurrentWindow.batch = inkgame.MenuWindow.batch


@window.event
def on_draw():
    '''Refreshes and updates the window'''
    global window
    global batch

    inkgame.CurrentWindow.update(keys)
    window = inkgame.CurrentWindow.window
    batch = inkgame.CurrentWindow.batch
    window.push_handlers(keys)
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    '''Starts the game on mouseclick'''
    if inkgame.CurrentWindow.window == inkgame.MenuWindow.window :
        MainSequence.game()

@window.event
def on_key_press(pressed_key, modifiers):
    '''Forwards the pressed keys appropriately and pauses/resumes/quits the game.'''
    inkgame.CurrentWindow.keypress(pressed_key)
    if pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.PauseWindow.window:
        MainSequence.resume()
    elif pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.GameWindow.window:
        MainSequence.pause()
    elif pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.WinWindow.window:
        exit()
    elif pressed_key == pyglet.window.key.ESCAPE:
        exit()

def update(dt):
    '''Calls the @window.event event, checks if the game has been won.'''
    if inkgame.GameWindow.won == 1:
        MainSequence.win()

def collect(dt):
    '''Calls the garbage collector'''
    gc.collect

pyglet.clock.schedule_interval(update, 1/60)
pyglet.clock.schedule_interval(inkgame.CurrentWindow.slow_update, 1/10)
pyglet.clock.schedule_interval(collect, 5)
MainSequence.main_menu()
pyglet.app.run()  