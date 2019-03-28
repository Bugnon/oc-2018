import pyglet, random, math, time
from random import randint

#Define variables
window_height=800
window_width=1000

# Set up a window
window = pyglet.window.Window(window_width, window_height)
batch = pyglet.graphics.Batch()

#show current verse at a fixed point no matter the window's size : 1% padding to the left,
verse = pyglet.text.Label(text="Vers", x=window_width/100, y=window_height-(window_height/30), font_size=window_height/40, batch=batch)

# create a new class
class FloatingLabel(pyglet.text.Label):

    # constructor function calling
    def __init__(self, *arg, **kwargs):
        # calling parent constructor function
        super().__init__(*arg, **kwargs)
        self.x = randint(-2, 0)
        self.y = randint(-5, 5)
        self.dx = randint(-2, 0)
        self.dy = randint(-2, 2)
        
    def update(self, dt):
        self.x += self.dx
        self.y += self.dy
        self.x %= window.width
        self.y %= window.height
        
        
mots = ['Alexandrin', 'ballade', 'césure', 'rime', 'poème', 'décasyllabe', 'fables','lyrique','sizain','strophe','tercet','hpetasyllabe']
mots2 = ['arbre', 'soleil', 'monde','banane','table','sac','stylos','coiffeur','lunette','pull','bracelet','montre']
labels = []

for mot in mots:
    label = FloatingLabel(mot, font_size=randint(12, 36), batch=batch)
    labels.append(label)

for mot in mots2:
    label = FloatingLabel(mot, font_size=randint(12, 36), batch=batch)
    labels.append(label)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    for label in labels:
        label.update(dt)

pyglet.clock.schedule_interval(update, 1/60) # update at 10Hz
pyglet.app.run()




# mots = ['poétique', 'beau', 'frémissant']

# while True:
#     #answer = input('enter an index (0-2): ')

#     answer = input('enter a word: ')

#     if answer in mots:
#         print('yes')
#     else:
#         print('no')