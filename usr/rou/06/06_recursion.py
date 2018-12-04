# File: 06_recursion.py
# Author : Fabian Roulin
# Date : 27.11.2018

# Saisie au clavier

#name = input("Votre nom: ")
#print("Hello", name)

import math

print("Calcule de l'hypothénuse")
a = float(input("une catètte: "))
b = float(input("l'autre catètte: "))

c = math.sqrt(a**2 + b**2)
print("L'hypothénuse vaut: ", c)
i=0

d = input("Recommencer: ")

