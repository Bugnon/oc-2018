# Turtle

import turtle

bob = turtle.Turtle()

def polygon(length, poly):
    
    for i in range(poly):
        
        bob.fd(length)
        bob.lt(360/poly)
        
        
def polygonright(length, poly):
    
    for i in range(poly):
        
        bob.fd(length)
        bob.rt(360/poly)
        
def starbase(t, a, n):
    for i in range(n):
        t.fd(a)
        t.bk(a)
        t.lt(360/n)


