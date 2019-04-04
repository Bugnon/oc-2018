import pyglet, random
import math
from pyglet import font
from rotatingsprite import RotatingSprite, Player

font.add_file('resources/Angelface.otf')
Angelface = font.load('Angelface', 14)

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

# Set up a window
rapportparchemin = 3506/2480
game_window = pyglet.window.Window(fullscreen = True)
x = game_window.width
y = game_window.height
pyglet.gl.glClearColor(1,1,1,1)

batch = pyglet.graphics.Batch()

parchemin_image = pyglet.resource.image('resources/parchemin2.png')
parchemin_image.lengh = y
parchemin_image.width = y/rapportparchemin
parchemin_sprite = pyglet.sprite.Sprite(img=parchemin_image, x=x-y/rapportparchemin, y=(game_window.height-parchemin_image.height)/2)

wallpaper = pyglet.resource.image('resources/wallpaper.jpg')
wallpaper_sprite = pyglet.sprite.Sprite(img=wallpaper, x=0, y=0)

player_image = pyglet.resource.image("resources/encrier.png")
center_image(player_image)
player_ink = Player(img=player_image, x=(x-y/rapportparchemin)/2, y=y/2, batch=batch)

game_window.push_handlers(player_ink)

# utilisation de la classe Sprite telquel
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/modules/sprite.html?highlight=sprites
circle_segment = pyglet.image.load("resources/circle_segment.png")
circle_segment.anchor_x = circle_segment.width//2
circle_segment.anchor_y = circle_segment.height//2

segments = []
xc, yc = ((x-y/rapportparchemin)//2, y/2)
r = x/4
for i in range(15):
    angle_degrees = (360/15)*i
    angle_radians = math.radians(angle_degrees)

    segment = RotatingSprite(img=circle_segment, batch=batch)
    segment.angle = angle_radians
    segment.r = r
    segment.xc = xc
    segment.yc = yc
    segment.scale = 0.56*x/1200
    segments.append(segment)

words = ['arbre','fromage','language','beau','ramage','hôte','voix','bec','flatteur','dépens','leçon','honteux','confus','jura','tard']

poetry = open("resources/poeme.txt")

def write_words():
        i = 0
        for word in words:
                msg = '{}'.format(word)
                label = pyglet.text.Label(msg,
                          font_name='Times New Roman',
                          font_size=15,
                          color=(75, 0, 130, 255),
                          x=segments[i].x, y=segments[i].y,
                          anchor_x='center', anchor_y='center')
                label.text = msg
                i += 1
                label.draw()
def split_poetry():
        ListLines = poetry.readlines()
        ListWords = []
        for line in ListLines:
                words = line.split(' ')
                ListWords.append(words)

def choose_words():
        random.choice(ListWords)
def write_poetry():
    saut = 55
    for line in poetry:
        saut = saut+17*x/800
        poeme = pyglet.text.Label(line,
                            font_name='Angelface',
                            font_size=14*x/800,
                            color=(0, 0, 50, 255),
                            x=x-320*x/800, y=y-30*x/800-saut,
                            batch=batch)
        poeme.draw()

write_poetry()

@game_window.event
def on_draw():

    game_window.clear()
    wallpaper_sprite.draw()
    player_ink.draw()
    parchemin_sprite.draw()

    batch.draw()
    write_words()

def update(dt):
    for segment in segments:
        segment.update(dt)
    player_ink.update(dt)


if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()