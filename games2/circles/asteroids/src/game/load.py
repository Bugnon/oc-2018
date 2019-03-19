import pyglet
import random
import resources
import asteroid
from util import distance


def player_lives(num_icons, batch=None):
    """
    Create num_icons player lives sprites. These are displayed in the top right of the screen, and indicate how many
    lives the player has.
    :param num_icons: The number of player_lives icons to display
    :param batch: The drawing batch to include the player_lives in
    :return: A list of player_lives sprites
    """
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=785-i*30, y=585, batch=batch)
        new_sprite.scale = 0.5
        new_sprite.rotation = 270
        player_lives.append(new_sprite)

    return player_lives


def asteroids(num_asteroids, player_position, batch=None):
    """
    Creates num_asteroids asteroid PhysicalObjects at random positions and rotations, checking to ensure they are far enough
    away from the players location.
    :param num_asteroids: The number of asteroids to draw to the screen
    :param player_position: The players current position
    :param batch: The batch to include the asteroids in
    :return: A list of asteroids sprites
    """
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        # Try and place a new asteroid. If it is too close to the player, start again
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)

        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
        asteroids.append(new_asteroid)
    return asteroids