import math, pyglet

def screenInfo(z):
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()      
    screen = display.get_default_screen()
    if z == "x":
        return screen.width
    elif z == "y":
        return screen.height
    return

'''Formula to calculate distance between point A and B. Accepts (A, B)'''
def distance(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

'''Draws the top line'''
def drawUI(window_height, window_width):
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a beautiful line 
        ("v2f", (0, window_height-(window_height/20), window_width, window_height-(window_height/20)))
    )

'''Draws the charge bar on top of the pen'''
def drawChargeBar(pen,pen_image,has_fired):
    if pen.dead is False:
        pen_start = pen.x - pen.width / 2
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line for the fire effect
            ("v2f", (pen_start, pen.y+(pen_image.height*pen.scale)/2, pen_start+2*(pen.width*(has_fired/60)), pen.y+(pen_image.height*pen.scale)/2))
        )
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line for the fire effect
            ("v2f", (pen_start, pen.y+(pen_image.height*pen.scale)/2+1, pen_start+2*(pen.width*(has_fired/60)), pen.y+(pen_image.height*pen.scale)/2+1))
        )
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line for the fire effect
            ("v2f", (pen_start, pen.y+(pen_image.height*pen.scale)/2+2, pen_start+2*(pen.width*(has_fired/60)), pen.y+(pen_image.height*pen.scale)/2+2))
        )
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line for the fire effect
            ("v2f", (pen_start, pen.y+(pen_image.height*pen.scale)/2+3, pen_start+2*(pen.width*(has_fired/60)), pen.y+(pen_image.height*pen.scale)/2+3))
        )