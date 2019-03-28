import pyglet
import math

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