# File: 06_recursion.py
# Author: Michael Greub
# Date: 27.11.2018

# Saisi au clavier
#
#name=input('votre nom: ')
#print('\n Hello ', name)
#
#a=input('Un nombre : ')
#a=float(a)
#
#print(a)
#print(a*2)

import turtle
turtle.speed(9999)
def save():
    img=input('Nom de l\'image')
    cv=turtle.getcanvas()
    img_name = img + '.eps'
    cv.postscript(file=img_name, colormode='color')

# exercice 5.5
def dessiner(a, n):
#    a: longueur du segment
#    n: nombre de niveaux
    if n==0:
        return
    angle=30
    turtle.fd(a*n)
    turtle.lt(angle)
    dessiner(a, n-1)
    turtle.rt(2*angle)
    dessiner(a, n-1)
    turtle.lt(angle)
    turtle.bk(a*n)

