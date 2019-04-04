import pyglet
import numpy as np

# create n x m matrix with random integers 
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint
n, m = 7, 16
wall = np.random.randint(1, 4, size=(n, m))
print(wall)

# define size of window
window = pyglet.window.Window(800, 600)


# import blocks
blueblock = pyglet.image.load('blueblock.jpg')
greenblock = pyglet.image.load('greenblock.jpg')
yellowblock = pyglet.image.load('yellowblock.jpg')

blocks = [blueblock, greenblock, yellowblock]

# resize blocks
imageWidth = 50
imageHeight = 50
blueblock.width = imageWidth
blueblock.height = imageHeight
yellowblock.width = imageWidth
yellowblock.height = imageHeight
greenblock.width = imageWidth
greenblock.height = imageHeight

# setting an image as the background 

# background = pyglet.image.load('parchemin.jpg')

# displaying a text behind the blocks
poem = """
C'est un trou de verdure où chante une rivière,
Accrochant follement aux herbes des haillons
D'argent ; où le soleil, de la montagne fière,
Luit : c'est un petit val qui mousse de rayons.

Un soldat jeune, bouche ouverte, tête nue,
Et la nuque baignant dans le frais cresson bleu,
Dort ; il est étendu dans l'herbe, sous la nue,
Pâle dans son lit vert où la lumière pleut.

Les pieds dans les glaïeuls, il dort. Souriant comme
Sourirait un enfant malade, il fait un somme :
Nature, berce-le chaudement : il a froid.

Les parfums ne font pas frissonner sa narine ;
Il dort dans le soleil, la main sur sa poitrine,
Tranquille. Il a deux trous rouges au côté droit."""
label = pyglet.text.Label(poem, multiline=True, width=500,
                          font_name='Arial', 
                          font_size=10,
                          x=250, y=580)

@window.event
def on_draw():
    window.clear()
    label.draw()

    # create a random grid with the 3 type of blocks
    for i in range(n):
        for j in range(m):
            x = j * 50
            y = 550 - i * 50
            index = wall[i, j]
            if index > 0:
                block = blocks[index-1]
                block.blit(x, y)


# mouse motions

from pyglet.window import mouse 

@window.event
def on_mouse_motion(x, y, dx, dy):
    pass

# makes a block disappear when clicked on 

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('left click')
        i = (600 - y) // 50
        j = x // 50
        wall[i, j] = 0
        print(x, y, i, j)
    pass


pyglet.app.run()