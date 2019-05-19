# coding=utf-8
import pyglet, random, math
from pyglet import font
from pyglet.window import FPSDisplay
from classes_test import Player, Feather, RotatingSprite

#Add a font for the poem on the right of the window
font.add_file('resources/font/Angelface.otf')
Angelface = font.load('Angelface', 14)

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)

#import music file
musicSource = pyglet.media.load('resources/sound/violin.wav')
music = pyglet.media.Player()
music.volume = 0.0005

# keep playing for as long as the app is running (or you tell it to stop):
music.eos_action = pyglet.media.SourceGroup.loop


# Create a class for the game_window
class Window(pyglet.window.Window):
    """Classe définissant une fenêtre de jeu en pleine écran à 60 Hz."""
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.set_fullscreen(True)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)

#Set up the window with Window class
game_window = Window()
x = game_window.width
y = game_window.height

#Load the wallpaper
wallpaper = pyglet.resource.image('resources/sprites/wallpaper.jpg')
wallpaper_sprite = pyglet.sprite.Sprite(img=wallpaper, x=0, y=0)

#Create a batch and set up the parchment image
batch = pyglet.graphics.Batch()
parchment_image = pyglet.resource.image('resources/sprites/parchment.png')
center_image(parchment_image)
parchment_scale = parchment_image.height/parchment_image.width #Scale of the parchment
parchment = pyglet.sprite.Sprite(img=parchment_image, x=x//2, y=parchment_image.height//2 + 20)

#Create the player sprite with the Player class
player_image = pyglet.resource.image('resources/sprites/player.png')
center_image(player_image)
player_sprite = Player(img=player_image, x=x//2, y=(y+2*parchment.y)//2, batch=batch)
game_window.push_handlers(player_sprite)

#Create the circle segment image
circle_segment = pyglet.image.load("resources/sprites/circle_segment.png")
center_image(circle_segment)

for i in range(15):
    angle_degrees = (360/15)*i
    angle_radians = math.radians(angle_degrees)
    xc, yc = (x//2, (y+2*parchment.y)//2)
    r = x/6
    segment = RotatingSprite(angle_radians=angle_radians, x=x, r=r, xc=xc, yc=yc, word=RotatingSprite.words[i], img=circle_segment, batch=batch)
    segment.scale = r/540
    RotatingSprite.segments.append(segment)

def write_word(msg):
        label = pyglet.text.Label(str(msg),
                                font_name='Times New Roman',
                                font_size=15,
                                color=(75, 0, 130, 255),
                                x=parchment.x, y=parchment.y,
                                anchor_x='center', anchor_y='center')
        label.draw()

def chargeBar(player_sprite, player_image):
        '''Draws the line for the reloading time.'''

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

    game_window.clear()
    wallpaper_sprite.draw()
    game_window.fps_display.draw()
    player_sprite.draw()
    parchment.draw()
    batch.draw()
    write_word('Insérez la phrase')
    for segment in RotatingSprite.segments:
        segment.label.draw()
    chargeBar(player_sprite, player_image)

    for projectile in Feather.feathers:
        projectile.draw()

def update(dt):
    global segment
    player_sprite.update(dt)
    for segment in RotatingSprite.segments:
        segment.update(dt)

    ### Try the collision
    for feather in Feather.feathers:
        if math.sqrt((xc - feather.x)**2 + (yc - feather.y)**2) > segment.r - segment.height//2 - 25:
                feather.dead = True

if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, game_window.frame_rate)

    music.queue(musicSource)
    music.play()

    pyglet.app.run()