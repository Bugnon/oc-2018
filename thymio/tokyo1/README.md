# Projet Tokyo 1



## Fonctionnement général

### Affichage

Les *secondes* sont affichées sur les *leds de proximité leds.prox.h*

Les *minutes* sont affichées sur les *leds circulaires*

Les *heures* sont affichées sur les *leds des boutons*

Les *heures* ne pouvant aller que jusqu'à 12, une lumière est utilisée pour représenter AM/PM

### Modules

Quatre *modules* sont disponibles :

- Horloge (Mauve)

- Alarme (Rouge)

- Chronomètre (Jaune)

- Timer (Vert)

### Variables

Les quatre *modules* fonctionnent autour d'un *module* central, qui utilise les variables suivantes : 

- display_h : 0-12 : affichage des heures

- display_m : 0-60 : affichage des minutes

- display_s : 0-60 : affichage des secondes

- am : 0-1 : AM ou PM?

- mode : 0-3 :  module sélectionné

- active : 0-1 : sélection active? 

### Sélection des modules

Les modules sont sélectionnés en utilisant les boutons *gauche* et *droite*. Ils sont ensuite validés en utilisant le bouton *central*

## Modules

### Horloge
  
Le module horloge est lancé avec le *bouton central* après avoir été sélectionné. 

Il affiche simplement les heures/minutes/secondes quand actif, et continue de faire passer le temps en arrière plan.

Le *module alarme* en dépend.

### Alarme

Les capteurs de proximité verticale sont utilisés pour choisir quelle variable incrémenter : *heures, minutes, secondes.*

Les boutons avant/arrière sont utilisés pour incrémenter/décrémenter. 

### Le reste est à venir :c
