import math, gc, pyglet, inktilities, inkentities
from random import randint
from pyglet import clock
from pyglet.window import key, mouse

####### RESSOURCES #######

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

###### END RESSOURCES ######

###### VARIABLES ######

# Get screen size
window_width = inktilities.screenInfo("x")
window_height = inktilities.screenInfo("y")

###### CLASSES ######

class SoundPlayer():
    '''Handles the soundtrack and sound effect.'''
    player = pyglet.media.Player()
    playing = 0

    #Sets up a list of sounds to play when firing
    fire_sound = []
    for i in range(7):
        fire_sound.append(pyglet.media.StaticSource(pyglet.media.load('./resources/sounds/WaterDrop0' + str(i) + '.wav', streaming=False)))

    #Sets up a list of sounds to play when an ink blob splatters
    splatter_sound = []
    for i in range(7):
        splatter_sound.append(pyglet.media.StaticSource(pyglet.media.load('./resources/sounds/Splatter0' + str(i) + '.wav', streaming=False)))

    levelup_sound = pyglet.media.StaticSource(pyglet.media.load('./resources/sounds/Levelup.wav', streaming=False))
    rip_sound = pyglet.media.StaticSource(pyglet.media.load('./resources/sounds/Rip.wav', streaming=False))

    music = {
        'menu':pyglet.media.load('./resources/music/Deliberate Thought.wav', streaming=False),
        'game':pyglet.media.load('./resources/music/How it Begins.wav', streaming=False),
        'win':pyglet.media.load('./resources/music/Digital Lemonade.wav', streaming=False)
        }

    player.volume = 1

    def playMusic(music):
        '''Plays the soundtrack located at index music in the music[] dictionnary'''
        
        SoundPlayer.player.delete()

        # Skips a song if playing currently and adds the selected one to the queue
        SoundPlayer.player.next_source()
        SoundPlayer.player.queue(SoundPlayer.music[music])
        SoundPlayer.player.play()
        SoundPlayer.playing = 1

    def update():
        '''Ensures the music player keeps playing the soundtrack if it is supposed to (playing == 1)'''
        if SoundPlayer.playing == 1 and not SoundPlayer.player.playing:
            SoundPlayer.player.play()

