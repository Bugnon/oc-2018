import math, pyglet, inktilities
from pyglet.window import key, mouse

###### RESSOURCES ######

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

pen_image = pyglet.resource.image('pen.png')
ink_image = pyglet.resource.image('ink.png')
splatter_image = pyglet.resource.image('splatter.png')

###### MISC ######

# Get screen size
window_width = inktilities.screenInfo("x")
window_height = inktilities.screenInfo("y")

###### ENTITIES ######

class Pen(pyglet.sprite.Sprite):
    
    pen_image.anchor_x = pen_image.width / 2
    pen_image.anchor_y = pen_image.height / 2

    fire_treshold = 60
    has_fired = 0

    def __init__(self, *arg, **kwargs):
        super().__init__(img=pen_image, *arg, **kwargs)
        self.x = window_width / 4
        self.y = window_height / 2
        self.scale = window_width / (self.image.width * 16)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        self.react_to_ink = False
        self.is_ink = False
        self.dead = False

        self.touchtime = 0
        self.limits = [window_width / 5, window_width / 2]
        
        self.new_objects = []


    def update(self, keys):
        if keys[key.UP] and not keys[pyglet.window.key.DOWN]:
            self.dy = 7
            if self.y >= window_height - window_height / 15 - self.height:
                self.y = window_height - window_height / 15 - self.height 
        elif keys[key.DOWN] and not keys[key.UP]:
            self.dy = -7
            if self.y <= self.height:
                self.y = self.height
        else:
            self.dy = 0

        if keys[key.RIGHT] and not keys[key.LEFT]:
            self.dx = 5
            if self.x >= self.limits[1]:
                self.x = self.limits[1]
        elif keys[key.LEFT] and not keys[key.RIGHT]:
            self.dx = -5
            if self.x <= self.limits[0]:
                self.x = self.limits[0]
        else:
            self.dx = 0 

        self.y += self.dy
        self.x += self.dx
        if Pen.has_fired > 0:
            Pen.has_fired -= 1

    def keypress(self, pressed_key):
        if pressed_key == pyglet.window.key.SPACE and Pen.has_fired==0:
            self.fire()
            Pen.has_fired = Pen.fire_treshold
            print('fired')
        else:
            pass   

    # Create and launch ink
    def fire(self):
        pass
        '''
        ink_x = self.x + self.width / 2
        ink_y = self.y
        ink = Ink(x = ink_x, y = ink_y, batch = batch)
        ink.scale = Ink.ink_scale
        self.new_objects.append(ink)
        fire_sound[randint(1, 6)].play()
        '''


class FloatingLabel(pyglet.text.Label):

    # constructor function calling
    def __init__(self, *arg, **kwargs):
        # calling parent constructor function
        super().__init__(*arg, **kwargs)
        self.x = randint(int(2/3*window_width),window_width)
        self.y = randint(0,window_height/2)
        self.dead = False

        self.dx = randint(-2, -1)
        self.dy = randint(-2, 2)

        self.react_to_ink = True
        self.is_ink = False

        self.new_objects = []

        self.kind = bool

    def update(self, dt):
        w, h = window.width, window.height
        self.x += self.dx
        self.y += self.dy
        self.x %= w
        if self.y >= h - (h / 15) or self.y < 0:
            self.dy = -self.dy

class Ink(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=ink_image, *args, **kwargs)
        # Ink speed is proportional to the window's width and itselfs, and is affected by the pen's current speed
        self.dx = (2*window_width / self.width + pen.dx / 3)

        # Kills the ink blob after it has had the time to travel through the map
        pyglet.clock.schedule_once(self.die, window_width/(9/10*self.dx*60))
        self.is_ink = True
        
        # Collision attributes
        self.react_to_ink = True
        self.is_ink = True
        self.dead = False

        self.new_objects = []


    def update(self, dt):
        self.x += self.dx

    # Marks the ink blob as dead
    def die(self, dt):
        self.dead = True

    def splatter(self):
        global ink_scale
        splatter_x = self.x
        splatter_y = self.y
        splatter = Splatter(x=splatter_x, y=splatter_y, batch=batch)
        splatter.scale = 0.1
        splatter.rotation = randint(1, 360)
        self.new_objects.append(splatter)
        splatter_sound[randint(1, 6)].play()

class Splatter(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=splatter_image, *args, **kwargs)
        self.dx = 0.001
        # Kills the ink blob after it has had the time to travel through the map
        pyglet.clock.schedule_once(self.die, 2)
        self.is_ink = True
        
        # Collision attributes
        self.react_to_ink = False
        self.is_ink = True
        self.dead = False

        self.new_objects = []


    def update(self, dt):
        self.scale = abs(self.scale - self.dx)

    # Marks the ink blob as dead
    def die(self, dt):
        self.dead = True