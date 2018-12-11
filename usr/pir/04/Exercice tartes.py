import turtle
import math
bob=turtle.Turtle()

def tarte (n, r):
    angle=360/n
    turn=(180-(angle))/2
    for i in range (n):
        bob.fd(r)
        bob.lt(turn)
        bob.fd(r)
        bob.bk(r)
        bob.rt((180-(angle/2)))
        
nom = input('je suis beau\n')
            
