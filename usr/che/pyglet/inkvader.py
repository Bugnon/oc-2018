import pyglet, random, math, time
from pyglet.window import key, mouse
from random import randint

# Resources 
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()
pen_image = pyglet.resource.image('pen.png')
ink_image = pyglet.resource.image('ink.png')

game_objects = []

# Define variables
platform = pyglet.window.get_platform()
display = platform.get_default_display()      
screen = display.get_default_screen()
window_width = screen.width
window_height = screen.height

has_fired=0

# Set up a window
window = pyglet.window.Window(fullscreen=True)
batch = pyglet.graphics.Batch()

#show current verse at a fixed point no matter the window's size : 1% padding to the left,
verse = pyglet.text.Label(text="Vers", x=window_width/100, y=window_height-(window_height/30), font_size=window_height/40, batch=batch)
#versetest = pyglet.text.Label(text=str(window_height-(window_height/30)), x=10, y=10, font_size=window_height/40, batch=batch)

'''Formula to calculate distance between point A and B. Accepts (A, B)'''
def distance(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

'''Creates a class for the floating text'''
class FloatingLabel(pyglet.text.Label):

    # constructor function calling
    def __init__(self, *arg, **kwargs):
        # calling parent constructor function
        super().__init__(*arg, **kwargs)
        self.x = randint(int(2/3*window_width),window_width)
        self.y = randint(0,window_height)
        self.dead = False

        self.dx = randint(-2, -1)
        self.dy = randint(-2, 2)

        self.react_to_ink = True
        self.is_ink = False

        self.new_objects = []

    '''Applies acceleration when object moves, and ensures it stays within the game's borders'''
    def update(self, dt):
        w, h = window.width, window.height
        self.x += self.dx
        self.y += self.dy
        self.x = (self.x - 200) % (w-200) +200
        #self.x %= window.width-(window.width/10)
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
        self.x = window_width / 100
        self.y = window_height / 2
        self.dy = 0.0

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        self.react_to_ink = False
        self.is_ink = False
        self.dead = False
        
        self.new_objects = []


    def update(self, dt):
        
        global has_fired
        
        if self.key_handler[key.UP]:
            self.dy = 10
        elif self.key_handler[key.DOWN]:
            self.dy = -10
        else:
            self.dy = 0
        
        if self.key_handler[key.RIGHT] and has_fired==0:
            self.fire()
            has_fired=60
            print("fired")
        elif has_fired >0:
            has_fired-=1
        else:
            pass    

        self.y += self.dy
        self.y %= window_height-(window_height/15) #Creates a zone free of word on top of the screen
        #if self.y < 20:
        #    self.y = 20

    # Create and launch ink
    def fire(self):
        print(self.x, self.y)
        ink_x = self.x
        ink_y = self.y
        print(ink_x,ink_y)
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
        self.dx = 7
        # Kills the ink blob after it has had the time to travel through the map
        pyglet.clock.schedule_once(self.die, window_width/(9/10*self.dx*60))
        self.is_ink = True
        
        # Collision attributes
        self.react_to_ink = False
        self.is_ink = True
        self.dead = False

        self.new_objects = []


    def update(self, dt):
        self.x += self.dx

    # Marks the ink blob as dead
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
pen.rotation = 0

# Registering key event handler
window.push_handlers(pen.key_handler)

for mot in mots:
    label = FloatingLabel(mot, font_size=randint(12, 36), batch=batch)
    labels.append(label)

#for mot in mots2:
#    label = FloatingLabel(mot, font_size=randint(12, 36), batch=batch)
#    labels.append(label)


game_objects.append(pen)
game_objects.extend(labels)


@window.event
def on_draw():
    #pyglet.gl.glClearColor(.8, 0.8, 0.8, 1)
    window.clear()
    batch.draw()
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a beautiful line 
        ("v2f", (0, window_height-(window_height/20), window.width, window_height-(window_height/20)))
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
    
    

pyglet.clock.schedule_interval(update, 1/60) # update at 60Hz
pyglet.app.run()