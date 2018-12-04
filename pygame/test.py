import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("flower.png")
ballrect = ball.get_rect()

screen.fill(black)
screen.blit(ball, ballrect)
pygame.display.flip()