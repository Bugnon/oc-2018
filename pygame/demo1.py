import pygame
pygame.init()

size = width, height = 640, 240
speed = [2, 2]
green = (0, 255, 0)

screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'q':
                running = False

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(green)
    screen.blit(ball, ballrect)
    pygame.display.flip()