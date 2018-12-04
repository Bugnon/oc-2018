# File: 06_recursion.py
# Auteur: Massimo Stefani
# Date: 27.11.2018

# Siasie au clavier

#name = input('Votre nom: ')
#print('Hello', name)

#Calculer HYP triangle
##import math
##print("Calcul de l'HYP")
##a = float(input('un nombre: '))
##b = float(input('un nombre: '))
##
##c = math.sqrt(a**2 + b**2)
##print('c:', c)

import turtle
turtle.setup(width=700, height=300)
def save(img):
    cv = turtle.getcanvas()
    img_name = img + '.eps'
    cv.postscript(file=img_name, colormode='color')
    
# EX 5.5

def dessiner(a, n):
##a: longueur du segment
##    n: nombre de niveaux
    if n==0:
        return
    angle = 50
    turtle.fd(a * n)
    turtle.lt(angle)
    dessiner(a, n-1)
    turtle.rt(2*angle)
    dessiner(a, n-1)
    turtle.lt(angle)
    turtle.bk(a * n)

dessiner(14, 5)
save('tree_20_4')