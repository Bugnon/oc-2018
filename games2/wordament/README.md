# Wordament

* Auteurs: Fabian Roulin, Michael Greub et Mirko Pirona
* Date: Le 25 mai 2019

## Introduction

Des lettres et des mots, tel est le concept. Le but du jeu est similaire à celui du scrabble, c'est à dire, de créer des mots avec des lettres prédéfini. Il existe de nombreuse variantes de ce jeu, mais nous avons décidé de prendre la plus pure, et la plus facile à expliquer et prendre en main.

## Côté poétique

Le côté poétique est apporté par le nombre de personnalisation possible du programme. En effet, pour le moment la liste des mots admis est une liste extraite du dictionnaire Gutenberg ([Source de la liste](http://www.pallier.org/liste-de-mots-francais.html)).  Cependant il est aussi possible de créer une liste avec les noms de tous les poètes, ou une liste des mots à connotation poétique.
Pour ce faire, en marge de notre jeu, nous avons aussi créé un petit script permettant de transformer un fichier texte en liste compatible avec notre jeu.
Pour finir, notre jeu présente un interface simple est lisible, pour permettre la meilleur expérience possible. 

## But du jeux

Le jeux est constitué de deux modes. Le premier se nommant "levels" est un mode dans lequel il faut atteindre un score de 300 avec une grille de lettre 4 x 4 prédéfinie sachant que la valeur des lettres est écrite en dessous de ces dernières. Une fois le niveau terminé le suivant démarre jusqu'au niveau 10. Le deuxième mode s'appelant "endless mode" est un mode dans lequel le but est de faire le plus grand score possible dans une grille générée aléatoirement tout en gardant la base du mode "levels".

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

## Fonctions

Les fonctions de notre programme sont appelées soit à l’initialisation du jeu soit lors des événements de la class ```window```.
Nos principales fonctions sont :

* random_level_generation()
* on_resize()
* check_existence()
* create_image_store()
* new_level()

...



## Explication du jeu :

Lorsque le jeu est lancé, il vous envoie directement dans le menu ou hub du jeu. Là, vous devez choisir le mode de jeu auquel vous désirer jouer. Il y a le mode selected level, qui vous donne des niveaux déjà programmés ou le mode random level qui génère des niveaux aléatoires. 
Dans ces deux modes de jeu, le but est identique. C’est de créer des mots sur la grille. Vous pouvez vous déplacer d’une case sur une des 8 cases adjacentes, soit en haut, à gauche, en bas, à droite ou encore dans les 4 diagonales. 

Pour faire un mot, vous placer le curseur de la souris  sur la première lettres de votre mot et vous appuyer sur le bouton gauche de la souris tout en maintenant le bouton enfoncé. Vous pourrez alors déplacer le curseur afin de compléter votre mot. Quand votre mot serra finit, il vous suffira de relâcher le bouton gauche de la souris pour valider le mot. Lorsque vous créez un mot, les cases utilisées deviennent de couleur jaunes. 
Une fois terminé, si le mot existe, il deviendra vert, dans le cas contraire il deviendra rouge. De plus, si le mot a déjà été fait, il apparaîtra également en rouge. 

Un nombre de point vous sera attribué à chaque mot correct en fonction des lettres utilisées et de la longueur du mot. Le jeu passera au niveau suivants lorsque vous aurez atteint les 50 points. 
Dans le mode random level, en haut à droite se trouve un bouton « next » qui vous permettra de changer de niveau si vous ne parvenez pas aux 50 points nécessaires.

...

# Conclusion :

Pour conclure, la création de ce jeu nous a apprit à répartir la tâche de travail et à s’organiser de manière optimale. De plus ce fut intéressant de voir le jeu évoluer au fur et à mesure que nous l’avancions. 
