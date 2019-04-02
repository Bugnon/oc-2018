import pyglet, random, math, time, inktilities
from pyglet.window import key, mouse
from random import randint

pyglet.options['audio'] = ('openal', 'silent')

# Resources 
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()
pen_image = pyglet.resource.image('pen.png')
ink_image = pyglet.resource.image('ink.png')
fire_sound = []
for i in range(7):
    fire_sound.append(pyglet.media.load('./resources/sounds/WaterDrop0' + str(i) + '.wav', streaming=False))

game_objects = []

# Music
# create a player and queue the song
player = pyglet.media.Player()
sound = pyglet.media.load('./resources/music/Furious Freak.wav')
player.queue(sound) 

# keep playing for as long as the app is running (or you tell it to stop):
player.eos_action = pyglet.media.SourceGroup.loop

player.play()

# Get screen size
window_width = inktilities.screenInfo("x")
window_height = inktilities.screenInfo("y")

# Define ink variables
ink_scale = window_width/(ink_image.width*100)
ink_image.anchor_x = ink_image.width / 2
ink_image.anchor_y = ink_image.height / 2

# Define pen variables
has_fired = 0
fire_treshold = 30
pen_image.anchor_x = pen_image.width / 2
pen_image.anchor_y = pen_image.height / 2

# Set up a window
window = pyglet.window.Window(fullscreen=True)
batch = pyglet.graphics.Batch()

#show current verse at a fixed point no matter the window's size : 1% padding to the left,
verse = pyglet.text.Label(text="Vers", x=window_width/100, y=window_height-(window_height/30), font_size=window_height/40, batch=batch)
#versetest = pyglet.text.Label(text=str(window_height-(window_height/30)), x=10, y=10, font_size=window_height/40, batch=batch)

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
        actual_distance = inktilities.distance((self.x, self.y), (obj.x, obj.y))

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, obj):
        if obj.__class__ is not self.__class__:
            self.dead = True


class Pen(pyglet.sprite.Sprite):

    def __init__(self, *arg, **kwargs):
        super().__init__(img=pen_image, *arg, **kwargs)
        self.x = window_width / 4
        self.y = window_height / 2

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        self.react_to_ink = False
        self.is_ink = False
        self.dead = False
        
        self.new_objects = []


    def update(self, dt):
        global fire_treshold
        global has_fired
        
        if self.key_handler[key.UP]:
            self.dy = 10
        elif self.key_handler[key.DOWN]:
            self.dy = -10
        else:
            self.dy = 0

        if self.key_handler[key.RIGHT] and self.x < window_width / 2:
            self.dx = 5
        elif self.key_handler[key.LEFT] and self.x > window.width / 5:
            self.dx = -5
        else:
            self.dx = 0
        
        if self.key_handler[key.SPACE] and has_fired==0:
            self.fire()
            has_fired=fire_treshold
        elif has_fired >0:
            has_fired-=1
        else:
            pass    

        self.y += self.dy
        self.y %= window_height-(window_height/15) #Creates a zone free of words on top of the screen

        self.x += self.dx

    # Create and launch ink
    def fire(self):
        global ink_scale
        ink_x = self.x+((window_width/(pen_image.width*16))*pen_image.width*0.9)
        ink_y = self.y
        ink = Ink(x=ink_x, y=ink_y, batch=batch)
        ink.scale = ink_scale
        self.new_objects.append(ink)
        fire_sound[randint(1, 6)].play()

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
        actual_distance = inktilities.distance((self.x, self.y), (obj.x, obj.y))

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, obj):
        if obj.__class__ is not self.__class__:
            self.dead = True

class Ink(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=ink_image, *args, **kwargs)
        self.dx = (window_width/self.width)
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
        actual_distance = inktilities.distance((self.x, self.y), (obj.x, obj.y))

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, obj):
        if obj.__class__ is not self.__class__:
            self.dead = True



mots = ['Alexandrin', 'ballade', 'césure', 'rime', 'poème', 'décasyllabe', 'fables','lyrique','sizain','strophe','tercet','hpetasyllabe']
mots2 = ['arbre', 'soleil', 'monde','banane','table','sac','stylos','coiffeur','lunette','pull','bracelet','montre']
labels = []

# Pen creation
pen = Pen(batch=batch)
pen.scale = window_width/(pen_image.width*16)
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
    inktilities.drawUI(window_height, window_width) #Draws the rest of the UI
    inktilities.drawChargeBar(pen, pen_image, has_fired) #Draws the charge bar

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
    

pyglet.clock.schedule_interval(update, 1/60) # update at 60Hz
pyglet.app.run()