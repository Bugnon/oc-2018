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

def matrix_print(M):
    n = len(M)
    for y in range(n):
        for x in range(n):
            if M[y][x]==1:
                sense.set_pixel(x, y, red)
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


g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

test_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, b, g, b, g, g,
    b, b, g, b, b, b, b, b,
    b, b, b, g, b, b, b, b,
    b, b, b, b, g, b, b, b,
    b, b, b, b, b, g, b, b,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, b, b, g
]


sense.set_pixels(test_pixels)


#check si une ligne est pleine, la supprime et descend les lignes au-dessus.
l=1
score=0
while l==1:
    for i in range(8):
        a=0
        for j in range(8):
            if sense.get_pixel(7-j, 7-i)!=[0, 0, 0]:
                a+=1
                if a==8:
                    score+=1
                    for k in range(8):
                        sense.set_pixel(k, 7-i, black)
                    for c in reversed(range(7-i)):
                        for d in range(8):
                            sense.set_pixel(d, c+1, (sense.get_pixel(d, c)))
                            sense.set_pixel(d, c, black)


