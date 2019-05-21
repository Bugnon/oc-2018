##### IMPORT #####
import pyglet, random, math, time
from pyglet.window import key, FPSDisplay

##### MEDIA #####
fire = pyglet.media.load('resources/sound/fire.wav', streaming=False)
fire_sound = pyglet.media.Player()
fire_sound.volume = 0.001

##### SCREEN INFORMATION #####
platform = pyglet.window.get_platform()
display = platform.get_default_display()      
screen = display.get_default_screen()

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

##### GAME WINDOW CLASS #####
# Create a class for the game_window
class Window(pyglet.window.Window):
    """Classe définissant une fenêtre de jeu en pleine écran à 60 FPS."""
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.set_fullscreen(True)
        self.frame_rate = 1/60.0 
        self.fps_display = FPSDisplay(self)

##### PLAYER CLASS #####
class Player(pyglet.sprite.Sprite):
    """Classe définissant le joueur qui sera contrôlé avec les flèches gauche et droite."""
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

        self.image = pyglet.resource.image('resources/sprites/player.png')
        
        self.rotate_speed = 200

        self.keys = {'left':False, 'right':False, 'space':False}

        self.timer = 0

        self.angle = 0

        self.reloading = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.SPACE:
            self.keys['space'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.SPACE:
            self.keys['space'] = False

    def fire(self):
        self.angle = self.timer * self.rotate_speed
        feather = Feather(player=self, img=Feather.feather, x=self.x, y=self.y)
        feather.x = self.x + self.width * math.sin(math.radians(self.angle))
        feather.y = self.y + self.height * math.cos(math.radians(self.angle))

        feather.rotation = self.angle
        feather.scale = 0.03

        Feather.feathers.append(feather)
        fire_sound.queue(fire)
        fire_sound.play()
        self.reloading = 35 # 0,58 sec car il descend de 1 chaque 1/60 sec

    def update(self, dt):
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
            self.timer -= 1 * dt
        elif self.keys['right']:
            self.rotation += self.rotate_speed * dt
            self.timer += 1 * dt
        
        if self.keys['space'] and self.reloading == 0:
            self.fire()
        
        if self.reloading > 0:
            self.reloading -= 1
        
        for feather in Feather.feathers:
            
            Feather.update_position(feather, dt)

            if feather.dead == True:
                Feather.feathers.remove(feather)
            
            if feather.x <= 0 or feather.x >= screen.width:
                Feather.feathers.remove(feather)
            elif feather.y <= 0 or feather.y >= screen.height:
                Feather.feathers.remove(feather)

##### PROJECTILE CLASS #####
class Feather(pyglet.sprite.Sprite):
    """Classe définissant les projectiles que le joueur lancera avec la barre espace."""

    #Create the projectile (feathers)
    feather = pyglet.resource.image('resources/sprites/feather.png')
    center_image(feather)

    feathers = []

    def __init__(self, player, *args, **kwargs):
        super(Feather, self).__init__(*args, **kwargs)

        self.image = pyglet.resource.image('resources/sprites/feather.png')

        self.speed = 600 # Norm of the velocity

        self.angle = player.angle

        self.dx = math.sin(math.radians(player.angle)) * self.speed
        self.dy = math.cos(math.radians(player.angle)) * self.speed

        self.dead = False

    def update_position(self, dt):

        self.x += self.dx * dt
        self.y += self.dy * dt

class Poetry():
    """Classe permettant de lire, couper, choisir et utiliser les vers et les mots."""
    towards = []
    words = []
    poetry = open("resources/documents/poeme.txt", encoding='utf8')
    towards_unsplited = poetry.read().split('\n')
    def __init__(self):
        self.poetry = Poetry.towards_unsplited
        self.towards = Poetry.towards
        self.words = Poetry.words

    def split_poetry(self):
            for line in self.poetry:
                    words_splited = line.split(' ')
                    self.towards.append(words_splited)
            return self.towards

    def choose_words(self):
            self.towards = Poetry().split_poetry()
            i = 0
            for __ in self.towards:
                    random_choice = random.choice(self.towards[i])
                    i += 1
                    self.words.append(random_choice)
            return self.words

    def save_words(self):
        with open('words.txt', 'w', encoding='utf8') as filehandle:
            for listitem in Poetry().choose_words():
                filehandle.write('%s\n' % listitem)
    
    def open_words(self):
        return open("words.txt", encoding='utf8').read().split('\n')

Poetry().save_words()

##### ROTATINGSPRITE CLASS #####
class RotatingSprite(pyglet.sprite.Sprite):
    """A class which defines the circle's segments and the turning words."""

    #Set the class attributes
    segments = []
    words = Poetry().open_words()
    angular_velocity = math.pi/5
    circle_segment_grey = pyglet.resource.image('resources/sprites/circle_segment_grey.png') #Dead segment

    def __init__(self, angle_radians, r, xc, yc, word, *args, **kwargs):
        super(RotatingSprite, self).__init__(*args, **kwargs)
        #Set the instance attributes
        self.word = word #the word  assigns to self

        self.angle = angle_radians
        self.xc = xc
        self.yc = yc
        self.r = r
        #self.dr = 100
        #self.growing = False


        self.scale = 0.56*screen.width/1200

        self.dead = False

        self.update_position()

    def update_position(self):
        #Set the self label onto the self segment
        self.label = pyglet.text.Label(self.word.upper(),
                font_name='Times New Roman',
                font_size=self.r/30,
                color=(75, 0, 130, 255),
                x=self.x, y=self.y,
                anchor_x='center', anchor_y='center')

        self.x = self.xc + self.r * math.sin(self.angle)
        self.y = self.yc + self.r * math.cos(self.angle)
        self.rotation = math.degrees(self.angle)

    def update(self, dt):
        self.angle += RotatingSprite.angular_velocity * dt
        self.scale = self.r/540

        if self.dead == True:
                self.img = RotatingSprite.circle_segment_grey #replace the image by a dead segment image
                RotatingSprite.words.remove(self.word) #destroy the word assigns to the dead segment

        #if self.r >= 450:
        #    self.growing = False
        #elif self.r <= 200:
        #    self.growing = True

        #if self.growing:
        #    self.r += self.dr * dt
        #else:
        #    self.r -= self.dr * dt

        self.update_position()

