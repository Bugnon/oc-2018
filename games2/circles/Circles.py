##### IMPORT #####
import pyglet, random, math
from pyglet import font
from classes import Player, Feather, RotatingSprite, Window, Poetry
from pyglet.window import mouse

##### USEFUL SIMPLE FUNCTIONS #####
def center_image(image):
    """
    Sets an image's anchor point to its center
    :param image: image
    :return: None
    """
    image.anchor_x = image.width // 2 # put the anchor of the image at the half of its width
    image.anchor_y = image.height // 2 # put the anchor of the image at the half of its height

def distance(point_1=(0, 0), point_2=(0, 0)):
    '''
    Calculates the distance between two points.
    :param point_1: tuple
    :param point_2: tuple
    :return: float
    '''
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2) # pythagore

##### MUSIC #####
musicSource = pyglet.media.load('resources/sound/violin.wav')
music = pyglet.media.Player()
music.volume = 0.0005
#Keep playing for as long as the app is running (or you tell it to stop):
music.eos_action = pyglet.media.SourceGroup.loop

##### GAME WINDOW #####
game_window = Window()
x = game_window.width
y = game_window.height
game = False #State of the game, on or off

##### WALLPAPER #####
wallpaper = pyglet.resource.image('resources/sprites/wallpaper.jpg')
wallpaper_sprite = pyglet.sprite.Sprite(img=wallpaper, x=0, y=0)

##### MENU ####
close_img = pyglet.resource.image('resources/sprites/close_game.png')
close_img2 = pyglet.resource.image('resources/sprites/close_game_grey.png')
close_scale = close_img.height/close_img.width
close = pyglet.sprite.Sprite(img=close_img,
                            x=close_img.width*close_scale//4,
                            y=y-int(2*close_img.height*close_scale)) #set position of close image
close.scale = close_scale

restart_img = pyglet.resource.image('resources/sprites/restart_game.png')
restart_img2 = pyglet.resource.image('resources/sprites/restart_game_grey.png')
restart_scale = restart_img.height/restart_img.width
restart = pyglet.sprite.Sprite(img=restart_img,
                            x=restart_img.width*restart_scale//4,
                            y=y-int(3.5*restart_img.height*restart_scale)) #set position of restart image
restart.scale = restart_scale

##### BATCH #####
batch = pyglet.graphics.Batch()

##### PARCHMENT #####
parchment_image = pyglet.resource.image('resources/sprites/parchment.png')
center_image(parchment_image)
parchment_scale = parchment_image.height/parchment_image.width #Scale of the parchment
parchment = pyglet.sprite.Sprite(img=parchment_image,
                                x=x//2,
                                y=parchment_image.height//2 + 20)

##### PLAYER #####
player_image = pyglet.resource.image('resources/sprites/player.png')
center_image(player_image)
player_sprite = Player(img=player_image,
                        x=x//2,
                        y=(y+2*parchment.y)//2,
                        batch=batch) # set position of player as a Player instance
game_window.push_handlers(player_sprite)

##### CIRCLE SEGMENTS #####
circle_segment = pyglet.resource.image("resources/sprites/circle_segment.png")
center_image(circle_segment)
#Load the 15 segments with the RotatingSprite class
for i in range(15):
    angle_degrees = (360/15)*i # set the angle of every segment
    angle_radians = math.radians(angle_degrees)
    xc, yc = (x//2, (y+2*parchment.y)//2)
    r = x//6 #radius of the circle
    segment = RotatingSprite(angle_radians=angle_radians,
                            r=r, xc=xc, yc=yc,
                            word=RotatingSprite.words[i], img=circle_segment, batch=batch)
    RotatingSprite.segments.append(segment) #add the segment to the list which is updated

##### POETRY #####
poem = open("resources/documents/poeme.txt", encoding='utf8') # open the poem
poetry = Poetry(poem)
poetry.initialize()

##### INRODUCTION LABEL #####
intro_text = pyglet.text.Label('Press left mouse button to start',
                    font_name='Times New Roman',
                    font_size=x/30,
                    italic=True,
                    x=x//2, y=y//2,
                    anchor_x='center', anchor_y='center')

##### GAME FUNCTIONS #####
global ligne
def write_towards(poetry):
    toward = poetry.split_poetry()
    msg = ' '.join(toward[ligne]) #take the first verse
    label = pyglet.text.Label(str(msg),
            font_name='Times New Roman',
            font_size=18,
            color=(75, 0, 130, 255),
            x=parchment.x, y=parchment.y,
            anchor_x='center', anchor_y='center')
    label.draw() #write the sentence on the parchment

def chargeBar(player_sprite, player_image):
        '''
        Draws the line for the reloading time.
        :param player_sprite: sprite
        :param player_image: image
        :return: None
        '''
        player_start = player_sprite.x - player_sprite.width // 2

        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ("v2f", (player_start, player_sprite.y-(player_image.height)/1.2, player_start+2*(player_sprite.width*(player_sprite.reloading/60)), player_sprite.y-(player_image.height)/1.2))
        )
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ("v2f", (player_start, player_sprite.y-(player_image.height)/1.2+1, player_start+2*(player_sprite.width*(player_sprite.reloading/60)), player_sprite.y-(player_image.height)/1.2+1))
        )
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ("v2f", (player_start, player_sprite.y-(player_image.height)/1.2+2, player_start+2*(player_sprite.width*(player_sprite.reloading/60)), player_sprite.y-(player_image.height)/1.2+2))
        )
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ("v2f", (player_start, player_sprite.y-(player_image.height)/1.2+3, player_start+2*(player_sprite.width*(player_sprite.reloading/60)), player_sprite.y-(player_image.height)/1.2+3))
        )

