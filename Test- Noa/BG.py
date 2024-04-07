# Background

background_image = "img/ciel.jpg"

import pygame

pygame.init()
screen = pygame.display.set_mode((720, 480))

pygame.display.set_caption("Créer un jeu avec PyGame")
background = pygame.image.load(background_image).convert()

run = True
while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.circle(background, (250, 250, 0), (140, 60), 30)
        screen.blit(background, (0, 0))

        pygame.display.update()

pygame.quit()
quit()