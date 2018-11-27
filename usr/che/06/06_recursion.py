# File: 06_recursion.py
# Author: Terence Chevroulet
# Date: 27.11.2018

# Saisie au clavier

#name= input('Votre nom ')
#print('Hello, '+name)

import math
print("Calcul de l'hypothénuse")

a=float(input('A: '))
b=float(input('B: '))

c=math.sqrt(a**2+b**2)
print('C: ',c)