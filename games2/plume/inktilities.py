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

def distance(A, B):
    '''Formula to calculate distance between point A and B. Accepts (A, B)'''
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

def init_ui(window_height, window_width):
    '''Return a vertex_list of the top line at 1/20th of the window's height from the top.'''
    return pyglet.graphics.vertex_list(
        2,
        ('v2f', (0, window_height-(window_height/20), window_width, window_height-(window_height/20))), 
        ('c4B', (255, 255, 255, 255) * 2)
        )

def init_chargebar():
    return pyglet.graphics.vertex_list(
                2, #draws a line for the fire effect
                ("v2f", (1, 0, 0, 1))
            )
def update_chargebar(pen, Pen):
    '''Returns a vertex_list of the charge bar on top of the pen'''
    pen_start = pen.x - pen.width / 2
    return [pen_start, pen.y + pen.height / 2, pen_start + (pen.width * (Pen.has_fired / 60)), pen.y + pen.height / 2]

def init_limit_vertex():
    '''Initialises the limit_vertex vertices'''
    return pyglet.graphics.vertex_list(
        2, #draws a line to show the pen has hit the limit
        ("v2f", (1, 0, 0, 1))
    )

def update_limit_vertex(window_height, pen):
    '''Returns the vertices of an animated line when the pen hits the left or right borders of where it is allowed to move.'''
    distance_to_top = window_height - (window_height / 20) - pen.y
    if pen.x >= pen.limits[1]:
        if pen.touchtime < 3:
            pen.touchtime += 0.2
        else:
            pen.touchtime = 3
        if distance_to_top > pen.height * 3:
            return [pen.x + pen.width / 1.75, pen.y - (pen.touchtime * pen.height), pen.x + pen.width / 1.75, pen.y + (pen.touchtime * pen.height)]
        else:
            return [pen.x + pen.width / 1.75, pen.y - (pen.touchtime * pen.height), pen.x + pen.width / 1.75, pen.y + (distance_to_top / 3) * pen.touchtime]
    elif pen.x <= pen.limits[0]:
        if pen.touchtime < 3:
            pen.touchtime += 0.2
        else:
            pen.touchtime = 3
        if distance_to_top > pen.height * 3:
            return [pen.x - pen.width / 1.75, pen.y - (pen.touchtime * pen.height), pen.x - pen.width / 1.75, pen.y + (pen.touchtime * pen.height)]
        else:
            return [pen.x - pen.width / 1.75, pen.y - (pen.touchtime * pen.height), pen.x - pen.width / 1.75, pen.y + (distance_to_top / 3) * pen.touchtime]
    else:
        if pen.touchtime > 0:
            pen.touchtime -= 0.2
        return [0, 0, 0, 0]