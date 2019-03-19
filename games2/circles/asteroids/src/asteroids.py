import pyglet
from game import resources, load, physicalobject, player

# Set the main game window
game_window = pyglet.window.Window(800, 600)

# Define the main graphics batch
main_batch = pyglet.graphics.Batch()

# Set the main labels that will display at the top of the screen
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Pyglet Asteroids", x=400, y=575, anchor_x='center', batch=main_batch)
player_lives = load.player_lives(3, main_batch)

# Set up the player
player_ship = player.Player(x=400, y=300, batch=main_batch)

# Set up the asteroids
asteroids = load.asteroids(3, player_ship.position, main_batch)

# Create a list of all game objects
game_objects = [player_ship] + asteroids

# Add any specified event handlers to the event handler stack
for obj in game_objects:
    for handler in obj.event_handlers:
        game_window.push_handlers(handler)


def update(dt):
    for i in xrange(len(game_objects)):
        for j in xrange(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    to_add = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        game_objects.remove(to_remove)

    game_objects.extend(to_add)

@game_window.event
def on_draw():
    # Draw all of our batched sprites to the screen
    game_window.clear()
    main_batch.draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
