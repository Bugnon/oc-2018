import pyglet
from levels import levels

height = 500
width = 500
pattern_size = min(height, width)

new_word = ""
M_NUL = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
ML = (levels.L1)
#print(levels.L1)

window = pyglet.window.Window(height, width)

@window.event
def on_draw():
    global ML
    window.clear()
    for u in range(4):
        for n in range(4):
            letter = "images/" + ML[3-n][u] + ".png"
            letter_print = pyglet.image.load(letter)
            letter_print.blit(x= pattern_size/4 * u, y=pattern_size/4 * n, height=pattern_size/4, width=pattern_size/4)

@window.event  
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global new_word
    global M_NUL
    old_case = [-1, -1]
    if buttons & pyglet.window.mouse.LEFT:
#        print(x, y, dx, dy, buttons, modifiers)
        for k in range(4):
            for i in range(4):
                if pattern_size/4 * k < y < ((k+1) * pattern_size/4 ) and  pattern_size/4 * i < x < ((i+1) * pattern_size/4) and M_NUL[3-k][i] == 0:
                    if old_case == [-1, -1] or ((k == old_case[0]+1 or k == old_case[0]-1) and (i == old_case[1]+1 or i == old_case[1]-1)): 
#                        print(ML[3-k][i])
                        M_NUL[3-k][i] = 1
                        new_word += (ML[3-k][i])
                        old_case = [k, i]
                        print(old_case)
                        print(new_word)



pyglet.app.run()
