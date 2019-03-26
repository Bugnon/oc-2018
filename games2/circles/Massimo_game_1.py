import pyglet
from pyglet import font
font.add_file('resources/Handwriting.ttf')
Handwriting = font.load('Janda Elegant Handwriting', 14)

# Set up a window
rapportparchemin = 3506/2480
x = 500
y = x*9/16
game_window = pyglet.window.Window(x, y)
image = pyglet.resource.image('resources/parchemin.png')
image.height = y
image.width = y/rapportparchemin


def write_poetry():
    fname = input("Enter file name: ")
    num_lines = 0
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
print("Number of lines:")
print(num_lines)
txt = open("resources/poeme.txt", "r")
poetry = pyglet.text.Label(str(txt.read()),
                          font_name='Janda Elegant Handwriting',
                          font_size=14,
                          x=0, y=-20)
poetry.draw()

@game_window.event
def on_draw():
    game_window.clear()
    image.blit(x-y/rapportparchemin, 0)
    write_poetry()

pyglet.app.run()