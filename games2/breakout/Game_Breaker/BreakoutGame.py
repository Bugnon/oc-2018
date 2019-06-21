"""
version: 4.037.3.450087
"""
import pyglet
import math
import numpy as np
from pyglet.window import key
from pyglet.window import FPSDisplay
from pyglet.window import mouse 

window = pyglet.window.Window(
    width = 640, height = 480, resizable=False, caption='Initial caption')
# window.set_location(480, 220)
# print(window.width, window.height)
window.set_caption('Breakout')
icon1 = pyglet.image.load('images/icon1.png')
icon2 = pyglet.image.load('images/icon2.png')

# import blocks
blueblock = pyglet.image.load('images/Brique_Bleue.png')
greenblock = pyglet.image.load('images/Brique_Verte.png')
yellowblock = pyglet.image.load('images/Brique_Jaune.png')

blocks = [blueblock, greenblock, yellowblock]

# resize blocks
brickWidth = 40
brickHeight = 30
blueblock.width = brickWidth
blueblock.height = brickHeight
yellowblock.width = brickWidth
yellowblock.height = brickHeight
greenblock.width = brickWidth
greenblock.height = brickHeight

n, m = 7, 16
wall = np.random.randint(1, 4, size=(n, m))
print(wall)




window.set_icon(icon1, icon2)
background = pyglet.image.load('images/Background.png')
"""Initialisation de la fenêtre du jeu.
Les dimensions de la fenêtre sont 960x640.
Le titre de la fenêtre est 'Breakout'.
Les icones et l'image de font sont initialisés.
"""


class Balle():
    def __init__(self):
        self.image = pyglet.image.load('images/Balle.png')
        self.center_image()
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.sprite.x = window.width // 2
        self.sprite.y = window.height - (
            window.height * 3 // 4) + self.sprite.height // 2
        """
        Le point de départ est au milieu de l'écran et juste au dessus
        de la barre. ref-> Player.__init__
        """
        self.sprite.speed = 400.0  # pixel/sec
        self.sprite.direction = 60  # degrés

    def center_image(self):
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2

    def move_ball(self, dt):
        self.sprite.x += math.cos(
            self.sprite.direction * math.pi / 180) * self.sprite.speed * dt
        # '*math.pi/180' permet la convertion en radians.
        self.sprite.y += math.sin(
            self.sprite.direction * math.pi / 180) * self.sprite.speed * dt
        # '*math.pi/180' permet la convertion en radians.

    def bounce_side(self,
                    dt):  # Calcule l'angle de rebond sur les côtés verticaux.
        self.sprite.direction = 180 - self.sprite.direction
        self.move_ball(dt)

    def bounce_plan(
            self, dt):  # Calcule l'angle de rebond sur les côtés horizontaux.
        self.sprite.direction *= -1
        self.move_ball(dt)

    def update(self,
               dt):  # dt = 1/60 (ces opérations sont répétées 60x par seconde)
        if self.sprite.x <= self.sprite.width / 2:
            self.sprite.x = 1 + self.sprite.width / 2
            self.bounce_side(dt)
        elif self.sprite.x >= window.width - (self.sprite.width // 2):
            # Rebond sur le côté droit.
            self.sprite.x = window.width - (self.sprite.width // 2) - 1
            self.bounce_side(dt)
        elif self.sprite.y <= self.sprite.height / 2:
            self.sprite.y = 1 + self.sprite.height // 2
            self.bounce_plan(dt)
        elif self.sprite.y >= window.height - (
                self.sprite.height // 2):  # Rebond sur le plafond.
            self.sprite.y = window.height - (self.sprite.height // 2) - 1
            self.bounce_plan(dt)
        elif player.sprite.x - player.sprite.width // 2 < self.sprite.x < player.sprite.x + player.sprite.width // 2:
            if self.sprite.y - self.sprite.height // 2 < player.sprite.y + player.sprite.height // 2:
                self.bounce_plan(dt)
            else:
                self.move_ball(dt)
        else:
            self.move_ball(dt)


class Player():
    """
        Représente le joueur sous forme de barre.
        Il se déplace horizontalement entre les 2 bords de la fenêtre.
        Le joueur le contrôle avec les flèche droite et gauche du clavier,
        en modifiant sa vitesse.
        Position: x et y. Vitesse: speed.
    """

    def __init__(self):
        self.image = pyglet.image.load(
            'images/Barre.png')  # format .png pour la transparence.
        self.center_image()  # l'encre de l'image est fixée au centre.
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.sprite.x = window.width // 2
        self.sprite.y = window.height - (
            window.height * 3 // 4) - self.sprite.height // 2
        # Le point de départ est au milieu de l'écran,
        # au premier tier de la hauteur de la fenêtre.
        self.sprite.speed = 0.0

    def center_image(self):  # l'encre de l'image est fixée au centre.
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2

    def update(self, dt):
        if self.sprite.x <= 0 + self.sprite.width // 2:
            self.sprite.speed = 0  # La barre s'arrête
            self.sprite.x = 1 + self.sprite.width // 2
        elif self.sprite.x >= window.width - self.sprite.width // 2:
            self.sprite.speed = 0  # La barre s'arrête
            self.sprite.x = window.width - (1 + self.sprite.width // 2)
        else:
            self.sprite.x += self.sprite.speed * dt


"""
Création des éléments du Jeu.
Le joueur: player.
La balle: balle.
"""
space = True
player = Player()
balle = Balle()
"""
Lancement de la balle.
N'est effectué qu'une fois.
"""


@window.event
def on_key_press(symbol, modifiers):
    global space
    if space is True:
        if symbol == key.SPACE:
            pyglet.clock.schedule_interval(balle.update, 1 / 60.0)
            space = False  # Cela ne marche qu'une fois.
    elif space is False:
        pass


"""
Manipulation de la barre.
"""


@window.event
def on_text_motion(motion):
    if motion == key.RIGHT:
        if player.sprite.speed < 0:
            player.sprite.speed += 200
            # Le changement de vitesse est plus rapide lorsque
            # le joueur va dans le sens opposé à sa vitesse actuelle.
        else:
            player.sprite.speed += 50
    elif motion == key.LEFT:
        if player.sprite.speed > 0:
            player.sprite.speed -= 200
            # Le changement de vitesse est plus rapide lorsque
            # le joueur va dans le sens opposé à sa vitesse actuelle.
        else:
            player.sprite.speed -= 50


"""
Affichage des éléments du jeu.
Le fond, la balle, et le joueur.
"""


@window.event



def on_draw():
    window.clear()
    background.blit(0, 0)
    # create a random grid with the 3 type of blocks
    for i in range(n):
        for j in range(m):
            x = j * brickWidth
            y = 450 - i * brickHeight
            index = wall[i, j]
            if index > 0:
                block = blocks[index-1]
                block.blit(x, y)    
                # print(n, m, i, j, x, y, index)
    balle.sprite.draw()
    player.sprite.draw()

def on_mouse_motion(x, y, dx, dy):
    pass

# makes a block disappear when clicked on 

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('left click')
        i = (480 - y) // 30
        j = x // 40
        if wall[i, j] == 0:
          wall[i, j] = 3
        else:
          wall[i, j] = 0
        print(x, y, i, j)
    pass


pyglet.clock.schedule_interval(player.update, 1 / 60.0)
pyglet.app.run()
