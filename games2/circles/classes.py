import pyglet
import math
from pyglet.window import key

feather_image = pyglet.resource.image("resources/plume.png")

player_image = pyglet.resource.image("resources/encrier.png")

# définition d'une nouvelle classe
class RotatingSprite(pyglet.sprite.Sprite):
    """Classe définissant les sprites qui tournent."""
    def __init__(self, *args, **kwargs):
        super(RotatingSprite, self).__init__(*args, **kwargs)

        self.angular_velocity = math.pi/10
        self.angle = 0
        self.xc = 100
        self.yc = 100
        self.r = 100
        self.update_position()

    def update_position(self):
        self.x = self.xc + self.r * math.sin(self.angle)
        self.y = self.yc + self.r * math.cos(self.angle)
        self.rotation = math.degrees(self.angle)

    def update(self, dt):
        self.angle += self.angular_velocity * dt
        self.update_position()

class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        
        self.rotate_speed=200

        self.keys = {'left':False, 'right':False}

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.SPACE:
            self.fire()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False

    def fire(self):
        feather_x = self.x + player_image.width / 2
        feather_y = self.y
        feather = Feather(x=feather_x, y=feather_y)
        self.new_objects.append(feather)

    def update(self, dt):
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        elif self.keys['right']:
            self.rotation += self.rotate_speed * dt

class Feather(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(Feather, self).__init__(*args, **kwargs)
        # Ink speed is proportional to the window's width and itselfs, and is affected by the pen's current speed
        self.speed = 100

        self.speed_x = self.speed
        self.speed_y = self.speed

        self.new_objects = []

        self.keys = {'space':False}


    def update(self, dt):
        self.x += self.speed_x * dt
        self.y += self.speed_x * dt

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.keys['space'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.keys['space'] = False
    
    def update(self, dt):
        if self.keys['space']:
            self.draw()
            self.x += self.speed_x * dt
            self.y += self.speed_y * dt
