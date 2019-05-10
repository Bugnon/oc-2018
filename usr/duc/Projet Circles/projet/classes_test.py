import pyglet, random, math, time
from pyglet.window import key

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


class Player(pyglet.sprite.Sprite):
    """Classe définissant le joueur qui sera contrôlé avec les flèches gauche et droite."""
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        
        self.rotate_speed = 200

        self.keys = {'left':False, 'right':False, 'space':False}

        self.timer = 0

        self.angle = 0

        #Create the projectile (feathers)
        self.feathers = []
        self.feather = pyglet.resource.image('resources/sprites/feather.png')
        center_image(self.feather)

        self.reloading = 0


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
        self.angle = self.timer * self.rotate_speed
        feather = Feather(player=self, img=self.feather, x=self.x, y=self.y)
        feather.x = self.x + self.width * math.sin(math.radians(self.angle))
        feather.y = self.y + self.height * math.cos(math.radians(self.angle))
        
        feather.rotation = self.angle

        feather.scale = 0.03
        self.feathers.append(feather)
        self.reloading = 45 # 0,75 sec car il descend de 1 chaque 1/60 sec

    def update(self, dt):
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
            self.timer -= 1 * dt
        elif self.keys['right']:
            self.rotation += self.rotate_speed * dt
            self.timer += 1 * dt
        
        if self.keys['space'] and self.reloading == 0:
            self.fire()
        
        if self.reloading > 0:
            self.reloading -= 1
        
        for feather in self.feathers:
            Feather.update_position(feather, dt)

            platform = pyglet.window.get_platform()
            display = platform.get_default_display()      
            screen = display.get_default_screen()
            screen_width = screen.width
            screen_height = screen.height

            if feather.x <= 0 or feather.x >= screen_width:
                self.feathers.remove(feather)
            elif feather.y <= 0 or feather.y >= screen_height:
                self.feathers.remove(feather)

class Feather(pyglet.sprite.Sprite):
    """Classe définissant les projectiles que le joueur lancera avec la barre espace."""
    def __init__(self, player, *args, **kwargs):
        super(Feather, self).__init__(*args, **kwargs)

        self.speed = 600 # Norm of the velocity$

        self.angle = player.angle

        self.dx = math.sin(math.radians(player.angle)) * self.speed
        self.dy = math.cos(math.radians(player.angle)) * self.speed

    def update_position(self, dt):


        self.x += self.dx * dt
        self.y += self.dy * dt

class RotatingSprite(pyglet.sprite.Sprite):
    """Classe définissant les segments de cercle qui tournent."""
    def __init__(self, angle_radians, x, r, xc, yc, *args, **kwargs):
        super(RotatingSprite, self).__init__(*args, **kwargs)

        self.angular_velocity = math.pi/10
        self.angle = angle_radians
        self.xc = xc
        self.yc = yc
        self.r = r
        self.update_position()

        self.scale = 0.56*x/1200

    def update_position(self):
        self.x = self.xc + self.r * math.sin(self.angle)
        self.y = self.yc + self.r * math.cos(self.angle)
        self.rotation = math.degrees(self.angle)

    def update(self, dt):
        self.angle += self.angular_velocity * dt
        self.update_position()