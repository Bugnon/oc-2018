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

I=[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
L=[[1, 0], [1, 1]]
O=[[1, 1], [1, 1]]

shapes = (I, L, O)

P = choice(shapes)



def matrix_print(M):
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                    sense.set_pixel(x, y, red)
    print(M)


def matrix_print_left(M):
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                if 0<x<8:
                    sense.set_pixel(x-1, y, red)
    print(M)


def matrix_print_right(M):
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                if -1<x<7:
                    sense.set_pixel(x+1, y, red)
    print(M)




def rotate_90(matrix): #tourne la matrice carrée de 90 degrés vers la droite
    n = len(matrix)
    for y in range(n):
        for x in range(n):
            if matrix[y][x]==1:
                sense.set_pixel(x, y, black)
    print(matrix)
    for layer in range((n + 1) // 2):
        for index in range(layer, n - 1 - layer, 1):
            matrix[layer][index], matrix[n - 1 - index][layer], \
                matrix[index][n - 1 - layer], matrix[n - 1 - layer][n - 1 - index] = \
                matrix[n - 1 - index][layer], matrix[n - 1 - layer][n - 1 - index], \
                matrix[layer][index], matrix[index][n - 1 - layer]
    for y in range(n):
        for x in range(n):
            if matrix[y][x]==1:
                sense.set_pixel(x, y, red)
    print(matrix)

    return matrix


while True:
    for event in sense.stick.get_events():
         if event.action == 'pressed' and event.direction == 'middle':
            rotate_90(P)
         elif event.direction == 'down' and event.action == 'held':
            print('Descend')
         elif event.direction == 'left' and event.action == 'pressed':
            matrix_print_left(P)
         elif event.direction == 'right' and event.action == 'pressed':
            matrix_print_right(P)
        
