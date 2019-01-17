from sense_hat import SenseHat
from time import sleep, time
from random import randint, choice

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
white = (255, 255, 255)
black = (0, 0, 0)

color=(white, orange, yellow, cyan, magenta, blue, green, red)

sense=SenseHat()


##formes=(O, L, T, I, J, S, Z)

sense.clear(black)

L=[[0, 1, 0], [0, 1, 0], [0, 1, 1]]

def matrix_print(M):
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                sense.set_pixel(x, y, red)
    print(M)




def rotate_square_matrix_right_90(matrix):
    n = len(matrix)
    for layer in range((n + 1) // 2):
        for index in range(layer, n - 1 - layer, 1):
            matrix[layer][index], matrix[n - 1 - index][layer], \
                matrix[index][n - 1 - layer], matrix[n - 1 - layer][n - 1 - index] = \
                matrix[n - 1 - index][layer], matrix[n - 1 - layer][n - 1 - index], \
                matrix[layer][index], matrix[index][n - 1 - layer]
    return matrix
