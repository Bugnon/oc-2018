import pyglet, random, math, time
from pyglet.window import key

fire = pyglet.media.load('resources/sound/fire.wav', streaming=False)
fire_sound = pyglet.media.Player()
fire_sound.volume = 0.01

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)


class Player(pyglet.sprite.Sprite):
    """Classe définissant le joueur qui sera contrôlé avec les flèches gauche et droite."""
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

        self.image = pyglet.resource.image('resources/sprites/player.png')
        
        self.rotate_speed = 200

        self.keys = {'left':False, 'right':False, 'space':False}

        self.timer = 0

        self.angle = 0

        #Create the projectile (feathers)
        self.feathers = []
        self.feather = pyglet.resource.image('resources/sprites/feather.png')
        center_image(self.feather)

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
        feather = Feather(player=self, img=self.feather, x=self.x, y=self.y)
        feather.x = self.x + self.width * math.sin(math.radians(self.angle))
        feather.y = self.y + self.height * math.cos(math.radians(self.angle))

        feather.rotation = self.angle
        feather.scale = 0.03

        self.feathers.append(feather)
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
        
        for feather in self.feathers:
            
            Feather.update_position(feather, dt)


            platform = pyglet.window.get_platform()
            display = platform.get_default_display()      
            screen = display.get_default_screen()

            if feather.dead == True:
                self.feathers.remove(feather)
            
            if feather.x <= 0 or feather.x >= screen.width:
                self.feathers.remove(feather)
            elif feather.y <= 0 or feather.y >= screen.height:
                self.feathers.remove(feather)

class Feather(pyglet.sprite.Sprite):
    """Classe définissant les projectiles que le joueur lancera avec la barre espace."""
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

class RotatingSprite(pyglet.sprite.Sprite):
    """Classe définissant les segments de cercle qui tournent."""

    segments = []
    words = ['arbre','fromage','language','beau','ramage','hôte','voix','bec','flatteur','dépens','leçon','honteux','confus','jura','tard']

    def __init__(self, angle_radians, x, r, xc, yc, word, *args, **kwargs):
        super(RotatingSprite, self).__init__(*args, **kwargs)

        self.word = word

        self.angular_velocity = math.pi/5
        self.angle = angle_radians
        self.xc = xc
        self.yc = yc
        self.r = r
        self.dr = 100
        #self.growing = False

        self.label = pyglet.text.Label(self.word.upper(),
                font_name='Times New Roman',
                font_size=self.r/30,
                color=(75, 0, 130, 255),
                x=0, y=0,
                anchor_x='center', anchor_y='center')

        self.scale = 0.56*x/1200

        self.dead = False

        self.update_position()

    def update_position(self):
        self.x = self.xc + self.r * math.sin(self.angle)
        self.y = self.yc + self.r * math.cos(self.angle)
        self.rotation = math.degrees(self.angle)

        self.label.x = self.x
        self.label.y = self.y

    def update(self, dt):
        self.angle += self.angular_velocity * dt
        self.scale = self.r/540

        if self.dead == True:
                RotatingSprite.segments.remove(self)
                RotatingSprite.words.remove(self.word)

        #if self.r >= 450:
        #    self.growing = False
        #elif self.r <= 200:
        #    self.growing = True

        #if self.growing:
        #    self.r += self.dr * dt
        #else:
        #    self.r -= self.dr * dt

        self.update_position()