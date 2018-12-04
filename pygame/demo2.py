import pygame
pygame.init()

size = width, height = 640, 240
dict = {'k':BLACK, 'w':WHITE, 'r':RED, 'g':GREEN, 'b':BLUE}

screen = pygame.display.set_mode(size)

color = WHITE
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            c = event.unicode
            if c == 'q':
                running = False
            elif c in dict:
                color = dict[c]

    screen.fill(color)
    pygame.display.flip()