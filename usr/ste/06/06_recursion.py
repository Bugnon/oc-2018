#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

green = [225, 225, 225]

sense.show_message("8=D", text_colour=green)