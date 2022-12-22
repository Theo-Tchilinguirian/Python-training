# imports
import pygame

pygame.init()  # initialisation de pygame (pour charger tous les composants)


# création de la classe qui représente le joueur :

class Player(pygame.sprite.Sprite):  # hérite de la superclasse Sprite; car le joueur est une sprite  (sprite est le module; Sprite la classe)
    def __init__(self):
        super().__init__()  # On initialise, récupère la superclasse d'abord.
        self.max_health = 100
        self.health = 100
        self.attack = 1
        self.velocity = 5  # en pixels


# génération de la fenêtre du jeu :

pygame.display.set_caption("Le Jeu !!!!!!!!!!!!!!!!!!!!!!!!!!!")
screen = pygame.display.set_mode((1080, 720))  # On le récupère: renvoie une surface (ctrl + clic sur la méthode)

# Importer et charger l'arrière plan :
background = pygame.image.load('assets/bg.jpg')

running = True

# Boucle du jeu :
while running:

    # On applique/dessine l'arrière plan du jeu :
    screen.blit(background, (0, -300))  # On injecte l'image aux coordonnées précises
    # On met à jour l'écran :
    pygame.display.flip()

    # Si le joueur ferme la fenêtre :
    for event in pygame.event.get():
        # On vérifie si l'évènement est fermeture de fenêtre:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        print(event)