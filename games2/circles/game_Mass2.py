import pyglet, random
import math
from pyglet import font

words = ['arbre','fromage','language','beau','ramage','hôte','voix','bec','flatteur','dépens','leçon','honteux','confus','jura','tard']

poetry = open("resources/poeme.txt")

def write_words():
        i = 0
        for word in words:
                msg = '{}'.format(word)
                label = pyglet.text.Label(msg,
                          font_name='Times New Roman',
                          font_size=15,
                          color=(75, 0, 130, 255),
                          x=segments[i].x, y=segments[i].y,
                          anchor_x='center', anchor_y='center')
                label.text = msg
                i += 1
                label.draw()

def write_poetry():
    saut = 55
    for line in poetry:
        saut = saut+17*x/800
        poeme = pyglet.text.Label(line,
                            font_name='Angelface',
                            font_size=14*x/800,
                            color=(0, 0, 50, 255),
                            x=x-320*x/800, y=y-30*x/800-saut,
                            batch=batch)
        poeme.draw()

write_poetry()

@game_window.event
def on_draw():

    game_window.clear()
    wallpaper_sprite.draw()
    player_ink.draw()
    parchemin_sprite.draw()

    batch.draw()
    write_words()

def update(dt):
    for segment in segments:
        segment.update(dt)
    player_ink.update(dt)


if __name__ == "__main__":

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()