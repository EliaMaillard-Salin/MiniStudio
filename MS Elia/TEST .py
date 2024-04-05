

import pygame

import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

class Plateform: 
    def __init__(self,posX,posY,width,height,color): 
        self.solid = False
        self.Rect = pygame.Rect(posX,posY,width,height)
        self.color = color
        self.Ground = pygame.Rect(posX + 1 , posY - 1, width - 2 , 1)
    def CreatePlateform(self,plateformeList):
        plateformeList.append(self)
    def Display(self,surface): 
        screen.blit(Tower, (0,0))
        pygame.draw.rect(surface,"red",self.Ground)
    def Collision(self, Rect):  
        if (self.Ground.left + self.Ground.width >= Rect.left and
            self.Ground.left <= Rect.left + Rect.width and
            self.Ground.top + self.Ground.height >= Rect.top  and 
            self.Ground.top <= Rect.top + Rect.height): #Collision avec le sol  
            return True
        return False



# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)  # Couleur des plateformes

# Paramètres du joueur
player_x = 50
player_y = 50
player_width = 50
player_height = 50 #

player_velocity = 5 #
dash_velocity = 20
is_jumping = False
is_dashing = False
dash_cooldown = 0
jump_force = 10  # Force du saut simplifiée
gravity = 0.5
vertical_velocity = 0


# Horloge pour contrôler les FPS
clock = pygame.time.Clock()

# Boucle de jeu
running = True

allPlateforms=[]


Spawn = Plateform(0, screen_height - 20, screen_width, 20, "green")
Spawn.CreatePlateform(allPlateforms)

P1 = Plateform(300, 475, 200, 20, "green")
P1.CreatePlateform(allPlateforms)

P2 = Plateform(0, 305, 200, 20, "green")
P2.CreatePlateform(allPlateforms)

P3 = Plateform(500, 350, 200, 20, "green")
P3.CreatePlateform(allPlateforms)




Tower = pygame.image.load("img/Maison_entree.png").convert_alpha()

Tower = pygame.transform.scale(Tower, (200,400))

Barrer = pygame.image.load("img/Maison_entree_barriere.png").convert_alpha()
Barrer = pygame.transform.scale(Barrer,(200,400))


while running:
    clock.tick(60)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not is_jumping:
                is_jumping = True
                vertical_velocity = -jump_force

    keys = pygame.key.get_pressed()

    # Gestion du dash
    if keys[pygame.K_LSHIFT] and not is_dashing and dash_cooldown <= 0:
        is_dashing = True
        dash_cooldown = 60
        dash_direction = 0
        if keys[pygame.K_q]:
            dash_direction = -1
        elif keys[pygame.K_d]:
            dash_direction = 1
        else: 
            is_dashing = False
            dash_cooldown = 0


    if is_dashing:
        player_x += dash_direction * dash_velocity
        dash_cooldown -= 1
        if dash_cooldown <= 50:
            is_dashing = False

    if not is_dashing:
        # Déplacement horizontal
        if keys[pygame.K_q]:
            player_x -= player_velocity
        if keys[pygame.K_d]:
            player_x += player_velocity

    # Appliquer la gravité
    vertical_velocity += gravity
    player_y += vertical_velocity

    # Vérifier la collision avec les plateformes
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for platform in allPlateforms:
        platform_rect = platform.Ground
        if platform.Collision(player_rect) and vertical_velocity > 0:
            player_y = platform_rect.top - player_height
            vertical_velocity = 0
            is_jumping = False  # Réinitialiser l'état de saut à l'atterrissage

    if not is_dashing:
        dash_cooldown -= 1

    # Affichage
    screen.fill(black)

    for i in allPlateforms:
        i.Display(screen)

    screen.blit(Tower, (0,0))
    pygame.draw.rect(screen, "red" , (player_x, player_y, player_width, player_height))

    screen.blit(Barrer,(0,0))
    
    pygame.display.update()

pygame.quit()
sys.exit()
