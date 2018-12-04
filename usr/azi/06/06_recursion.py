#file: 06_recursion.py
#Author : Nisa Azizi
#Date : 27.11.2018

#saisie au clavier

#théorème de pythagore
##import math
##print("calcul de l'hypothénuse")
##
##a = float(input('a: '))
##b = float(input('b: '))
##c = math.sqrt(a**2 + b**2)
##print('c:', c)

import turtle

turtle.setup(width=700, height =300)

def save(img) :
    cv = turtle.getcanvas()
    img_name= img + '.eps'
    cv.postscript(file=img_name, colormode='color')
    

#exercice 5.5
def dessiner (a, n):
    #a : longueur segment
    #n : nombre de niveaux
    if n==0 :
        return
    angle = 50
    turtle.fd(a*n)
    turtle.lt(angle)
    dessiner(a, n-1)
    turtle.rt(2*angle)
    dessiner(a, n-1)
    turtle.lt(angle)
    turtle.bk(a*n)
    
dessiner(30,3)
turtle.reset()
dessiner(30,4)
