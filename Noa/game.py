import pygame
import json
import PlayerFiles.PlayerMovement as Player
import PlatformsFiles.PlatformsClass as Platforms


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mon Jeu de Plateforme")

# Couleurs
WHITE = (255, 255, 255)
BG_COLOR = (144, 201, 120)

# Paramètres du jeu
TILE_SIZE = 40  # Assure-toi que cette valeur correspond à celle utilisée dans l'éditeur


#############################################################################################
def load_level(level_path='level0_data.csv'):
    with open(level_path, 'r') as file:
        return json.load(file)

def create_platforms(level_data):
    platforms = []
    for y, row in enumerate(level_data):
        for x, tile_type in enumerate(row):
            if tile_type != -1:  # -1 signifie pas de plateforme
                platforms.append(Platforms.Plateform(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, WHITE))
    return platforms

# Charge le niveau
level_data = load_level()
platforms = create_platforms(level_data)
#############################################################################################
# Crée le joueur
player = Player.Player(50, SCREEN_HEIGHT - 130, 50, 50)  # Les valeurs initiales peuvent varier selon ton niveau

# Paramètres de la boucle de jeu
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not player.isJumping:
                player.isJumping = True
                player.verticalVelocity = -player.jumpForce

    screen.fill(BG_COLOR)  # Remplit l'écran avec la couleur de fond

    # Dessine les plateformes
    for platform in platforms:
        platform.Display(screen)

    # Met à jour et dessine le joueur
    player.Movement()
    player.UpdatePlayer(screen)

    # Gestion des collisions
    for platform in platforms:
        if platform.CheckCollision(player.playerRect):
            player.PlayerOnGround(platform.Rect.y)  # Ajuste cette méthode si nécessaire

    pygame.display.flip()  # Met à jour l'écran avec tout ce que nous avons dessiné
    clock.tick(60)  # Maintient le jeu à 60 FPS

pygame.quit()
