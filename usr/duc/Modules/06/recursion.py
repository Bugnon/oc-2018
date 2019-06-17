# Files 06 : récursion
# Author : Hugo Ducommun
# Date : 27.11.2018

# Saisie du clavier

name = input("Votre nom : ")
print ("\nHello", name, '\n')

# Théorème de Pythagore

import math

print('Programme du théorème de Pythagore')
print("Calul de l'hypothènuse\n")

a=float(input('La catète a : '))
b=float(input('La catète b : '))

c=math.sqrt(a**2 + b**2)
print('L\'hypothénuse c = ', c)
