# File: 06_recursion.py
# Author: Terence Chevroulet
# Date: 27.11.2018

# Saisie au clavier

#name= input('Votre nom ')
#print('Hello, '+name)
##
##import math
##print("Calcul de l'hypothénuse")
##
##a=float(input('A: '))
##b=float(input('B: '))
##
##c=math.sqrt(a**2+b**2)
##print('C: ',c)

import turtle
turtle.speed(0)
turtle.setup(width=700, height=300)

def save(img):
    cv=turtle.getcanvas()
    img_name=img+'.eps'
    cv.postscript(file=img_name, colormode='color')
    
##Ex 5.5
def dessiner(a, n):
##    a -> longueur du segment
##    n -> nombre de niveaux
    if n==0:
        return
    angle=50
    turtle.fd(a*n)
    turtle.lt(angle)
    dessiner(a,n-1)
    turtle.rt(2*angle)
    dessiner(a,n-1)
    turtle.lt(angle)
    turtle.bk(a*n)