class GameWindow():
    '''Manages the game window'''
    window = pyglet.window.Window(fullscreen = True)
    batch = pyglet.graphics.Batch()
    verse_text = [line.rstrip('\n') for line in open('./resources/txt/verse.txt')]
    verse = pyglet.text.Label(
        'Vers |',
        x = window_width / 100, 
        y = window_height - (window_height / 30), 
        font_size = window_height / 40,
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        batch = batch
        )
    vertex_UI = inktilities.init_ui(window_height, window_width)
    pyglet.graphics.Batch.migrate(vertex_UI, vertex_UI, pyglet.gl.GL_LINES, None, batch)
    vertex_limit = None
    vertex_chargebar = None
    word_amount = [0, 0]
    word_created = 0
    word_list = []
    object_list = []
    ink_list = []
    score = 0
    negscore = 0
    level = 1
    won = 0

    def level_creation():
        '''Initializes the level'''    
        GameWindow.pen = inkentities.Pen(batch=GameWindow.batch)
        GameWindow.object_list.append(GameWindow.pen)
        GameWindow.vertex_limit = inktilities.init_limit_vertex()
        pyglet.graphics.Batch.migrate(GameWindow.vertex_limit, GameWindow.vertex_limit, pyglet.gl.GL_LINES, None, GameWindow.batch)
        GameWindow.vertex_chargebar = inktilities.init_chargebar()
        pyglet.graphics.Batch.migrate(GameWindow.vertex_chargebar, GameWindow.vertex_chargebar, pyglet.gl.GL_LINES, None, GameWindow.batch)
    
    def keypress(pressed_key):
        '''Forwards keypresses to the pen'''
        inkentities.Pen.keypress(GameWindow.pen, pressed_key)
    
    def object_cleanup():
        '''Removes dead objects from lists and batch'''
        for to_remove in [obj for obj in GameWindow.object_list if obj.dead]:
        
            # Remove the object from any batches it is a member of
            to_remove.delete()

            # Remove the object from our list
            GameWindow.object_list.remove(to_remove)

    def addword(dt):
        '''Creates a word of the missing kind'''
        word = inkentities.FloatingLabel.create_word(GameWindow.word_amount, GameWindow.batch)
        GameWindow.object_list.append(word)
        GameWindow.word_list.append(word)
        GameWindow.word_created = 0

    def create_ink():
        '''Creates an ink bullet'''
        ink = GameWindow.pen.fire(GameWindow.pen, GameWindow.batch)
        GameWindow.object_list.append(ink)
        GameWindow.ink_list.append(ink)
        SoundPlayer.fire_sound[randint(1, 6)].play()

    def update(keys):
        '''Forwards the held keys update to the pen and update all the game objects and vertices'''
        inkentities.Pen.update(GameWindow.pen, keys)
        for entity in GameWindow.object_list:
            if entity.__class__ is not inkentities.Pen:
                entity.update(entity)
        GameWindow.vertex_limit.vertices[:] = inktilities.update_limit_vertex(window_height, GameWindow.pen)
        GameWindow.vertex_chargebar.vertices[:] = inktilities.update_chargebar(GameWindow.pen, inkentities.Pen)

    def slow_update():
        '''Called every 5th of a second for better performances, checks the collision and the amount of words present, initiates cleanup'''
        if (GameWindow.word_amount[0] < 5) or (GameWindow.word_amount[1] < 5) and GameWindow.word_created == 0:
            GameWindow.word_created = 1
            pyglet.clock.schedule_once(GameWindow.addword, 1.5)
        if inkentities.Pen.spawnink == True:
            GameWindow.create_ink()
            inkentities.Pen.spawnink = False
        GameWindow.word_collision()
        GameWindow.ink_collision()
        GameWindow.object_cleanup()
    
    def word_collision():
        '''Checks if a bullet collides with a word'''
        for i in range(len(GameWindow.ink_list)):
            for j in range(len(GameWindow.word_list)):
                obj_1 = GameWindow.ink_list[i]
                obj_2 = GameWindow.word_list[j]

                if not obj_1.dead and not obj_2.dead:
                    if (obj_2.x <= obj_1.x <= obj_2.x + obj_2.content_width) and (obj_2.y - obj_2.content_height / 2 <= obj_1.y <= obj_2.y + obj_2.content_height):
                        obj_2.dead = True
                        if obj_2.kind == True:
                            GameWindow.word_amount[1] += -1
                            SoundPlayer.levelup_sound.play()
                            GameWindow.update_verse()
                        else:
                            GameWindow.word_amount[0] += -1
                            GameWindow.negscore += 1
                            SoundPlayer.rip_sound.play()
                        if obj_1.__class__ is inkentities.Ink:
                            splatter = obj_1.splatter(GameWindow.batch, obj_2.kind)
                            GameWindow.object_list.append(splatter)
                            GameWindow.ink_list.append(splatter)
                            SoundPlayer.splatter_sound[randint(1, 6)].play()
                            obj_1.dead = True
                        else:
                            SoundPlayer.splatter_sound[randint(1, 6)].play()

    def ink_collision():
        '''Check if a bullet collides with another'''
        for i in range(len(GameWindow.ink_list)):
            for j in range(i + 1, len(GameWindow.ink_list)):
                obj_1 = GameWindow.ink_list[i]
                obj_2 = GameWindow.ink_list[j]

                if not (obj_1.dead or obj_1.__class__ == inkentities.Splatter) and not (obj_2.dead or obj_2.__class__ == inkentities.Splatter):
                    if (obj_2.x - obj_2.width <= obj_1.x <= obj_2.x + obj_2.width) and (obj_2.y - obj_2.height <= obj_1.y <= obj_2.y + obj_2.height):
                        obj_2.dead = True
                        splatter = obj_1.splatter(GameWindow.batch, 2)
                        GameWindow.object_list.append(splatter)
                        GameWindow.ink_list.append(splatter)
                        SoundPlayer.splatter_sound[randint(1, 6)].play()
                        obj_1.dead = True

    def update_verse():
        '''Updates the verse at the top of the screen'''
        if GameWindow.verse_text[GameWindow.score] == "X":
            GameWindow.score += 1
            SoundPlayer.levelup_sound.play()
            GameWindow.level += 1
            GameWindow.verse.text = "Vers " + str(GameWindow.level) + " | "
        elif GameWindow.verse_text[GameWindow.score] == "XX":
            GameWindow.won = 1
        else:
            GameWindow.verse.text = GameWindow.verse.text + " " + GameWindow.verse_text[GameWindow.score]
            GameWindow.score += 1


class PauseWindow():
    '''Manages the pause window'''
    window = pyglet.window.Window(fullscreen = True)
    batch = pyglet.graphics.Batch()
    pause = pyglet.text.Label(
        'PAUSE', 
        x = window_width / 2, 
        y = window_height / 2, 
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width / 25, 
        bold = True,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center',
        batch = batch
        )
    pass

class WinWindow():
    '''Manages the win window'''
    window = pyglet.window.Window(fullscreen = True)
    batch = pyglet.graphics.Batch()
    win = pyglet.text.Label(
        'YOU WON!',
        x = window_width / 2,
        y = window_height / 2,
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width / 25,
        bold = True,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center',
        batch = batch
    )
    exit = pyglet.text.Label(
        'Exit with ESCAPE',
        x = window_width / 2,
        y = window_height / 20,
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width / 70,
        bold = True,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center',
        batch = batch
    )


class MenuWindow():
    '''Manages the menu window'''
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
    tips4 = pyglet.text.Label(
        'Quit with ESCAPE', 
        x = window_width / 2, 
        y = window_height / 20 + 3 * window_height / 20,
        font_name = ['Verdana', 'San Francisco', 'Avenir Next', 'Helvetica', 'Arial'],
        font_size = window_width / 75,
        align = 'center',
        anchor_x = 'center',
        anchor_y = 'center', 
        batch = batch
        )
    
    def update():
        '''Makes the font "breathe"'''
        x = MenuWindow.font_breathe
        MenuWindow.font_breathe = x + 0.01
        if x > window_width / 5000:
            MenuWindow.font_breathe = -x
        MenuWindow.button_start.font_size = MenuWindow.button_start.font_size + x


class CurrentWindow():
    '''Holds the variable for the window being used, and forwards some calls (like keys)'''
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
        
    def slow_update(dt):
        if CurrentWindow.window == GameWindow.window :
            GameWindow.slow_update()
