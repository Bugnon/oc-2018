# Wordament

* Auteurs: Fabian Roulin, Michael Greub et Mirko Pirona
* Date: Le 25 mai 2019
1. [Introduction](#introduction)
2. [Côté poétique](#côté-poétique)
3. [But du jeu](#but-du-jeu)
4. [Explication du jeu](#explication-du-jeu)
    * [Possibiltés de personnalisation](#Possibiltés-de-personnalisation)
5. [Structure du programme](#Stucture-du-programme)
    * [random_level_generation](#random_level_generation) [check_existence](#check_existence)
    * [create_image_store](#create_image_store)
    * [new_level](#new_level)
6. [Conclusion](#conclusion)

********

## Introduction

Des lettres et des mots, tel est le concept. Le but du jeu est similaire à celui du scrabble, c'est à dire, de créer des mots avec des lettres prédéfini. Il existe de nombreuse variantes de ce jeu, mais nous avons décidé de prendre la plus pure, et la plus facile à expliquer et prendre en main.

## Côté poétique

Le côté poétique est apporté par le nombre de personnalisation possible du programme. En effet, pour le moment la liste des mots admis est une liste extraite du dictionnaire Gutenberg ([Source de la liste](http://www.pallier.org/liste-de-mots-francais.html)).  Cependant il est aussi possible de créer une liste avec les noms de tous les poètes, ou une liste des mots à connotation poétique.
Pour ce faire, en marge de notre jeu, nous avons aussi créé un petit script permettant de transformer un fichier texte en liste compatible avec notre jeu.
Pour finir, notre jeu présente un interface simple est lisible, pour permettre la meilleur expérience possible. 

## But du jeux

Le jeux est constitué de deux modes. Le premier se nommant "Selected level" est un mode dans lequel il faut atteindre un score de 100 avec une grille de lettre 4 x 4 prédéfinie sachant que la valeur des lettres est écrite en dessous de ces dernières. Une fois le niveau terminé le suivant démarre jusqu'au niveau 10. Le deuxième mode s'appelant "Random Level" est un mode dans lequel le but est de faire le plus grand score possible dans une grille générée aléatoirement tout en gardant la base du mode "Selected levels".

## Explication du jeu :

Lorsque le jeu est lancé, il vous envoie directement dans le menu ou hub du jeu. Là, vous devez choisir le mode de jeu auquel vous désirer jouer. Il y a le mode _selected level_, qui vous donne des niveaux déjà programmés ou le _mode random level_ qui génère des niveaux aléatoires. 

Dans ces deux modes de jeu, le but est identique. C’est de créer des mots sur la grille. Vous pouvez vous déplacer d’une case sur une des 8 cases adjacentes, soit en haut, à gauche, en bas, à droite ou encore dans les 4 diagonales. 

Pour faire un mot, vous placer le curseur de la souris  sur la première lettres de votre mot et vous appuyer sur le bouton gauche de la souris tout en maintenant le bouton enfoncé. Vous pourrez alors déplacer le curseur afin de compléter votre mot. Quand votre mot serra finit, il vous suffira de relâcher le bouton gauche de la souris pour valider le mot. Lorsque vous créez un mot, les cases utilisées deviennent de couleur jaunes. 

Une fois terminé, si le mot existe, il deviendra vert, dans le cas contraire il deviendra rouge. De plus, si le mot a déjà été fait, il apparaîtra également en rouge. 

Un nombre de point vous sera attribué à chaque mot correct en fonction des lettres utilisées et de la longueur du mot. Le jeu passera au niveau suivants lorsque vous aurez atteint les 200 points. 

Dans le mode random level, en haut à droite se trouve un bouton « next » qui vous permettra de changer de niveau si vous ne parvenez pas aux 200 points nécessaires.

### Possibiltés de personnalisation

Ce jeu à été construit pour offrir un certain nombre d'ajouts personnels. 
Les fonds d'écrans et les musiques peuvent être changés dans le dossier image. Les points par lettre et le nombre de lettre (par exemple si vous changez de langue) peuvent être modifiés dans le fichier levels du dossier du même nom. Les bonus de longueur peuvent également être changé dans ce fichier.

## Stucture du programme

Notre programme est codé en python, avec une forte sollicitation du module ```Pyglet```. La fonction principale de ce module est de permettre les interactions directes avec l'utilisateurs, de gérer l'affichage des images et les quelques effets sonnores et musicaux utilisés. 

Notre code a été codé de façon linéaire, sans utilisé la programmation orienté objet (OOP).

Notre code commence donc par l'importation des quatre modules utilisés par la suite, soit:
* Pyglet
* Codecs
* La fonction Path de Pathlib
* Random

par le code suivant:
```python
import pyglet
from levels import levels
import codecs
from pathlib import Path
from random import randint
```
La deuxième ligne quant à elle, importe le contenu du fichier ```levels``` qui contient les différents niveaux.
La fonction Path a pour but de rendre l'arborescence de notre jeu compatible avec tous les systèmes d'exploitations. En effet, elle permet entre autres de trouver le chemin absolu du fichier et donc le repertoire dans lequel se trouve le jeu.

Pour finir, le module random permet d'ajouter quelques effet aléatoires pour éviter une redondance du programme. Ce module a donc été utilisé pour par exemple changer la musique ou créer une grille de jeu aléatoire. 

Les différentes fonctions de notre programme sont appelées soit à l’initialisation du jeu soit lors des événements de la class ```window```.
Nos principales fonctions sont :
* random_level_generation()
* check_existence()
* create_image_store()
* new_level()

### create_image_store:
```python
def create_image_store(ML):
    image_store = {}
    for u in range(4):
        for n in range(4):
            print(ML[3 - n][u])
            init = pyglet.image.load(Path(game_location + '/images/' + ML[3 - n][u] + '.png'))
            init_grid = pyglet.image.ImageGrid(init, 1, 4)
            image_store[ML[3 - n][u]] = init_grid
return image_store
```
La fonction *create_image_store* est utile pour augmenter les performances du programme. En effet, cette fonction,appelée lors de la génération d'un niveau permet de garder en mémoire dans un dictionnaire les images des lettres de la grille. L'autre option aurait été d'ouvrir le fichier chaque fois qu'on en a besoin.
À noter tout de même que les fichiers enrgesitré ne sont pas du type *abstract image*, mais du type *image grid*, ce qui permet aussi d'importer une seul image au lieu de quatre (pour les quatres couleurs du jeu).

### random_level_generation
```python
def random_level_generation():
    all_letter = []
    grid = []
    for letter in levels.scrabble_letter:
        for i in range(levels.scrabble_letter[letter]):
            all_letter.append(letter)
    for i in range(4):
        line = []
        for j in range(4):
            changed_letter = all_letter.pop(randint(0, len(all_letter)-1-4*i-j))
            line.append(changed_letter)
        grid.append(line)
return grid
```
La fonction *random_level_generation* retourne une grille de jeu generée de manière aléatoire, mais qui respecte quand même les limites de nombre de lettre du scrabble francophone.
Afin de généré cette matrice, et pour ne pas dépasser le nombre de lettres limite, nous avons d'abord généré une liste contenant toutes les lettres de l'alphabet, et le nombre de fois correspondant. Ensuite une simple extraction aléatoire de cette liste nous donne notre grille.

### new_level
```python
def new_level():
    init_var()
    if game_state ==  1:
        level += 1
        var = "L" + str(level)
        ML = getattr(levels, var)
    else:
        ML = random_level_generation()
    print(ML)
    image_store = {}
image_store = create_image_store(ML)
```
La fonction *new_level* est celle qui gère le passage d'un niveau à un autre. Pour ce faire, elle remet toutes les variable de jeu à zéro via la fonction *init_var*(qui n'est pas traité ici). Puis change la grille de jeu (*ML*) pour en faire le nouveau niveau.

###  check_existence
```python
def check_existence(search):
    search = str(search + '\r\n')
    search = search.lower()
    string = set(string)
    if search in string:
return True
```

Pour finir, la fonction *check_existence* sert à controller si les mots soumis par l'utilisateur sont valide.Pour ce faire, il lit tout simplement le fichier texte *dico.txt*, est en crée une liste avec un élément par ligne. Ensuite une simple recherche dans ladite liste permet de valider, ou non, le mot de l'utilisateur.


## Conclusion :

Pour conclure, la création de ce jeu nous a apprit à répartir la tâche de travail et à s’organiser de manière optimale. De plus ce fut intéressant de voir le jeu évoluer au fur et à mesure que nous l’avancions. 
