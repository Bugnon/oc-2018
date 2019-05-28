"""
version: 4.037.3.450087
"""
import pyglet
import time
import math
from pyglet.window import key
from pyglet.window import FPSDisplay

window = pyglet.window.Window(width=960, height=640,
resizable=False, caption='Initial caption')
window.set_location(480, 220)
window.set_caption('Breakout')
icon1 = pyglet.image.load('images/icon1.png')
icon2 = pyglet.image.load('images/icon2.png')
window.set_icon(icon1, icon2)
background = pyglet.image.load('images/Background.png')
"""Initialisation de la fenêtre du jeu.
Les dimensions de la fenêtre sont 960x640.
Le titre de la fenêtre est 'Breakout'.
Les icones et l'image de font sont initialisés.
"""

class Balle():
        """
        Représente la balle du jeu.
        Elle se déplace à vitesse constante et
        rebondit sur les murs, le plafond et le joueur.
        Position: x et y. Vitesse: speed[pixel/sec].
        Direction: direction[degré].
        """

        def __init__(self):
                self.image = pyglet.image.load('images/Balle.png') # format png. pour la transparence.
                self.center_image() # l'encre de l'image est fixée au centre.
                self.sprite = pyglet.sprite.Sprite(self.image) # 50x50
                self.sprite.x = window.width//2 
                self.sprite.y = window.height-(window.height*3//4)+self.sprite.height//2
                # Le point de départ est au milieu de l'écran et juste au dessus de la barre. ref-> Player.__init__ 
                self.sprite.speed = 400.0 # pixel/sec
                self.sprite.direction = 60 # degrés

        def center_image(self): # l'encre de l'image est fixée au centre.
                self.image.anchor_x = self.image.width // 2
                self.image.anchor_y = self.image.height // 2
   
        def move_ball(self, dt): # Déplace la balle selon sa vitesse speed et sa direction.
                self.sprite.x += math.cos(self.sprite.direction*math.pi/180)*self.sprite.speed * dt # '*math.pi/180' permet la convertion en radians.
                self.sprite.y += math.sin(self.sprite.direction*math.pi/180)*self.sprite.speed * dt # '*math.pi/180' permet la convertion en radians.
    
        def bounce_side(self, dt): # Calcule l'angle de rebond sur les côtés verticaux.
                self.sprite.direction = 180-self.sprite.direction
                self.move_ball(dt)

        def bounce_plan(self, dt): # Calcule l'angle de rebond sur les côtés horizontaux.
                self.sprite.direction *= -1
                self.move_ball(dt)

        def update(self, dt): # dt = 1/60 (ces opérations sont répétées 60x par seconde)
                if self.sprite.x <= self.sprite.width/2: # Rebond sur le côté gauche.
                        self.sprite.x = 1+self.sprite.width/2
                        self.bounce_side(dt)
                elif self.sprite.x >= window.width-(self.sprite.width//2): #Rebond sur le côté droit.
                        self.sprite.x = window.width-(self.sprite.width//2)-1
                        self.bounce_side(dt)
                elif self.sprite.y <= self.sprite.height/2: # Rebond sur le sol. (À retirer après les phases de test)
                        self.sprite.y = 1+self.sprite.height//2
                        self.bounce_plan(dt)
                elif self.sprite.y >= window.height-(self.sprite.height//2): # Rebond sur le plafond.
                        self.sprite.y = window.height-(self.sprite.height//2)-1
                        self.bounce_plan(dt)
                elif player.sprite.x-player.sprite.width//2 < self.sprite.x < player.sprite.x+player.sprite.width//2: # Rebond sur le joueur.
                        if self.sprite.y-self.sprite.height//2 < player.sprite.y+player.sprite.height//2:
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
                self.image = pyglet.image.load('images/Barre.png') # format .png pour la transparence.      
                self.center_image() # l'encre de l'image est fixée au centre.
                self.sprite = pyglet.sprite.Sprite(self.image) #250x50
                self.sprite.x = window.width//2
                self.sprite.y = window.height-(window.height*3//4)-self.sprite.height//2
                # Le point de départ est au milieu de l'écran,
                # au premier tier de la hauteur de la fenêtre.
                self.sprite.speed = 0.0 #pixel/sec
    
        def center_image(self): # l'encre de l'image est fixée au centre.
                self.image.anchor_x = self.image.width // 2
                self.image.anchor_y = self.image.height // 2

        def update(self, dt):
                if self.sprite.x <= 0 + self.sprite.width//2: #Lorsque le joueur atteind le côté gauche
                        self.sprite.speed = 0 # La barre s'arrête
                        self.sprite.x = 1 + self.sprite.width//2
                elif self.sprite.x >= window.width - self.sprite.width//2: #Lorsque le joueur atteind le côté gauche
                        self.sprite.speed = 0 # La barre s'arrête
                        self.sprite.x = window.width - (1 + self.sprite.width//2)
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
        if space == True:
                if symbol == key.SPACE: # Permet de lancer la balle en appuyant sur la barre espace
                        pyglet.clock.schedule_interval(balle.update, 1/60.0)
                        space = False # Cela ne marche qu'une fois.
        elif space == False:
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
        balle.sprite.draw()
        player.sprite.draw()

pyglet.clock.schedule_interval(player.update, 1/60.0)
pyglet.app.run()