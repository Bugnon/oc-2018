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
music.volume = 0.005

# Create a class for the game_window
class Window(pyglet.window.Window):
    """Classe définissant une fenêtre de jeu en pleine écran à 60 FPS."""
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
parchment = pyglet.resource.image('resources/sprites/parchment.png')
parchment_scale = parchment.height/parchment.width #Scale of the parchment

#Create the player sprite with the Player class
player_image = pyglet.resource.image('resources/sprites/player.png')
center_image(player_image)
player_sprite = Player(img=player_image, x=x//2, y=y//2, batch=batch)
game_window.push_handlers(player_sprite)

#Create the circle segment image
circle_segment = pyglet.image.load("resources/sprites/circle_segment.png")
center_image(circle_segment)

segments = []

for i in range(15):
    angle_degrees = (360/15)*i
    angle_radians = math.radians(angle_degrees)
    xc, yc = (x//2, y//2)
    r = x/4
    segment = RotatingSprite(angle_radians=angle_radians, x=x, r=r, xc=xc, yc=yc, img=circle_segment, batch=batch)
    segments.append(segment)

words = ['arbre','fromage','language','beau','ramage','hôte','voix','bec','flatteur','dépens','leçon','honteux','confus','jura','tard']

def write_words():
        i = 0
        for word in words:
                if i < len(segments):
                        msg = '{}'.format(word.upper())
                        label = pyglet.text.Label(msg,
                                font_name='Times New Roman',
                                font_size=14,
                                color=(75, 0, 130, 255),
                                x=segments[i].x, y=segments[i].y,
                                anchor_x='center', anchor_y='center')
                        label.text = msg
                        i += 1
                        label.draw()

@game_window.event
def on_draw():

    game_window.clear()
    wallpaper_sprite.draw()
    game_window.fps_display.draw()
    player_sprite.draw()
    batch.draw()
    write_words()

    for projectile in player_sprite.feathers:
        projectile.draw()

def update(dt):
    global segment
    player_sprite.update(dt)
    for segment in segments:
        segment.update(dt)

    ### Try the collision
    for feather in player_sprite.feathers:
        if math.sqrt((xc - feather.x)**2 + (yc - feather.y)**2) >= r - segment.height//2 - 25:
                feather.dead = True
                
if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, game_window.frame_rate)

    music.queue(musicSource)
    music.play()

    pyglet.app.run()