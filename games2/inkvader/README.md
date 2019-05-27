# Inkvader

* Authors: Térence Chevroulet, Victoria Vila, Hélène Ardevol
* Date: 2019/05/27

## Sommaire

1. [Description](#Description)
    1. [Introduction](#Introduction)
    1. [Le Côté Poétique](#Le-Côté-Poétique)
    1. [Explication du Jeu](#Explication-du-Jeu)
    1. [Guide Visuel](#Guide-Visuel)
1. [Structure du Programme](#Structure-du-Programme)
    1. [Gestion des Fenêtres](#Gestion-des-Fenêtres)
    1. [Performance](#Performance)
    1. [OpenGL](#OpenGL)
    1. [Interactions Souris-Clavier](#Interactions-Souris-Clavier)
    1. [Collisions](#Collisions)
1. [Conclusion](#Conclusion)

## Description

### Introduction
Participant à l'option complémentaire informatique, nous avons dû créer un jeu ayant un rapport avec la poésie, à présenter lors de la semaine pendant laquelle le gymnnase du Bugnon participait à un projet du Printemps de la poésie soutenu par l'UNIL. Plus d'informations sont disponibles sur le site: [Printemps de la poésie UNIL](http://printempspoesie.ch/wordpress/)

Inkvader est un jeu style rétro gaming. Nous nous sommes inspirés du jeu classique [Space Invaders](https://fr.wikipedia.org/wiki/Space_Invaders) pour le créer, ainsi que des jeux à scrolling forcé. Il s'agit de se déplacer avec une plume et de tirer des tâches d'encre sur des mots flottants sur l'écran. Ces mots sont de deux sortes. D'un côté, ils ont un vocabulaire poétique. Et de l'autre, ce sont des mots choisis au hasard. Le but est de tirer sur les mots poétiques, afin qu'un poème s'écrive progressivement. 

### Le Côté Poétique
Dans notre jeu, Inkvader, nous avons inséré le côté poétique des manières suivantes: 
1. Le fait que notre fusée soit une plume, et qu'elle lance des tâches d'encre sur des mots, donne un côté poétique à notre jeu.
1. De plus, les mots flottants sur l'écran ont un rapport avec la poésie. Il s'agit des mots donnant le côté poétique (ex: "syllabe", "rime"). 
1. Un autre côté poétique est que lorsque l'on tire sur un mot poétique, un poème apparaît progressivement.


### Explication du Jeu 

* Le but: Le but du jeu est de faire apparaître les vers du poème *"Le Dormeur du Val"* de Rimbaud.

Premièrement, le joueur ,et en marche le jeu, en cliquant avec la souris sur l'écran d'accueil. Ensuite, il a la possibilité de se déplacer dans une zone limitée avec les *Flèches* et de lancer horizontalement des projectiles avec la touche *Espace*.

Si les projectiles touchent un mot faisant partie du vocabulaire technique poétique, un mot du poème sera dévoilé. Les erreurs ne sont pas comptabilisées, mais provoquent un bruit désagréable.

Lorsque le poème est complété, le jeu affiche un écran de victoire.

### Guide Visuel

* Pour démarrer le jeu il faut cliquer sur l'écran à l'aide de la souris.

![clicktostart](https://github.com/Bugnon/oc-2018/blob/master/games2/inkvader/screenshots/Screen%20Start.png?raw=true) 
 
 * Voici à quoi ressemble le jeu lorsqu'une partie est en cours.

 ![play](https://github.com/Bugnon/oc-2018/blob/master/games2/inkvader/screenshots/Screen%20Game.png?raw=true)
 
 * En appuyant sur la touche *Enter*, le jeu se met en pause.

 ![pause](https://github.com/Bugnon/oc-2018/blob/master/games2/inkvader/screenshots/Screen%20Pause.png?raw=true)
 
 * La plume ne peut se déplacer dans tout l'espace de l'écran, une barre apparait lorsqu'elle atteint une limite.

 ![limite](https://github.com/Bugnon/oc-2018/blob/master/games2/inkvader/screenshots/Screen%20Limit.png?raw=true)
 
 * Lorsqu'un mot du vocabulaire poétique est touché, la tâche d'encre est verte en signe de victoire.

 ![victoire](https://github.com/Bugnon/oc-2018/blob/master/games2/inkvader/screenshots/Screen%20Green.png?raw=true)
  
 * Lorsqu'un mot du vocabulaire pas poétique est touché, la tache d'encre est rouge en signe d'échec.

 ![échec](https://github.com/Bugnon/oc-2018/blob/master/games2/inkvader/screenshots/Screen%20Red.png?raw=true)

 * Lorsque l'entièreté du poème a été affichée, la partie est gagnée!

 ![win](https://github.com/Bugnon/oc-2018/blob/master/games2/inkvader/screenshots/Screen%20Won.png?raw=true)


## Structure du Programme
Nous n'allons pas vous présenter le code en entier, car il est très long et complexe. Néanmoins, nous allons vous expliquer les concepts principaux pour comprendre le fonctionnement de notre code. La boucle de notre jeu se trouve dans `inkvader.py`, les entités dans `inkentities.py`, les différentes fenêtres de jeu, leur configuration et fonctionnement dans `inkgame.py`, et finalement quelques utilitaires dans `inktilities.py`.

#### Gestion des Fenêtres

À chaque fois que `update(dt)` est appelée, `pyglet` rafraichit la fenêtre et son contenu. Or, ce contenu dépend d'une variable `window` et du contenu du `batch`, qui sont dépendants de la variable `CurrentWindow.window` de `inkgame.py`. Ainsi, en changeant cette variable, il est possible de passer d'un batch à un autre et d'une fenêtre à une autre sans pour autant perdre leur contenu! De plus, elle permet de rediriger l'appel des fonctions de mise à jour aux bons endroits.

Par exemple, lorsque l'on pause le jeu, il suffit de faire 
```python
def pause():
    inkgame.CurrentWindow.window = inkgame.PauseWindow.window
    inkgame.CurrentWindow.batch = inkgame.PauseWindow.batch
```
Puis pour reprendre,
```python
def resume():
    inkgame.CurrentWindow.window = inkgame.GameWindow.window
    inkgame.CurrentWindow.batch = inkgame.GameWindow.batch
```
Ce qui simplifie radicalement la tâche, tout en la rendant efficace et plus propre.

#### Performance

Le rafraîchissement étant de 60Hz, certaines opérations peuvent rapidement devenir très lourdes. Ainsi, il y a dans `inkvader.py` une fonction 
```python
pyglet.clock.schedule_interval(inkgame.CurrentWindow.slow_update, 1/10)
```
Celle-ci fait en sorte que, par exemple, la vérification des collisions ne se fasse qu'à 10Hz. 

#### OpenGL

Il fallait dessiner des lignes avec OpenGL pour représenter différents éléments d'interface. La fonction la plus simple à utiliser, `.draw()`, est terriblement inefficace pour un programme à 60Hz. Cependant, il est possible de mettre à jour les `vertices` de lignes déjà existantes à 60Hz dans le batch où se trouvent les autres `sprites`, ce qui permet de n'avoir à initialiser les lignes qu'une fois.

Initialisation des lignes et ajout au batch:
```python
GameWindow.vertex_chargebar = inktilities.init_chargebar()
pyglet.graphics.Batch.migrate(GameWindow.vertex_chargebar, GameWindow.vertex_chargebar, pyglet.gl.GL_LINES, None, GameWindow.batch)
```
```python
def init_chargebar():
    '''Initializes the charge bar vertices'''
    return pyglet.graphics.vertex_list(
                2, #draws a line for the fire effect
                ("v2f", (1, 0, 0, 1))
            )
```
Il suffit ensuite de mettre à jour les `vertices` à chaque `update`
```python
GameWindow.vertex_chargebar.vertices[:] = inktilities.update_chargebar(GameWindow.pen, inkentities.Pen)
```
```python
def update_chargebar(pen, Pen):
    '''Returns a vertex_list of the charge bar on top of the pen'''
    pen_start = pen.x - pen.width / 2
    return [pen_start, pen.y + pen.height / 2, pen_start + (pen.width * (Pen.has_fired / 60)), pen.y + pen.height / 2]
```

#### Interactions Souris-Clavier 
Dans Inkvader, nous utilisons la souris et le clavier de ces manières:

* La souris s'utillise pour lancer le jeu.
```python
'''Starts the game on mouseclick'''
def on_mouse_press(x, y, button, modifiers):
    if inkgame.CurrentWindow.window == inkgame.MenuWindow.window:
        MainSequence.game()
```

* Les *flèches directionnelles* pour déplacer la plume. L'event est redirigé à `Inkgame.py`, puis à l'instance `GameWindow.pen` directement, qui l'utilisera dans des conditions.
```python
def update(keys):
    '''Forwards the held keys update to the pen and update all the game objects and vertices'''
    inkentities.Pen.update(GameWindow.pen, keys)
```
```python
def update(self, keys):
    if keys[key.UP] and not keys[pyglet.window.key.DOWN]:
```
* *Espace* pour tirer les tâches d'encre sur les mots, en ayant redirigé précédemment l'event keypress de `Inkvader.py` à `Inkgame.py`, puis à la fonction `keypress` de `GameWindow`, et finalement à l'instance `pen` provenant de la classe `Pen` de `Inkentities.py`. Celle-ci utilisera ensuite des conditions pour savoir quoi en faire.

```python
inkgame.CurrentWindow.keypress(pressed_key)
```
```python
def keypress(pressed_key):
    '''Forwards pressed keys to GameWindow'''
    if CurrentWindow.window == GameWindow.window:
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

#### Collisions 

Afin de gérer les collisions entre projectiles et projectiles, splatters et mots, nous avons deux fonctions respectives: `word_collision()` et `ìnk_collision`.

Ces deux fonctions fonctionnement sur le même concept: les instances `inkentities.Ink`, `inkentities.Splatter` et `inkentities.FloatingLabel` lorsqu'elles sont instancées sont ajoutées à une liste respective `ink_list` et `word_list`. Ainsi, facilement retrouvables, il est possible d'itérer entre chacune d'entre elles et de vérifier que l'une des des instances ne se retrouve pas dans l'aire d'une autre. Voici un extrait d'une des deux fonctions:

```python
for i in range(len(GameWindow.ink_list)):
    for j in range(len(GameWindow.word_list)):
        obj_1 = GameWindow.ink_list[i]
        obj_2 = GameWindow.word_list[j]

        if not obj_1.dead and not obj_2.dead:
            if (obj_2.x <= obj_1.x <= obj_2.x + obj_2.content_width) and (obj_2.y - obj_2.content_height / 2 <= obj_1.y <= obj_2.y + obj_2.content_height):
```

La condition ci-dessus est longue, mais permet de ne pas avoir à utiliser de constantes: la *hitbox* des instances sera toujours proportionnelle à leur taile! De plus, en vérifiant séparément pour différentes listes, cela permet de ne pas avoir à comparer entre tous les objets présents dans la fenêtre, ce qui causait des erreurs graves (segfault.)

## Conclusion

Pour finir, ce programme nous a permis d'approfondir nos connaissances pour ce qui est de la gestion des *fenêtres* `window`, des `batch`, d'*OpenGL*, et nous a même donné l'occasion de discuter d'un problème de performance avec l'un des membres de l'équipe de développement de *Pyglet*, qui nous a renseigné sur le fonctionnement de ces différentes méthodes graphiques.

Ce travail d'optimisation était enrichissant, et permettait de découvrir une certaine satisfaction à voir des paragraphes de code devenir de simples lignes, tout en voyant notre programme devenir plus réactif.

La question de l'esthétique du jeu était également cruciale, Inkvader étant dans la sobriété absolue: noir, blanc, quelques gouttes de vert et rouge. Communiquer des informations, comme les limites d'une zone, le bien-fondé d'une action, un temps de recharge à travers cette optique minimaliste était délicat, mais s'est trouvé être un défi amusant et créatif.

La recherche de contenu sonore et sa conversion dans un format adapté était délicate aussi, mais nous avons pu obtenir des sons qui étaient adaptés et relativement plaisants à entendre. Quant à la musique, elle est libre de droits et par Kevin Macleod.

Manquant de temps à cause de l'abondance de tests en cette fin de troisième année, nous n'avons malheureusement pas pu polir notre code autant que prévu. Certaines fonctions n'ont pas de commentaires, et d'autres pourraient certainement être optimisées. L'un des objectifs, si l'occasion se présente, serait de permettre au eu de recommencer à partir de l'écran de victoire, et d'y afficher le score. 