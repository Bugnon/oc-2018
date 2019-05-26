# Inkvader

* Authors: Térence Chevroulet, Victoria Vila, Hélène Ardevol
* Date: 23/05/2019

## Description

### Introduction
Dans notre Gymnase du Bugnon Ours, nous avons pu participer au Printemps de la poésie, soutenu par l'UNIL. Dans l'option complémentaire informatique, nous avons dû créer un jeu ayant un rapport avec la poésie, à présenter lors de la semaine pendant laquelle le gymnnase du Bugnon, site de l'Ours participait à ce projet du Printemps de la poésie. Plus d'informations sont disponibles sur ce site: [Printemps de la poésie UNIL](http://printempspoesie.ch/wordpress/)

Inkvader est un jeu style rétro gaming. Nous nous sommes inspirés du jeu classique [Space Invaders](https://fr.wikipedia.org/wiki/Space_Invaders) pour le créer, ainsi que des jeux à scrolling forcé. Il s'agit de se déplacer avec une plume et de tirer des tâches d'encre sur des mots flottants sur l'écran. Ces mots sont de deux sortes. D'un côté, ils ont un vocabulaire poétique. Et de l'autre, ce sont des mots choisis au hasard. Le but est de tirer sur les mots poétiques, afin qu'un poème s'écrive progressivement. 

### Le côté Poétique
Dans notre jeu, Inkvader, nous avons inséré le côté poétique des manières suivantes : 
* Le fait que notre fusée soit une plume, et qu'elle lance des tâches d'encre sur des mots, donne un côté poétique à notre jeu.
* De plus, les mots flottants sur l'écran ont un rapport avec la poésie. Il s'agit des mots donnant le côté poétique (ex: "syllabe", "rime"). 
* Un autre côté poétique est que lorsque l'on tire sur un mot poétique, un poème apparaît progressivement. 

### Structure du programme
Nous n'allons pas vous présenter le code en entier, car il est très long et complexe. Néanmoins, nous allons vous expliquer les *variables*, les *classes* et les *méthodes* principales pour pouvoir comprendre comment fonctionne le jeu. La boucle de notre jeu se trouve dans inkvader.py, les entités dans inkentities.py, les différentes fenêtres de jeu et leur configuration et fonctionnement dans inkgame.py, et finalement quelques utilitaires dans inktilities.py.

* Les Variables
-> Objets principaux : stylo, mots, tâche d'encre
* Les Class

* Les méthodes 

* La Fonction Main

### Visuel

* Pour démarrer le jeu il faut cliquer sur l'écran à l'aide de la souris.
![clicktostart](../../../games2/plume/clicktostart.JPG)
 
 * Voici à quoi ressemble le jeu lorsqu'une partie est en cours.
 ![play](/downloads/8d062285-658f-45a2-8de1-e8676fbc54e0.JPG)
 
 * En appuyant sur la touche "enter", le jeu se met en pause.
 ![pause](/downloads/8d062285-658f-45a2-8de1-e8676fbc54e0.JPG)
 
 * La plume ne peut se déplacer dans tout l'espace de l'écran, une barre apparait lorsqu'elle atteint une limite.
 ![limite](/downloads/8d062285-658f-45a2-8de1-e8676fbc54e0.JPG)
 
 * Lorsqu'un mot du vocabulaire poétique est touché, la tâche d'encre est verte en signe de victoire.
 ![victoire](/downloads/8d062285-658f-45a2-8de1-e8676fbc54e0.JPG)
  
 * Lorsqu'un mot du vocabulaire pas poétique est touché, la tache d'encre est rouge en signe d'échèque.
 ![échèque](/downloads/8d062285-658f-45a2-8de1-e8676fbc54e0.JPG)

### Intéractions souris-clavier 
Dans Inkvader, nous utilisons la souris et le clavier de ces manières:

* La souris s'utillise pour lancer le jeu.
```python
'''Starts the game on mouseclick'''
def on_mouse_press(x, y, button, modifiers):
    if inkgame.CurrentWindow.window == inkgame.MenuWindow.window :
        MainSequence.game()
```

* Les *flèches directionnelles* pour déplacer la plume. L'event est redirigé à *Inkgame.py*, puis à l'instance *GameWindow.pen* directement, qui l'utilisera dans des conditions.
```python
def update(keys):
    '''Forwards the held keys update to the pen and update all the game objects and vertices'''
    inkentities.Pen.update(GameWindow.pen, keys)
```
```python
def update(self, keys):
    if keys[key.UP] and not keys[pyglet.window.key.DOWN]:
```
* *Espace* pour tirer les tâches d'encre sur les mots, en ayant redirigé précédemment l'event keypress de *Inkvader.py* à *Inkgame.py*, puis à la fonction *keypress* de *GameWindow*, et finalement à l'instane *pen* provenant de la classe *Pen* de *Inkentities.py*. Celle-ci utilisera ensuite des conditions pour savoir quoi en faire.

```python
inkgame.CurrentWindow.keypress(pressed_key)
```
```python
def keypress(pressed_key):
    '''Forwards pressed keys to GameWindow'''
    if CurrentWindow.window == GameWindow.window :
    GameWindow.keypress(pressed_key)
```
```python
def keypress(pressed_key):
    '''Forwards pressed keys to the pen'''
    inkentities.Pen.keypress(GameWindow.pen, pressed_key)
```
```python
def keypress(self, pressed_key):
    if pressed_key == pyglet.window.key.SPACE and Pen.has_fired==0:
```

* *Enter* afin de mettre le jeu sur pause.
* *Escape* pour quitter le jeu.
```python
def on_key_press(pressed_key, modifiers):
    '''Forwards the pressed keys appropriately and pauses/resumes/quits the game.'''
    inkgame.CurrentWindow.keypress(pressed_key)
    if pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.PauseWindow.window:
        MainSequence.resume()
    elif pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.GameWindow.window:
        MainSequence.pause()
    elif pressed_key == pyglet.window.key.RETURN and inkgame.CurrentWindow.window == inkgame.WinWindow.window:
        exit()
    elif pressed_key == pyglet.window.key.ESCAPE:
        exit()
```

### Explication du jeu 

* Le but: Le but du jeu est d'écrire le poème "Le Dormeur du Val" de Rimbaud.

Premierement on doit mettre en marche le jeu, en cliquant avec la souris sur l'écrans. Ensuite nous devons nous deplacer à l'aide des quatres flèches sur le clavier, montrées ci-dessus, afin de se positionner sur l'écran de maniere à pouvoir tirer sur un mot poétique. Il faut ensuite appuyer sur la barre d'espace pour tirer une tâche d'encre sur un mot. Il faut viser les mots poétiques, car à chaque fois qu'on en touche un, le poème s'écrit mot à mot en haut de l'écran.
