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

# A Continuer
