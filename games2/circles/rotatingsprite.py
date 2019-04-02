import pyglet
import math
from pyglet.window import key

player_image = pyglet.resource.image("resources/encrier.png")
# définition d'une nouvelle classe
class RotatingSprite(pyglet.sprite.Sprite):
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
        super(Player, self).__init__(img=player_image, *args, **kwargs)
        
        self.rotate_speed=150

        self.keys = dict(left=False, true=False)

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
        super(Player, self).update(dt)

        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        elif self.keys['right']:
            self.rotation += self.rotate_speed * dt
