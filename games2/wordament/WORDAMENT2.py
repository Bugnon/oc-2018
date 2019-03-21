import pyglet

height = 300
width = 700
pattern_size = min(height, width)

window = pyglet.window.Window(height, width)

@window.event
def on_mouse_press(x, y, button, modifiers):
    global M
    if button == pyglet.window.mouse.LEFT:
        for k in range(4):
            for i in range(4):
                if pattern_size/4 * k < y < ((k+1) * pattern_size/4 ) and  pattern_size/4 * i < x < ((i+1) * pattern_size/4):
                    
                    M[i][3-k] += 1
                    print(M, end = '\n\n')
                    M = [
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]
                        ]
                    break
@window.event
def on_draw():
    window.clear()
    for u in range(4):
        for n in range(4):
            N_letter = pyglet.image.load('n.png')                    
            N_letter.blit(x= pattern_size/4 * u, y=pattern_size/4 * n, height=pattern_size/4, width=pattern_size/4)

M = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]


pyglet.app.run()