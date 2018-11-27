# File: 06_recursion.py
# Author: Raphael Holzer
# Date: 27. 11. 2018

# Saisie au clavier

##name = input('Votre nom: ')
##print('\nHello', name)

# Théorème de Pythagore

import math
print("Calcul de l'hypothénuse")
      
a = float(input('a: '))
b = float(input('b: '))

c = math.sqrt(a**2 + b**2)
print('c:', c)
