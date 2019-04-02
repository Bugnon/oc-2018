import pyglet
from pyglet.window import key

window = pyglet.window.Window()
image = pyglet.resource.image('resources/ball.gif')
x = 200
y = 200

@window.event
def on_draw():
    window.clear()    
    image.blit(x, y)

@window.event
def speed():
    global x, y, s
    



@window.event
def on_key_press(symbol, modifiers):
    global x, y
    d = 4
    if symbol == key.LEFT:
        print('la balle va à gauche')
        x -= d
    elif symbol == key.RIGHT:
        print('la balle va à droite')
        x += d
    elif symbol == key.UP:
        print('la balle va en haut')
        y += d
    elif symbol == key.DOWN:
        print('la balle va en bas')
        y -= d
    print(x, y)

pyglet.app.run()