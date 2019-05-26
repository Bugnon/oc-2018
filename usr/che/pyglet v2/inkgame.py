import math, pyglet, inktilities, inkentities
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

game_objects = []
###### x ######

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
        '1':pyglet.media.load('./resources/music/How it Begins.wav', streaming=False),
        '2':pyglet.media.load('./resources/music/Furious Freak.wav', streaming=False)
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
    word_amount = [0, 0]
    word_created = 0
    word_list = []
    object_list = []

    def level_creation():    
        GameWindow.pen = inkentities.Pen(batch=GameWindow.batch)
    
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
    
    def object_cleanup():
        for to_remove in [obj for obj in GameWindow.object_list if obj.dead]:
        
            # Remove the object from any batches it is a member of
            to_remove.delete()

            # Remove the object from our list
            GameWindow.object_list.remove(to_remove)

    def addword(dt):
        text = 'test'
        word = inkentities.FloatingLabel(text, batch = GameWindow.batch)
        if GameWindow.word_amount[0] > GameWindow.word_amount[1]:
            GameWindow.word_amount[1] += 1
            word.kind = 1
        else:
            GameWindow.word_amount[0] += 1
            word.kind = 0
        GameWindow.word_list.append(word)
        GameWindow.object_list.append(word)
        GameWindow.word_created = 0

    def create_ink():
        ink_x = GameWindow.pen.x + GameWindow.pen.width / 2
        ink_y = GameWindow.pen.y - GameWindow.pen.height / 2
        ink = inkentities.Ink(x = ink_x, y = ink_y, batch = GameWindow.batch)
        ink.dx = (window_width / ink.width) / 10 + GameWindow.pen.dx / 2
        SoundPlayer.fire_sound[randint(1, 6)].play()
        GameWindow.object_list.append(ink)

    def update(keys):
        GameWindow.vertex_cleanup()
        GameWindow.object_cleanup()
        inkentities.Pen.update(GameWindow.pen, keys)
        for entity in GameWindow.object_list:
            entity.update(entity)
        try:
            GameWindow.vertex_limit = inktilities.drawLimitLine(window_height, GameWindow.pen)
            pyglet.graphics.Batch.migrate(GameWindow.vertex_limit, GameWindow.vertex_limit, pyglet.gl.GL_LINES, None, GameWindow.batch)
        except:
            pass
        try:
            GameWindow.vertex_chargebar = inktilities.drawChargeBar(GameWindow.pen, inkentities.Pen)
            pyglet.graphics.Batch.migrate(GameWindow.vertex_chargebar, GameWindow.vertex_chargebar, pyglet.gl.GL_LINES, None, GameWindow.batch)
        except:
            pass
        if (GameWindow.word_amount[0] or GameWindow.word_amount[1]) < 5 and GameWindow.word_created == 0:
            pyglet.clock.schedule_once(GameWindow.addword, 1.5)
            GameWindow.word_created = 1
        else:
            pass
        if inkentities.Pen.spawnink == True:
            GameWindow.create_ink()
            inkentities.Pen.spawnink = False
        else:
            pass
        GameWindow.collision()
    
    def collision():
        for i in range(len(GameWindow.object_list)):
            for j in range(i + 1, len(GameWindow.object_list)):

                obj_1 = GameWindow.object_list[i]
                obj_2 = GameWindow.object_list[j]

                # Make sure the objects haven't already been killed
                if not obj_1.dead and not obj_2.dead:
                    #Checks if object 1 is text and object 2 ink/splatter, in order to use the special text hitbox formula
                    if obj_1.__class__ is inkentities.FloatingLabel and obj_2.is_ink == True:
                        obj = [obj_1.content_width, obj_1.content_height]
                        if (obj_1.y - obj[1]/10 <= obj_2.y + obj_2.height <= obj_1.y + obj[1]*1.5) and (obj_1.x <= obj_2.x <= obj_1.x + obj[0]):
                            obj_1.dead = True
                            if obj_1.kind == True:
                                GameWindow.word_amount[0] += -1
                                SoundPlayer.levelup_sound.play()
                                #if vers[score] == "X":
                                #    score+=1
                                #    levelup_sound.play()
                                #    level += 1
                                #    verse.text = "Vers " + str(level) + " | "
                                #else:
                                #    verse.text = verse.text + " " + vers[score]
                                #    score += 1
                            elif obj_1.kind == False:
                                GameWindow.word_amount[1] += -1
                                SoundPlayer.rip_sound.play()
                            #If it's ink, it should splatter
                            if obj_2.__class__ is inkentities.Ink: 
                                GameWindow.object_list.append(obj_2.splatter(GameWindow.batch))
                                obj_2.dead = True
                            else:
                                SoundPlayer.splatter_sound[randint(1, 6)].play()
                    #Checks if both objects are Ink -> Splatter
                    elif obj_1.__class__ is inkentities.Ink and obj_2.__class__ is inkentities.Ink:
                        if inktilities.distance((obj_1.x, obj_1.y), (obj_2.x, obj_2.y)) < obj_1.width/2:
                            obj_1.dead = True
                            GameWindow.object_list.append(obj_1.splatter(GameWindow.batch))
                            obj_2.dead = True


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

