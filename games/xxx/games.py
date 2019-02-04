"""
File: games.py
Author: Raphael Holzer
Date: 27.01.2019

This module imports 6 SenseHAT game modules :
- morpion
- game2048
- mines
- tetris
- connect4
- labyrinth
"""

from sense_hat import SenseHat
from gamelib import *
import morpion
import game2048
import mines
import tetris
import connect4
import labyrinth


def main():
    """Present a question mark (?) and allow to choose a game.
    The left/right button increments/decrements the index number.
    The up button displays the game name.
    The middle button starts the selected game.
    """
    
    active = True
    sense = SenseHat()
    
    games = ['morption', '2048', 'mines', 'connect4', 'tetris', 'labyrinth']
    functions = [morpion.main, game2048.main, mines.main, connect4.main,
                 tetris.main, labyrinth.main]
    i = 0
    n = len(games)
    
    sense.show_message('games', text_colour=BLUE)
    sense.show_letter('?')

    while active:
        event = sense.stick.wait_for_event()
        if event.action == 'pressed':
            if event.direction == 'right':
                i = (i+1) % n
            elif event.direction == 'left':
                i = (i-1) % n
            elif event.direction == 'up':
                sense.show_message(games[i], text_colour=GREEN)
                
            elif event.direction == 'middle':
                functions[i]()
        
        sense.stick.get_events()        
        sense.show_letter(str(i), text_colour=RED)


# Execute the main() function when the file is executed,
# but do not execute when the module is imported as a module.
print('module name =', __name__)

if __name__ == '__main__':
    main()  