def in_sprite(sprite, x, y):
    '''
    Verifies if the coordonates (x, y) are in the sprite
    :param sprite: sprite
    :param x: int
    :param y: int
    :return: bool
    '''
    res = sprite.x <= x <= sprite.x + sprite.width and sprite.y <= y <= sprite.y + sprite.height
    return res

@game_window.event
def on_draw():
    '''
    The draw function.
    :return: None
    '''
    game_window.clear()
    wallpaper_sprite.draw()
    if game:
        restart.draw()
        close.draw()
        game_window.fps_display.draw()
        parchment.draw()
        #Draw the player and the segments
        batch.draw()
        write_towards(poetry)
        #Draw the segments
        for segment in RotatingSprite.segments:
            segment.label.draw()
        #Draw the reloading line
        chargeBar(player_sprite, player_image)
        #Draw every projectile
        for feather in Feather.feathers:
            feather.draw()
        #Draw the dead feathers
        for obj in RotatingSprite.intert_objects:
            obj.draw()
    else:
        intro_text.draw()

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    global game
    if mouse.LEFT == True:
        if game: #if the game is on or off
            if in_sprite(restart, x, y): #condition to press on the button
                game_restart()
            elif in_sprite(close, x, y):
                pyglet.app.exit()
        else:
            game = True

@game_window.event
def on_mouse_motion(x, y, dx, dy):
    '''
    Controls the animation of the two buttons.
    :return: None
    '''
    if restart.image == restart_img and in_sprite(restart, x, y): #turn the image in grey when mouse is on the restart button
        restart.image = restart_img2
    elif restart.image != restart_img and not in_sprite(restart, x, y):
        restart.image = restart_img

    if close.image == close_img and in_sprite(close, x, y): #turn the image in grey when mouse is on the close button
        close.image = close_img2
    elif close.image != close_img and not in_sprite(close, x, y):
        close.image = close_img

def game_restart():
    for segment in RotatingSprite.dead_segments:  # transform all dead segments back in segments
        segment.relive()
    RotatingSprite.dead_segments.clear() # clear the dead_segment list when restart
    RotatingSprite.intert_objects.clear() # clear the dead feathers when restart

def update(dt):
    '''
    Updates the game objects every frame (60 times per second)
    :param dt: float
    :return: None
    '''
    global ligne
    if game:
        player_sprite.update(dt)
        if len(Feather.feathers) > 0:
            for feather in Feather.feathers: # update position of all dead segments
                feather.update_position(dt)
        if len(RotatingSprite.segments) > 0:
            for segment in RotatingSprite.segments: # update position of all segments
                segment.update(dt)
        if len(RotatingSprite.dead_segments) > 0:
            for dead_segment in RotatingSprite.dead_segments: # update position of all dead segments
                dead_segment.update(dt)
        if len(RotatingSprite.intert_objects) > 0:
            for obj in RotatingSprite.intert_objects: #update position of the dead feathers
                obj.update(dt)
    
        ### Collision
        for feather in Feather.feathers:
            already_dead = False #prevent the delete of two segments with the same feather
            if distance(point_1=(feather.x, feather.y), point_2=(xc, yc)) > r - circle_segment.height//2: # check when a feather reaches the segments 
                feather.dead = True # kill the feather
                if len(RotatingSprite.segments) > 0:
                    for segment in RotatingSprite.segments:
                        if distance(point_1=(feather.x, feather.y), point_2=(segment.x, segment.y)) <  1.26 * r * math.sin(math.radians(360/15)/2): # check which segments is hit by the feather
                            if not already_dead: # kill the segment if the feather has not kill one already
                                if segment.word == RotatingSprite.words[0]:
                                    ligne += 1
                                    segment.dead = True
                                    segment.update(dt) # update the next segment in segment list (to prevent a bug)
                                    already_dead = True
                                else:
                                    pass
                else:
                    print('Win')
    else:
        pass

if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, game_window.frame_rate) #Activate the update function (60 Hz)

    music.queue(musicSource)
    music.play()
 
    pyglet.app.run()
