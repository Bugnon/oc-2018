# Circles

* Authors: Massimo Stefani, Valentin Piquerez et Hugo Ducommun
* Date: 23/05/2019

## Description

### Introduction



### Explication du jeu
Le but du jeu est de compléter les lacunes d'un poèmes. Pour celà, le joueur est muni d'un encrier qui tire des plumes. Cet encrier est au centre d'un cercle constitué de 15 mots qui tourne. Il faut tirer sur le mot qui manque dans le vers affiché pour passer au vers suivant jusqu'à ce que le poème soit complété.
#### Touches
* Barre espace : tirer les projectiles
* Flèches gauche-droite : faire tourner l'encrier
### Structure du programme
Notre jeu est composé de deux fichiers: le __classes.py__ et le __Circles.py__.
#### classes.py
Dans ce fichiers, nous définissins toutes les classes utiles à la création du jeu.
* Dans un premier temps, nous importons pyglet ainsi que quelques autres modules utiles
```python
import pyglet, random, math, time
from pyglet.window import key, FPSDisplay
```
Ensuite, nous définissons deux fonctions qui nous serons utiles par la suite.
* center_image

Cette fonction permet de définir la position d'images en fonction de leur centre.
  ```python
  def center_image(image):
    image.anchor_x = image.width // 2 # The center is placed at half of width
    image.anchor_y = image.height // 2 # The center is placed at half of height
  ```
* distance

Cette fonction permet de calculer la distance entre deux points.
```python
def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)
```

Par la suite, nous commencons à définir les `class` utiles pour le jeu.
* Window

Cette classe définit une fenêtre de jeu en __pleine écran__ à __60 FPS__, et les FPS sont affichés.
```python
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.set_fullscreen(True)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)
```
* Player

Cette classe définit le joueur, c'est-à-dire l'encrier, qui est commandé avec les touches _left_, _right_ et _space_.
Dans un premier temps, nous donnons plusieurs variables à notre joueur en définissant `__init__`.
```python
class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

        self.image = pyglet.resource.image('resources/sprites/player.png')
        self.rotate_speed = 200
        self.keys = {'left':False, 'right':False, 'space':False} #keys used to control the player
        self.timer = 0 #the timer is an attribute to helps the feather to know the angular position of the player
        self.angle = 0 #angle of the player at the beginning
        self.scale = 0.56*screen.width/1200 # size of the player
        self.reloading = 0
```
Ensuite, nous définissons `on_key_release`et `on_key_press` afin de savoir quans les touches du clavier sont utilisées pour contrôler le joueur.
```python
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
 ```
 Nous définissons ensuite une fonction `fire` qui sert au moment ou le joueur tire une plume, c'est-à-dire notre projectile. Nous lui donnons comme variables la rotation, qui est égale à la même que celle du joueur, ainsi que la position du projectile en fonction de l'angle de tir. Nous ajoutons aussi un bruit lorsqu'une plume est tirée.
 ```python
     def fire(self):
        self.angle = self.timer * self.rotate_speed

        feather = Feather(player=self, img=Feather.feather, x=self.x, y=self.y)
        feather.x = self.x + self.width * math.sin(math.radians(self.angle))
        feather.y = self.y + self.height * math.cos(math.radians(self.angle))
        feather.rotation = self.angle
        Feather.feathers.append(feather)
        
        fire_sound.queue(fire)
        fire_sound.play()

        self.reloading = 30 # = 0,5 sec car il descend de 1 chaque 1/60 sec
```
