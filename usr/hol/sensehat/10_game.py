# File: 10_game.py
# Author: Raphael Holzer
# Date: 07.01.2019

# from <module> import <object>
from sense_hat import SenseHat
from time import sleep

# create a new SenseHat object
sense = SenseHat()
sense.

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)

bat_y = 4

ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_ball():
    ball_position[0] += ball_velocity[0]
    if ball_position[0] in [0, 7]:
        ball_velocity[0] = -ball_velocity[0]

    ball_position[1] += ball_velocity[1]
    if ball_position[1] in [0, 7]:
        ball_velocity[1] = -ball_velocity[1]

    if ball_position[0] == 1 and bat_y-1 <= ball_position[1] <= bat_y+1:
        ball_velocity[0] *= -1
    
    if ball_position[0] == 0:
        sense.show_message('GAME OVER')

    sense.set_pixel(*ball_position, red)

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y-1, white)
    sense.set_pixel(0, bat_y+1, white)


def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1


sense.set_pixel(0, 2, blue)
sense.set_pixel(7, 4, red)

# Main programm -------------------------

while True:
    sense.clear()
    sense.stick.direction_up = move_up
    sense.stick.direction_down = move_down
    draw_bat()
    draw_ball()
    sleep(0.25)

