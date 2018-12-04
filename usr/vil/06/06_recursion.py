#File: 06_recusrcion.py
#author: Victoria Vila
# saisie duc clavier


import turtle
turtle.setup(width=700, height=300)

def save(img):
    cv = turtle.getcanvas()
    img_name= img + '.eps'
    cv.postscript(file=img_name, colormode='color')
    
# exercie 5.5
def dessiner(a, n):
    # a: longueure du segement
    # n: nombre de niveaux
    if n==0:
        return
    angle = 50
    turtle.fd(a * n )
    turtle.lt(angle)
    dessiner(a, n-1)
    turtle.rt(2*angle)
    dessiner(a, n-1)
    turtle.lt(angle)
    turtle.bk(a * n)
    
dessiner(30, 3)
save('tree_30_3')

turtle.reset()
dessiner(20, 4)
save('tree_20_4')

turtle.reset()
dessiner(16, 5)
save('tree_26_5')
