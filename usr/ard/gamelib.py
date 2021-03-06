"""
gamelib is a SenseHAT game library module which provides
- color constants
- a function to display a color matrix
"""

from sense_hat import SenseHat

BLACK = (0, 0, 0)
LEMON = (255, 255, 128)
PINK = (255, 0, 128)
RED = (255, 0, 0)
MINT = (128, 255, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
GRAY = (90,94,107)
CORAIL = (231, 62, 1)
BORDEAU = (91, 60, 19)
LIME = (220, 255, 0)
WHITE = (255, 255, 255)


def main():
    """Test function to display all available colors."""
    sense = SenseHat()
    colors = (BLACK, LEMON, PINK, RED, MINT, BLUE, GREEN, MAGENTA, CYAN, YELLOW,
              ORANGE, GRAY, CORAIL, BORDEAU, LIME, WHITE)
    n = len(colors)
    print(n, 'colors')
    for x in range(8):
        for y in range(8):
            (r, g, b) = colors[(y*8 + x) % n]
            sense.set_pixel(x, y, r, g, b)


# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    main()