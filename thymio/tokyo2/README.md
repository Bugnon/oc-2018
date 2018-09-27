# Projet Tokyo 2

## définitions de variables 

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

Les **leds du devant** représentent les heures sauf pour le _chronomètre_ où elles représentent les _minutes_.
## Les différents états du robot
Les différents **modes** sont représentés par les **leds du dessus**.
* Blanc = Horloge
* Vert = Alarme
* Rouge = Chronomètre
* Bleu = Timer

### Pour montre
* heure => h
* minute => m
* seconde => s

### Chronométre

* heure => c-h
* minute => c-m
* seconde => c-s

### Alarme

* heure => a-h
* minute => a-m
* seconde => a-s

### Timer

* heure => t-h
* minute => t-m
* seconde => t-s


# Définitons des boutons

* Bouton central => changement de mode (montre, chrono, horloge, timer)
* Bouton avancer => augmenter la valeur
* Bouton reculer=> descendre la valeur
* Bouton gauche => set / pause / désafficher la pause du chrono
* Bouton droit => Démarrage / Stop

# Définition des leds

* Leds du cercle => minutes
* Leds de proximité avant (celles en haut uniquement) => secondes
* Leds des boutons + autre led à définir => heures
* Led du top=> état du robot (aucune lumière = aucun état (montre) / rouge = état 2 (chronomètre) / vert = état 1 (alarme) / bleu = état 3 (Timer)
