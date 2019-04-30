import pyglet
import math
from pyglet.window import key
import game_Hugo

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
        
        self.rotate_speed=150

        self.keys = {'left':False, 'right':False}

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
    
    def update(self, dt):
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        elif self.keys['right']:
            self.rotation += self.rotate_speed * dt

class Ink(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Ink, self).__init__(*args, **kwargs)

        self.speed_x = self.speed * math.sin(self.rotation)
        self.speed_y = self.speed * math.cos(self.rotation)

        self.keys = {'space':False}

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.keys['space'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.keys['space'] = False
    
    def update(self, dt):
        if self.keys['space']:
            ink.draw()
            self.x += self.speed_x * dt
            self.y += self.speed_y * dt