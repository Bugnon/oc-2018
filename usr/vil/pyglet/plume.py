import pyglet, random, math, time
from pyglet.window import key, mouse
from random import randint

# Resources 
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()
pen_image = pyglet.resource.image('stylos.png')
ink_image = pyglet.resource.image('ink.png')

game_objects = []

# Define variables
window_height=800
window_width=1000

# Set up a window
window = pyglet.window.Window(window_width, window_height)
batch = pyglet.graphics.Batch()

#show current verse at a fixed point no matter the window's size : 1% padding to the left,
verse = pyglet.text.Label(text="Vers", x=window_width/100, y=window_height-(window_height/30), font_size=window_height/40, batch=batch)
versetest = pyglet.text.Label(text=str(window_height-(window_height/30)), x=10, y=10, font_size=window_height/40, batch=batch)


def distance(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def random_position(label):
    x = label.x
    y = label.y
    while distance((label[0], label[1]), (x, y)) < 20:
        x = randint(-10, 10)
        y = randint(-10, 10)
    return x, y


# create a new class
class FloatingLabel(pyglet.text.Label):

    # constructor function calling
    def __init__(self, *arg, **kwargs):
        # calling parent constructor function
        super().__init__(*arg, **kwargs)
        self.x = randint(-2, 0)
        self.y = randint(-10, 10)
        self.dead = False

        #for i label in labels:
        #   self.x, self.y = random_position(label.x, label.y)
        self.dx = randint(-2, 0)
        self.dy = randint(-2, 2)

        self.react_to_ink = True
        self.is_ink = False

        self.new_objects = []

        
    def update(self, dt):
        self.x += self.dx
        self.y += self.dy
        self.x %= window.width
        self.y %= window_height-(window_height/15)


    def collides_with(self, obj):
        # Ignore ink collisions if we're supposed to
        if not self.react_to_ink and obj.is_ink:
            return False
        if self.is_ink and not obj.react_to_ink:
            return False

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        if obj.__class__ == self.__class__:
            other_width = obj.content_width
        else:
            other_width = obj.width
        collision_distance = self.content_width / 2 + other_width / 2

        # Get distance using position tuples
        actual_distance = distance((self.x, self.y), (obj.x, obj.y))

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, obj):
        if obj.__class__ is not self.__class__:
            self.dead = True


class Pen(pyglet.sprite.Sprite):

    def __init__(self, *arg, **kwargs):
        super().__init__(img=pen_image, *arg, **kwargs)
        self.x = 150
        self.y = window_height / 2
        self.dy = 0.0

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        self.react_to_ink = False
        self.is_ink = False
        self.dead = False
        
        self.new_objects = []


    def update(self, dt):
        if self.key_handler[key.UP]:
            self.dy = 10
        elif self.key_handler[key.DOWN]:
            self.dy = -10
        else:
            self.dy = 0
        
        if self.key_handler[key.SPACE]:
            self.fire()     

        self.y += self.dy
        self.y %= window_height-(window_height/15)
        #if self.y < 20:
        #    self.y = 20


    # Launch ink when spacebar is pressed
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    # Launch ink when left mouse button is pressed
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.fire()

    # Create and launch ink
    def fire(self):
        print(self.x, self.y)
        ink_x = self.x
        ink_y = self.y
        ink = Ink(x=ink_x, y=ink_y, batch=batch)
        ink.scale = 0.05
        self.new_objects.append(ink)


    def collides_with(self, obj):
        # Ignore ink collisions if we're supposed to
        if not self.react_to_ink and obj.is_ink:
            return False
        if self.is_ink and not obj.react_to_ink:
            return False

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        if obj.__class__ == self.__class__:
            other_width = obj.width
        else:
            other_width = obj.content_width
        collision_distance = self.width / 2 + other_width / 2

        # Get distance using position tuples
        actual_distance = distance((self.x, self.y), (obj.x, obj.y))

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, obj):
        if obj.__class__ is not self.__class__:
            self.dead = True


class Ink(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=ink_image, *args, **kwargs)
        pyglet.clock.schedule_once(self.die, 1)
        self.is_ink = True
        self.x = 100
        self.y = 100
        self.dx = 10
        
        # Collision attributes
        self.react_to_ink = False
        self.is_ink = True
        self.dead = False

        self.new_objects = []


    def update(self, dt):
        self.x += self.dx


    def die(self, dt):
        self.dead = True

    def collides_with(self, obj):
        # Ignore ink collisions if we're supposed to
        if not self.react_to_ink and obj.is_ink:
            return False
        if self.is_ink and not obj.react_to_ink:
            return False

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        collision_distance = self.width / 2 + obj.width / 2

        # Get distance using position tuples
        actual_distance = distance((self.x, self.y), (obj.x, obj.y))

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, obj):
        if obj.__class__ is not self.__class__:
            self.dead = True



mots = ['Alexandrin', 'ballade', 'césure', 'rime', 'poème', 'décasyllabe', 'fables','lyrique','sizain','strophe','tercet','hpetasyllabe']
mots2 = ['arbre', 'soleil', 'monde','banane','table','sac','stylos','coiffeur','lunette','pull','bracelet','montre']
labels = []

# Pen creation
pen = Pen(batch=batch)
pen.scale = 0.2
pen.rotation = 225

# Registering key event handler
window.push_handlers(pen.key_handler)


for mot in mots:
    label = FloatingLabel(mot, font_size=randint(12, 36), batch=batch)
    labels.append(label)

for mot in mots2:
    label = FloatingLabel(mot, font_size=randint(12, 36), batch=batch)
    labels.append(label)


game_objects.append(pen)
game_objects.extend(labels)


@window.event
def on_draw():
    pyglet.gl.glClearColor(.8, 0.8, 0.8, 1)
    window.clear()
    batch.draw()
    pyglet.graphics.draw(4, pyglet.gl.GL_LINES, 
        ("v2f", (0, 0, 0, window.height, 0, window_height-(window_height/20), window.width, window_height-(window_height/20)))
    )


def update(dt):
    # Check collisions for all objects
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):

            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            # Make sure the objects haven't already been killed
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    to_add = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    # Get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        # If the dying object spawned any new objects, add those to the game_objects list later
        to_add.extend(obj.new_objects)

        # Remove the object from any batches it is a member of
        to_remove.delete()

        # Remove the object from our list
        game_objects.remove(to_remove)

    # Add new objects to the list
    game_objects.extend(to_add)



    # Update each object
    #for obj in game_objects:
    #    obj.update(dt)
    #    if obj.dead:
    #        objects_to_remove.append(obj)

    # Delete dead objects
    #for obj in objects_to_remove:
    #    obj.delete()
    #    game_objects.remove(obj)
        
    # Add new objects to game_objects
    #game_objects.extend(objects_to_add)
    
    

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