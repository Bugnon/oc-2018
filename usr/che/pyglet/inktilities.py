import math, pyglet

touchtime = 0

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

'''Draws an animated line when the pen hits the left or right borders of where it is allowed to move'''
def drawLimitLine(window_height, pen, pen_limits):
    global touchtime
    distance_to_top = window_height - (window_height / 20) - pen.y
    if pen.dead is False:
        if pen.x >= pen_limits[1]:
            if touchtime < 3:
                touchtime += 0.2
            else:
                touchtime = 3

            if distance_to_top > pen.height * 3:
                pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line to show the pen has hit the limit
                    ("v2f", (pen.x + pen.width / 1.75, pen.y - (touchtime * pen.height), pen.x + pen.width / 1.75, pen.y + (touchtime * pen.height)))
                )
            else:
                pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line to show the pen has hit the limit
                    ("v2f", (pen.x + pen.width / 1.75, pen.y - (touchtime * pen.height), pen.x + pen.width / 1.75, pen.y + (distance_to_top / 3) * touchtime))
                )
        elif pen.x <= pen_limits[0]:
            if touchtime < 3:
                touchtime += 0.2
            else:
                touchtime = 3

            if distance_to_top > pen.height * 3:
                pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line to show the pen has hit the limit
                    ("v2f", (pen.x - pen.width / 1.75, pen.y - (touchtime * pen.height), pen.x - pen.width / 1.75, pen.y + (touchtime * pen.height)))
                )
            else:
                pyglet.graphics.draw(2, pyglet.gl.GL_LINES, #draws a line to show the pen has hit the limit
                    ("v2f", (pen.x - pen.width / 1.75, pen.y - (touchtime * pen.height), pen.x - pen.width / 1.75, pen.y + (distance_to_top / 3) * touchtime))
                )
                
        else:
            if touchtime > 0:
                touchtime -= 0.2
            else:
                pass
