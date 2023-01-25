import sys, pygame
from random import randint
pygame.init()

size = width, height = 1000, 1000
speed = [2, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("pygame_game_funny_cat_photo.png")
ballrect = ball.get_rect()


running = True

while running:
    r = randint(0, 100)
    bckgrnd_colour = black
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)  # conditions pour inverser la vitesse si on atteint le bord :
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bckgrnd_colour)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    
    # Le joueur ferme la fenêtre :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        print(event)
