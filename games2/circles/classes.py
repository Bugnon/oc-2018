##### IMPORT #####
import pyglet, random, math, time
from pyglet.window import key, FPSDisplay

##### MEDIA #####
fire = pyglet.media.load('resources/sound/fire.wav', streaming=False)
fire_sound = pyglet.media.Player()
fire_sound.volume = 0.001

##### SCREEN INFORMATION #####
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()

##### USEFUL SIMPLE FUNCTIONS #####
def center_image(image):
    """
    Sets an image's anchor point to its center
    :param image: image
    :return: None
    """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def distance(point_1=(0, 0), point_2=(0, 0)):
    '''
    Calculates the distance between two points.
    :param point_1: tuple
    :param point_2: tuple
    :return: float
    '''
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2)

##### GAME WINDOW CLASS #####
# Create a class for the game_window
class Window(pyglet.window.Window):
    """Class which defines the fullscreen game window at 60 Hz."""
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.set_fullscreen(True)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)

##### PLAYER CLASS #####
class Player(pyglet.sprite.Sprite):
    """Class which defines the player which be controlled with left and right arrows."""
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

        self.image = pyglet.resource.image('resources/sprites/player.png')
        self.rotate_speed = 200
        self.keys = {'left':False, 'right':False, 'space':False} # keys used to controll the player
        self.timer = 0 #the timer is an attribute to helps the feather to know the angular position of the player
        self.angle = 0 # angle of the player at the beginning of the game
        self.scale = 0.56*screen.width/1200 # scale of the inkwell in function of the size of the window
        self.reloading = 0 # default value of reloading

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.SPACE:
            self.keys['space'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.SPACE:
            self.keys['space'] = False

    def fire(self):
        self.angle = self.timer * self.rotate_speed # angle at which the feather appears in function of the angle of the player

        feather = Feather(player=self, img=Feather.feather, x=self.x, y=self.y)

        fire_sound.queue(fire) # fire sound when a feather is shot
        fire_sound.play()

        self.reloading = 30 # = 0,5 sec because it decreases by 1 every 1/60 of a second

    def update(self, dt):
        if self.keys['left']: # turn the inkwell to the left when left key is pressed
            self.rotation -= self.rotate_speed * dt
            self.timer -= 1 * dt
        elif self.keys['right']: # turn the inkwell to the right when right key is pressed
            self.rotation += self.rotate_speed * dt
            self.timer += 1 * dt
        
        if self.keys['space'] and self.reloading == 0: # fire a feather when space is pressed
            self.fire()
        
        if self.reloading > 0: # set reloading back to 0 after a shot
            self.reloading -= 1

##### PROJECTILE CLASS #####
class Feather(pyglet.sprite.Sprite):
    """Class which defines the projectiles thrown by the player with the space bar."""

    #Create the projectile (feathers)
    feather = pyglet.resource.image('resources/sprites/feather.png')
    center_image(feather)
    speed = 500 # Norm of the velocity
    feathers = [] #list of all the feathers thrown

    def __init__(self, player, *args, **kwargs):
        super(Feather, self).__init__(*args, **kwargs)

        Feather.feathers.append(self)

        self.x = player.x + player.width * math.sin(math.radians(player.angle)) # position of the feather on X axis in function of angle
        self.y = player.y + player.height * math.cos(math.radians(player.angle)) # position of the feather on Y axis in function of angle
        self.rotation = player.angle
        

        self.image = Feather.feather
        self.xc = player.x
        self.yc = player.y
        self.r = screen.width // 6

        self.scale = 0.02*screen.width/1200 #scale of a feather in function of the screen size

        self.angle = player.angle # angle of the feather same as the angle of the inkwell

        self.dx = math.sin(math.radians(player.angle)) * Feather.speed # speed of the feather on X axis
        self.dy = math.cos(math.radians(player.angle)) * Feather.speed # speed of the feather on X axis

        self.dead = False

    def update_position(self, dt):
        if self.dead:
            self.die()
        self.x += self.dx * dt
        self.y += self.dy * dt

    def die(self):
        Feather.feathers.remove(self)
        self = RotatingSprite(angle_radians=math.radians(self.angle),
                            r=self.r - self.height, xc=self.xc, yc=self.yc,
                            word=None, img=self.image)
        RotatingSprite.intert_objects.append(self)

##### POETRY #####
class Poetry():
    """Class which allows to read, cut, choose and use verses and words of a poetry."""
    towards = [] # list with the verses
    words = [] # list with the words to shoot
    towards_splited = poetry.read().split('\n') # each toward is a line of the document

    def __init__(self, poetry):
        self.poetry = Poetry.towards_splited
        self.towards = Poetry.towards
        self.words = Poetry.words

    def split_poetry(self):
        '''
        Split the poetry into a list of towards (vers)
        :return: list
        '''
        for line in self.poetry: #loop splitting each toward
            words_splited = line.split(' ')
            self.towards.append(words_splited)
        return self.towards

    def choose_words(self):
        '''
        Choose randomly a word in each toward of the poetry
        :return: list
        '''
        self.towards = self.split_poetry()
        i = 0
        for __ in self.towards: 
            while i < 15:
                random_choice = random.choice(self.towards[i]) # choose 15 words, each toward give a word
                if len(random_choice) > 2: # choose words with a len bigger than 2
                    i += 1
                    self.words.append(random_choice)
        return self.words

    def save_words(self):
        '''
        Save the 15 words chosen in choose_words in a created file called <words.txt>
        :return: None
        '''
        with open('resources/documents/words.txt', 'w', encoding='utf8') as filehandle: # save the words in a txt document
            for listitem in self.choose_words():
                filehandle.write('%s\n' % listitem)

    def open_words(self):
        '''
        Open the file with the words in it
        :return: list
        '''
        return open("resources/documents/words.txt", encoding='utf8').read().split('\n') # open the file containing the words

    def remove_words(self):
        '''
        Remove the word chosen in the toward.
        :return: list
        '''
        i = 0
        words_to_remove = self.open_words()
        towards = self.towards
        for toward in towards:
            loc = towards[i].index(words_to_remove[i]) # find de location of the word
            towards[i].remove(words_to_remove[i]) # remove de word
            towards[i].insert(loc, '........') # insert "........." in the same location
            i += 1 
        return towards

    def initialize(self):
        '''
        Initialize the poetry splitting.
        :return: None
        '''
        self.remove_words()

Poetry(poetry).save_words()

##### ROTATINGSPRITE CLASS #####
class RotatingSprite(pyglet.sprite.Sprite):
    """Class which defines the circle's segments (dead or alive), the dead feathers and the turning words."""

    #Set the class attributes
    segments = [] # list of living segments
    dead_segments = [] # list of all segments when they are shot
    intert_objects = [] #a list of the dead feather

    words = Poetry(poetry).open_words() #a list of the words of the poetry
    words.pop() # delete the last empty line
    angular_velocity = math.pi/5

    circle_segment = pyglet.image.load("resources/sprites/circle_segment.png")
    center_image(circle_segment)
    dead_segment = pyglet.image.load('resources/sprites/circle_segment_grey.png')
    center_image(dead_segment)

    def __init__(self, angle_radians, r, xc, yc, word, *args, **kwargs):
        super(RotatingSprite, self).__init__(*args, **kwargs)
        #Set the instance attributes
        self.word = word #the word assigns to self
        self.dead_word = None

        self.angle = angle_radians
        self.xc = xc
        self.yc = yc
        self.r = r
        if self.word != None: #If the sprite is a segment or an intert object (dead feather)
            self.scale = screen.width/3240
        else:
            self.scale = 2*screen.width/120000

        self.dead = False

        if self.word != None: #assign a word as a label to the sprite if it's a segment
            self.label = pyglet.text.Label(self.word.upper(),
                    font_name='Times New Roman',
                    font_size=self.r/30,
                    color=(75, 0, 130, 255),
                    x=self.x, y=self.y,
                    anchor_x='center', anchor_y='center')

    def update_position(self):
        #Set the self label onto the self segment
        self.x = self.xc + self.r * math.sin(self.angle)
        self.y = self.yc + self.r * math.cos(self.angle)
        self.rotation = math.degrees(self.angle)
        if self.word != None: #update the label
            self.label.begin_update()
            self.label.x = self.x 
            self.label.y = self.y
            self.label.end_update()

    def relive(self):
        self.image = RotatingSprite.circle_segment
        RotatingSprite.words.append(self.word) # add removed word back to the list words
        RotatingSprite.segments.append(self) # add removed segment back to the living segment list

    def update(self, dt):
        if self.dead:
            RotatingSprite.segments.remove(self) # remove the dead segment fron the living segment list
            RotatingSprite.words.remove(self.word) #destroy the word assigns to the dead segment
            RotatingSprite.dead_segments.append(self) # add the dead segment to the dead_segment list
            self.image = RotatingSprite.dead_segment #replace the image by a dead segment image
            self.dead = False #Stay as a RotatingSprite to update itself
        else:
            self.angle += RotatingSprite.angular_velocity * dt
            self.update_position()
