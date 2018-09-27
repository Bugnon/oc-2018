# Projet Tokyo 2
La **Tokyo Watch** est une **montre binaire** ayant 4 modes différents correspondant chacun à une couleur sur la lumière du dessus du robot (voir image 1) :
* Quand les leds sont **éteintes**, cela correspond au mode « **montre** »
* Le **rouge** correspond au mode « **chronomètre** »
* Le **vert** correspond au mode « **minuteur** »
* Le **bleu** correspond au mode « **Alarme** »

## Fonctionement
* Le mode « **montre** » permet d’afficher **l’heure en binaire**. La montre affiche sur les différentes lumières du robot les heures, les minutes et les secondes.
* Le mode « **chronomètre** » permet de **chronométrer** un temps en heures, minutes et secondes et d’avoir *un temps intermédiaire*.
* Le mode « **minuteur** » est un dispositif permettant de **séléctioner une durée** qui, quand elle est écoulée, permet de déclencher une alarme.
* Le mode « **alarme** » permet de **sélectionner** une heure (heures, minutes et secondes) à laquelle on souhaite que la montre sonne.
## Définitions des commandes

![Numérotations des boutons du thymio](https://github.com/Bugnon/oc-2018/blob/master/img/thymio.jpg)

* Le bouton **1** sert à **changer de mode**
### Horloge
* Incrémenter : 2
* Décrémenter : 4
### Alarme
* Incrémenter : 2
* Décrémenter : 4
* Arrêter : taper sur le Thymio
### Chronomètre
* Play/pause : 3
* Reset : 2
* Temps intermédiaire : 5
### Timer
* Incrémenter : 2
* Décrémenter : 4
## Affichage
Les **leds du cercle** représentent les minutes sauf pour le _chronomètre_ où elles représentent les _secondes_.

Les **leds du devant** représentent les heures sauf pour le _chronomètre_ où elles représentent les _minutes_ et pour le _timer_ ou elles représente les secondes.

