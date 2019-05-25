import math, pyglet, inktilities, inkentities
from random import randint
from pyglet import clock
from pyglet.window import key, mouse

####### RESSOURCES #######

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

###### END RESSOURCES ######

###### CONFIG ######

# Get screen size
window_width = inktilities.screenInfo("x")
window_height = inktilities.screenInfo("y")

###### UTILITIES ######

class SoundPlayer():

    player = pyglet.media.Player()
    playing = 0

    fire_sound = []
    for i in range(7):
        fire_sound.append(pyglet.media.load('./resources/sounds/WaterDrop0' + str(i) + '.wav', streaming=False))

    splatter_sound = []
    for i in range(7):
        splatter_sound.append(pyglet.media.load('./resources/sounds/Splatter0' + str(i) + '.wav', streaming=False))

    levelup_sound = pyglet.media.load('./resources/sounds/Levelup.wav', streaming=False)
    rip_sound = pyglet.media.load('./resources/sounds/Rip.wav', streaming=False)
    music = {
        'menu':pyglet.media.load('./resources/music/Deliberate Thought.wav', streaming=False),
        '1':pyglet.media.load('./resources/music/Furious Freak.wav', streaming=False)
        }

    player.volume = 0.4

    def playMusic(music):
        SoundPlayer.player.delete()

        SoundPlayer.player.next_source()
        SoundPlayer.player.queue(SoundPlayer.music[music])
        SoundPlayer.player.play()
        SoundPlayer.playing = 1

    def update():
        if SoundPlayer.playing == 1 and not SoundPlayer.player.playing:
            SoundPlayer.player.play()

    def pauseMusic():
        SoundPlayer.playing = 0
        SoundPlayer.player.pause()

    def stopMusic():
        SoundPlayer.player.delete()

class GameWindow():
    window = pyglet.window.Window(fullscreen = True)
    batch = pyglet.graphics.Batch()
    verse = pyglet.text.Label(
        'Vers |',
        x = window_width / 100, 
        y = window_height - (window_height / 30), 
        font_size = window_height / 40,
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        batch=batch
        )
    vertex_UI = inktilities.drawUI(window_height, window_width) #pyglet.graphics.vertex_list(2, ('v2f', (0, window_height-(window_height/20), window_width, window_height-(window_height/20))), ('c4B', (255, 255, 255, 255) * 2))
    pyglet.graphics.Batch.migrate(vertex_UI, vertex_UI, pyglet.gl.GL_LINES, None, batch)
    vertex_limit = None
    vertex_chargebar = None

    def level_creation():    
        GameWindow.pen = inkentities.Pen(batch=GameWindow.batch)
        pass
        #create words
        #draw pen UI
    
    def keypress(pressed_key):
        inkentities.Pen.keypress(GameWindow.pen, pressed_key)

    def vertex_cleanup():
        try:
            GameWindow.vertex_limit.delete()
        except:
            pass
        try:
            GameWindow.vertex_chargebar.delete()
        except:
            pass

    def update(keys):
        GameWindow.vertex_cleanup()
        inkentities.Pen.update(GameWindow.pen, keys)
        try:
            GameWindow.vertex_limit = inktilities.drawLimitLine(window_height, GameWindow.pen)
            pyglet.graphics.Batch.migrate(GameWindow.vertex_limit, GameWindow.vertex_limit, pyglet.gl.GL_LINES, None, GameWindow.batch)
        except:
            pass
        try:
            GameWindow.vertex_chargebar = inktilities.drawChargeBar(GameWindow.pen, inkentities.Pen)
            pyglet.graphics.Batch.migrate(GameWindow.vertex_chargebar, GameWindow.vertex_chargebar, pyglet.gl.GL_LINES, None, GameWindow.batch)
            print('charging')
        except:
            pass

class PauseWindow():
    window = pyglet.window.Window(fullscreen = True)
    batch = pyglet.graphics.Batch()
    pause = pyglet.text.Label(
        'PAUSE', 
        x = window_width / 2, 
        y = window_height / 2, 
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width/25, 
        bold = True,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center',
        batch = batch
        )
    pass

class MenuWindow():
    font_breathe = 0

    window = pyglet.window.Window(fullscreen = True)
    batch = pyglet.graphics.Batch()
    
    button_start = pyglet.text.Label(
        'CLICK TO START', 
        x = window_width / 2, 
        y = window_height / 2, 
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width/25, 
        bold = True,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center',
        batch = batch
        )
    tips = pyglet.text.Label(
        'Move with ARROWS', 
        x = window_width / 2, 
        y = window_height / 20 + 2 * window_height / 20, 
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width / 75,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center', 
        batch = batch
        )
    tips2 = pyglet.text.Label(
        'Fire with SPACE', 
        x = window_width / 2, 
        y = window_height / 20 + window_height / 20, 
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width / 75,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center', 
        batch = batch
        )
    tips3 = pyglet.text.Label(
        'Pause with ENTER', 
        x = window_width / 2, 
        y = window_height / 20, 
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width / 75,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center', 
        batch = batch
        )
    
    def update():
        x = MenuWindow.font_breathe
        MenuWindow.font_breathe = x + 0.01
        if x > window_width / 5000:
            MenuWindow.font_breathe = -x
        MenuWindow.button_start.font_size = MenuWindow.button_start.font_size + x


class CurrentWindow():
    window = MenuWindow.window
    batch = MenuWindow.batch

    def keypress(pressed_key):
        if CurrentWindow.window == GameWindow.window :
            GameWindow.keypress(pressed_key)

    def update(keys):
        if CurrentWindow.window == MenuWindow.window : 
            MenuWindow.update()
        elif CurrentWindow.window == GameWindow.window : 
            GameWindow.update(keys)
        #elif CurrentWindow.window == PauseWindow.window :
        #    PauseWindow.update()

###### LEVELS ######

###### ENTITIES ######

