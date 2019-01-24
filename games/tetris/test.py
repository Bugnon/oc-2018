from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
white = (255, 255, 255)
black = (0, 0, 0)

colors = (red, magenta, blue, cyan, green, yellow, white, orange)

### FORMES ###

i = cyan
o = yellow
t = magenta
l = orange
j = blue
z = red
s = green
x = black

I = [i, i, i, i] #Barre en cyan
     
O = [[o, o],
     [o, o]] ## Carré en jaune
     
T = [[t, t, t],
     [x, t, x]] ##T en violet
     
L = [[l, l, l],
     [l, x, x]] ##L en orange
     
J = [[j, j, j],
     [x, x, j]] ##J en bleu
     
Z = [[z, z, x],
     [x, z, z]] ##Z en rouge
     
S = [[x, s, s],
     [s, s, x]] ##S en vert
    
sense.set_pixels(Z)
sleep(3)

