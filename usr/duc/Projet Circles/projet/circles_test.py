##### IMPORT #####
import pyglet, random, math
from pyglet import font
from classes_test import Player, Feather, RotatingSprite, Window, Poetry

##### USEFUL SIMPLE FUNCTIONS #####
def center_image(image):
    """
    Sets an image's anchor point to its center
    :param image: image
    :return: None
    """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def distance(point_1=(0, 0), point_2=(0, 0)):
    '''
    Calculates the distance between two points.
    :param point_1: tuple
    :param point_2: tuple
    :return: float
    '''
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)

##### FONT #####
#font.add_file('resources/font/Angelface.otf')
#Angelface = font.load('Angelface', 14)

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

##### WALLPAPER #####
wallpaper = pyglet.resource.image('resources/sprites/wallpaper.jpg')
wallpaper_sprite = pyglet.sprite.Sprite(img=wallpaper, x=0, y=0)

##### BATCH #####
batch = pyglet.graphics.Batch()

##### PARCHMENT #####
parchment_image = pyglet.resource.image('resources/sprites/parchment.png')
center_image(parchment_image)
parchment_scale = parchment_image.height/parchment_image.width #Scale of the parchment
parchment = pyglet.sprite.Sprite(img=parchment_image, x=x//2, y=parchment_image.height//2 + 20)

##### PLAYER #####
player_image = pyglet.resource.image('resources/sprites/player.png')
center_image(player_image)
player_sprite = Player(img=player_image, x=x//2, y=(y+2*parchment.y)//2, batch=batch)
game_window.push_handlers(player_sprite)

##### CIRCLE SEGMENTS #####
circle_segment = pyglet.image.load("resources/sprites/circle_segment.png")
center_image(circle_segment)
#Load the 15 segments with the RotatingSprite class
for i in range(15):
    angle_degrees = (360/15)*i
    angle_radians = math.radians(angle_degrees)
    xc, yc = (x//2, (y+2*parchment.y)//2)
    r = x//6
    segment = RotatingSprite(angle_radians=angle_radians,
                            r=r, xc=xc, yc=yc,
                            word=RotatingSprite.words[i], img=circle_segment, batch=batch)
    segment.scale = r/540
    RotatingSprite.segments.append(segment)

##### POETRY #####
poem = Poetry()
poem.save_words()

##### GAME FUNCTIONS #####
def write_towards(poetry):
        remove_word = poetry.open_words()
        toward = poetry.split_poetry()
        msg = ' '.join(toward[0])
        label = pyglet.text.Label(str(msg),
                          font_name='Times New Roman',
                          font_size=18,
                          color=(75, 0, 130, 255),
                          x=parchment.x, y=parchment.y,
                          anchor_x='center', anchor_y='center')
        label.draw()

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

@game_window.event
def on_draw():
    '''
    The draw function.
    :return: None
    '''
    game_window.clear()
    wallpaper_sprite.draw()
    game_window.fps_display.draw()
    parchment.draw()
    #Draw the player and the segments
    batch.draw()
    write_towards(poem)
    #Draw the segments
    for segment in RotatingSprite.segments:
        segment.label.draw()
    #Draw the reloading line
    chargeBar(player_sprite, player_image)
    #Draw every projectile
    for feather in Feather.feathers:
        feather.draw()
    for obj in RotatingSprite.intert_objects:
        obj.draw()

def update(dt):
    '''
    Updates the game objects every frame (60 times per second)
    :param dt: float
    :return: None
    '''
    player_sprite.update(dt)
    for segment in RotatingSprite.segments:
        segment.update(dt)
    for dead_segment in RotatingSprite.dead_segments:
        dead_segment.update(dt)
    for obj in RotatingSprite.intert_objects:
        obj.update(dt)


    ### Try the collision
    for feather in Feather.feathers:
        r_max = r - segment.height/2 - feather.height/2
        if distance(point_1=(player_sprite.x, player_sprite.y), point_2=(feather.x, feather.y)) >= r_max:
            feather.dead = True

if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, game_window.frame_rate) #Activate the update function (60 Hz)

    music.queue(musicSource)
    music.play()

    pyglet.app.run()