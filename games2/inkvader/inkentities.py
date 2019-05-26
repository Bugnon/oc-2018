import math, pyglet, inktilities
import random
from pyglet.window import key, mouse

###### RESSOURCES ######

pyglet.resource.path = ['./resources/img']
pyglet.resource.reindex()

pen_image = pyglet.resource.image('pen.png')
ink_image = pyglet.resource.image('ink.png')
splatter_image = pyglet.resource.image('splatter.png')

words_1 = [line.rstrip('\n') for line in open('./resources/txt/words_1.txt')]
words_0 = [line.rstrip('\n') for line in open('./resources/txt/words_0.txt')]

###### MISC ######

# Get screen size
window_width = inktilities.screenInfo("x")
window_height = inktilities.screenInfo("y")

###### ENTITIES ######

class Pen(pyglet.sprite.Sprite):
    
    pen_image.anchor_x = pen_image.width / 2
    pen_image.anchor_y = pen_image.height / 2

    spawnink = False
    fire_treshold = 60
    has_fired = 0

    def __init__(self, *arg, **kwargs):
        super().__init__(img=pen_image, *arg, **kwargs)
        self.x = window_width / 4
        self.y = window_height / 2
        self.scale = window_width / (self.image.width * 16)

        self.anchor_x = self.image.width / 2
        self.anchor_y = self.image.height / 2

        self.react_to_ink = False
        self.is_ink = True
        self.dead = False

        self.touchtime = 0
        self.limits = [window_width / 5, window_width / 2]

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
            Pen.has_fired = Pen.fire_treshold
            Pen.spawnink = True
        else:
            pass   

    def fire(self, pen, batch):
        ink_x = pen.x + pen.width / 2
        ink_y = pen.y
        ink = Ink(x = ink_x, y = ink_y, batch = batch)
        ink.dx = (window_width / ink.width) / 10 + pen.dx / 2
        return ink


class FloatingLabel(pyglet.text.Label):
    # constructor function calling

    def __init__(self, *arg, **kwargs):
        # calling parent constructor function
        super().__init__(*arg, **kwargs)
        self.x = window_width
        self.y = random.randint(0, window_height / 2)
        self.anchor_y = 'center'
        self.dead = False

        self.font_size = random.randint(int(window_height/75), int(window_height/25))
        self.dx = random.randint(-2, -1)
        self.dy = random.choice([-2, -1, 1, 2])

        self.react_to_ink = True
        self.is_ink = False

        self.kind = 0
    
    def create_word(word_amount, batch):
        word = FloatingLabel(batch = batch)
        if word_amount[1] < 5:
            print('added false')
            word_amount[1] += 1
            word.kind = False
            word.text = words_0[random.randint(0, len(words_0) - 1)]
        elif word_amount[0] < 5:
            print('added true')
            word_amount[0] += 1
            word.kind = True
            word.text = words_1[random.randint(0, len(words_1) - 1)]

        return word

    def update(self, dt):
        self.x += self.dx
        self.y += self.dy
        self.x %= window_width
        if self.y >= window_height - (window_height / 15) - (self.content_height / 2) or self.y < 0:
            self.dy = -self.dy

class Ink(pyglet.sprite.Sprite):
    ink_image.anchor_x = ink_image.width / 2
    ink_image.anchor_y = ink_image.height / 2
    def __init__(self, *args, **kwargs):
        super().__init__(img=ink_image, *args, **kwargs)
        # Ink speed is proportional to the window's width and itselfs, and is affected by the pen's current speed
        self.dx = 0.1
        self.scale = window_width / (self.image.width * 64)
        self.anchor_x = self.width / 2
        self.anchor_y = self.height / 2

        # Kills the ink blob after it has had the time to travel through the map
        pyglet.clock.schedule_once(self.die, window_width / ( 9 / 10 * self.dx * 60))
        self.is_ink = True
        
        # Collision attributes
        self.react_to_ink = True
        self.is_ink = True
        self.dead = False

    def update(self, dt):
        self.x += self.dx

    # Marks the ink blob as dead
    def die(self, dt):
        self.dead = True

    def splatter(self, batch, kind):
        splatter_x = self.x
        splatter_y = self.y
        splatter = Splatter(x=splatter_x, y=splatter_y, batch=batch)
        splatter.scale = 0.1
        splatter.rotation = random.randint(1, 360)
        color = {0:(255, 127, 127), 1:(127, 255, 127), 2:(255, 255, 255)}
        splatter.color = color[kind]
        return splatter

class Splatter(pyglet.sprite.Sprite):
    splatter_image.anchor_x = splatter_image.width / 2
    splatter_image.anchor_y = splatter_image.height / 2
    def __init__(self, *args, **kwargs):
        super().__init__(img=splatter_image, *args, **kwargs)
        self.dx = 0.001
        self.anchor_x = self.width / 2
        self.anchor_y = self.height / 2
        # Kills the splatter after it has had the time to vanish
        pyglet.clock.schedule_once(self.die, 2)
        self.is_ink = True
        
        # Collision attributes
        self.react_to_ink = False
        self.is_ink = True
        self.dead = False

    def update(self, dt):
        self.scale = abs(self.scale - self.dx)

    # Marks the ink blob as dead
    def die(self, dt):
        self.dead = True