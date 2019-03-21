import pyglet, random, math
from random import randint

# Set up a window
window = pyglet.window.Window(800, 600)
batch = pyglet.graphics.Batch()

# create a new class
class FloatingLabel(pyglet.text.Label):

    # constructor function calling
    def __init__(self, *arg, **kwargs):
        # calling parent constructor function
        super().__init__(*arg, **kwargs)
        self.x = randint(0, 500)
        self.y = randint(0, 500)
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        
    def update(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.x %= window.width
        self.y %= window.height

        
mots = ['poétique', 'beau', 'frémissant']

labels = []
for mot in mots:
    label = FloatingLabel(mot, font_size=36, batch=batch)
    labels.append(label)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    for label in labels:
        label.update(dt)

pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz
pyglet.app.run()




# mots = ['poétique', 'beau', 'frémissant']

# while True:
#     #answer = input('enter an index (0-2): ')

#     answer = input('enter a word: ')

#     if answer in mots:
#         print('yes')
#     else:
#         print('no')