# cercle
from math import *

r=10

def circle(r):
    d = 2 * r
    circ = d * pi
    surface = pi * r**2
    print("Rayon : "+str(r))
    print("Diamètre : "+str(d))
    print("Circonférence : "+str(circ))
    print("surface : "+str(surface))