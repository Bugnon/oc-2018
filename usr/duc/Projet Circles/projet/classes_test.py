import pyglet, random, math
from pyglet.window import key


class Player(pyglet.sprite.Sprite):
    """Add an object in our game as a rotating sprite."""

    def __init__(self, *arg, **kwargs):
        super().__init__(img='resources/sprites/player.png', *arg, **kwargs)
        self.x = x
        self.y = y

        self.rotate_speed = 200

        self.keys = {'left':False, 'right':False, 'space':False}

    def draw(self):
        self.sprite.draw()

    def fire(self):
        pass

    def update(self, dt):
        pass
