# Poetic Breakout

* Authors: Pierre Gaglio, Jérémy Werro & Nisa Azizi
* Date: 26.05.2019

## Introduction

Au cours de l’année 2019, un évènement a eu lieu dans tout l’ouest de la Suisse ainsi que dans plusieurs villes partout dans le monde durant le mois d’avril : Le printemps de la poésie.
Cet événement s’est déroulé durant tout le mois d’avril et a consisté à proposer durant tout un mois des évènements ainsi que des activités liés à la poésie. ( pour plus d’informations, veuillez-vous référer au [site.](http://printempspoesie.ch)
Le gymnase vaudois du bugnon a décidé de prendre part au printemps de la poésie en faisant participer le corps enseignant ainsi que les élèves, tout au long d’une semaine, à des activités poétiques diverses et variées.
Dans le cadre de l’option complémentaire de 3ème année gymnasiale d’informatique, nous avons travaillé sur la programmation d’un jeu à thème poétique. Pour se faire, chaque groupe a proposé le style de jeu sur lequel travailler. 

Notre groupe a donc choisi de travailler sur un jeu de style « Casse-brique ». Ce style de jeu consiste, à l’aide d’une plateforme que le joueur contrôle, à faire rebondir une balle sur des briques sans laisser tomber ladite balle.
Afin d’ajouter notre côté poétique à notre jeu, nous avons décidé de travailler sur la reconstitution d’un poème à l’aide du cassage de brique.


## Explication du jeu 

Le jeu est inspiré du casse-briques classique. Il présente donc une barre horizontale, une balle et des briques. Plusieures lignes de briques se trouvent sur le haut de l'écran et le but est de les faire toutes disparaître à l'aide de la balle qui les détruit au moment où elle les touche. La balle traverse l'écran, rebondit sur les parois droite, gauche et supérieure et redescend lorsqu'elle touche une brique. C'est à ce moment que le joueur doit déplacer la barre horizontale se trouvant en bas de l'écran, afin d'éviter que la balle ne touche la paroi inférieure et qu'il perde donc la partie ou une vie. À chaque fois que la balle touche la barre, sa vitesse de déplacement augmente et, de ce fait, la difficulté du jeu. Voici [la page Wikipedia de ce jeu.](https://fr.wikipedia.org/wiki/Casse-briques) pour un approfondissement des mécaniques du jeu.

Notre jeu est donc une adaptation du casse-brique afin que l'on puisse y retrouver un côté poétique, il garde donc les règles de bases expliquées ci-dessus. Pendant la partie, un poème comprennant des lacunes est affiché en bas à gauche de l'écran. Les mots qui manquent seront écrits sur certaines briques et le but du joueur sera de casser ces briques afin de remplir les lacunes pour que son poème soit complet. Le joueur dispose alors de 45 secondes et 3 vies pour compléter le poème (le temps ainsi que les vies étant définies de manière arbitraires mais n'étant pas définitives). S'il réussit, il accède à la partie et au poème suivant. Le jeu comporte 5 niveaux dont la difficulté augmente graduellement. D'une part, à cause du nombre de lacunes qui devient de plus en plus important et d'autre part, à cause de la vitesse initiale de la balle qui augmente, elle aussi, à chaque niveau.

## Fonctionnement du programme

Notre jeu est composé d'un fichier nommé **BreakoutGame.py** ainsi que d'un dossier nommé **images** contenant 
toutes les images utilisées pour la programmation de notre jeu. Vous trouverez tout cela dans le dossier nommé **Game_Breaker**.

### Fonctionnement général du programme

Pour que notre programme puisse être fonctionnel, nous devons procéder en plusieurs étapes:

* En premier lieu, nous devons importer les modules de [pyglet](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html) nécessaires pour le bon fonctionnement des classes.
```
import pyglet
import time
import math
from pyglet.window import key
from pyglet.window import FPSDisplay
```

* Ensuite, nous programmons 3 classes différentes qui intéragiront entre elles:
    * La ``` class Ball() ```. 
    * La ``` class Player() ```. 
    * La ``` class Brique() ```. *À noter que la classe Brique n'a pas pu être intégrée dans notre fichier final susnommé **BreakoutGame.py**. Vous trouverez le code de cette classe dans le fichier nommé **breakoutbriques.py**.*
    
Pour plus de précision, veuillez vous référer au code et à ses explications[](https://github.com/Bugnon/oc-2018/blob/master/games2/breakout/Game_Breaker/BreakoutGame.py)

Finalement, nous définissons une fonction ```on_draw() ``` qui aura pour but de lancer le jeu.

### Intéractions clavier

Nous avons choisi de n'utiliser que 3 touches pour pouvoir utiliser notre jeu.
* **les flèches directionnelles droite et gauche**, qui permettront au joueur de faire se déplacer la barre vers la gauche ou vers la droite.
* **La touche spacebarre** qui permettre au joueur de lancer le jeu en activant le mouvement de la balle.

## Conclusion

Pour ce projet, le travail a été réparti équitablement entre les 3 programmeurs:
* **Azizi Nisa** s'est occupé de la programmation de la ``` class Brique() ```.
* **Werro Jeremy** s'est occupé de la programmation de la ``` class Ball() ```. 
* **Gaglio Pierre** s'est occupé de la programmation de la ``` class Player() ```.

Nous avons ensuite tenté de joindre nos travaux ensemble afin de rendre notre jeu fonctionnel et d'arriver à un résultat rendant notre programme jouable.

Cependant, notre équipe a rencontré un problème majeur qui ne nous a pas permis d'aboutir à une version jouable. Effectivement,  nos programmeurs, ayant des ordinateurs sous système d'exploitation *Windows*, n'ont pas pu installer le module *Pyglet* sur leur ordinateur personnel, malgré leurs efforts et la demande d'assistance à des personnes travaillant dans ce milieu. De ce fait, le travail n'a pu être avancé que difficilement en cours ou sur des périodes restreintes hors cours rendant notre avancement compliqué. Néanmoins, il nous a été possible d'assembler la partie *Player* ainsi que la partie *Balle* ensemble afin de donner un premier rendu du travail accompli.

L'enjeu poétique n'a pas pu non plus être accompli du fait des complications nommées ci-dessus. 

Nous vous remercions de votre lecture.
