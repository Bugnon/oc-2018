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
Nous n'allons pas vous présenter le code en entier, car il est très long. Néanmoins, nous allons vous expliquer les Variables, les Class et les méthodes principales pour pouvoir comprendre comment fonctionne le jeu. La boucle de notre jeu se trouve dans inkvader.py, les entités dans inkentities.py, les différentes fenêtres de jeu et leur configuration et fonctionnement dans inkgame.py, et finalement quelques utilitaires dans inktilities.py.

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
Dans Inkvader, on utilise la souris et le clavier de cette manière-ci.

* La souris s'utillise pour lancer le jeu. (insérer code) 

* Dans le clavier, on utilise ces quatre flèches pour déplacer la plume
=>
On utilise la touche "space bar" pour tirer les tâches d'encre sur les mots. (insérer code) 
On utilise la touche "enter" afin de mettre sur pause.

### Explication du jeu 

* Le but: Le but du jeu est d'écrire le poème "Le Dormeur du Val" de Rimbaud.

Premierement on doit mettre en marche le jeu, en cliquant avec la souris sur l'écrans. Ensuite nous devons nous deplacer à l'aide des quatres flèches sur le clavier, montrées ci-dessus, afin de se positionner sur l'écran de maniere à pouvoir tirer sur un mot poétique. Il faut ensuite appuyer sur la barre d'espace pour tirer une tâche d'encre sur un mot. Il faut viser les mots poétiques, car à chaque fois qu'on en touche un, le poème s'écrit mot à mot en haut de l'écran.
