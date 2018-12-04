# File: 06_recursion.py
# Author: jeremy werro
# Date: 27.11.2018

# Saisie au clavier

#name=input('Votre nom: ')
#print('\nHello', name)

import math
print("Calcul de l'hypothénus")

a = float(input('a: '))
b = float(input('b: '))

c = math.sqrt(a**2 + b**2)
print('c: ', c)
