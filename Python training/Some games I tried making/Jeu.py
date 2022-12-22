import sys, pygame
from random import randint
pygame.init()

size = width, height = 1000, 1000
speed = [10, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("C:/Users/PC1/Desktop/Nouveau dossier (2)/FIFE/Yikes.png")
ballrect = ball.get_rect()

while 1:
    r = randint(0, 100)
    if r == 0:
        clr = (255, 255, 255)
    else:
        clr = black
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(clr)
    screen.blit(ball, ballrect)
    pygame.display.flip()