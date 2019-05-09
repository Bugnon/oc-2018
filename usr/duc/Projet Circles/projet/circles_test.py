import pyglet, random, math
from pyglet import font
from classes_test import Player

#Add a font for the poem on the right of the window
font.add_file('resources/font/Angelface.otf')
Angelface = font.load('Angelface', 14)

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


batch = pyglet.graphics.Batch()
parchment = pyglet.resource.image('resources/sprites/parchment.png')
parchment_scale = parchment.height/parchment.width #Scale of the parchment


# Create a class for the game_window
class Window(pyglet.window.Window):
    """Classe définissant la fenêtre de jeu."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_fullscreen(True)
        self.frame_rate = 1/60.0

        #Create the player sprite
        self.player = Player(x=(self.width-self.height//parchment_scale)/2, y=self.height//2)

    def on_draw(self):
        self.clear()
        self.player.draw()

    def update(self, dt):
        pass




if __name__ == "__main__":

    game_window = Window()
    pyglet.clock.schedule_interval(game_window.update, game_window.frame_rate)
    pyglet.app.run()