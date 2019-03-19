import random
import pyglet
import physicalobject
import resources


class Asteroid(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(resources.asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random() * 100.0 - 50.0
        self.reacts_to_bullet = True

    def update(self, dt):
        super(Asteroid, self).update(dt)
        self.rotation += self.rotate_speed * dt

    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        if self.dead and self.scale > 0.25:
            num_asteroids = random.randint(2, 30)
            for i in xrange(num_asteroids):
                new_asteroid = Asteroid( x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.velocity_x = ( random.random() * 70 + self.velocity_x)
                new_asteroid.velocity_y = ( random.random() * 70 + self.velocity_y)
                new_asteroid.scale = self.scale * 0.5
                self.new_objects.append(new_asteroid)