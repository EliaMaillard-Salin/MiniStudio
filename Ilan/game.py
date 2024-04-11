import pygame
import csv
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
ROWS = 16
TILE_SIZE = SCREEN_HEIGHT // ROWS # Assure-toi que cette valeur correspond à celle utilisée dans l'éditeur
TILE_TYPES = 12

#load images
pine1_img = pygame.image.load('Ilan/asset/Background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('Ilan/asset/Background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('Ilan/asset/Background/mountain.png').convert_alpha()
sky_img = pygame.image.load('Ilan/asset/Background/sky_cloud.png').convert_alpha()

# Store textures in a list
textures = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'Ilan/asset/Blocs/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	textures.append(img)
# print(textures)
print(textures[6])
#############################################################################################
def load_level(level_path):
    with open(level_path, 'r') as file:
        return list(csv.reader(file))

def create_platforms(level_data):
    platforms = []
    for y, row in enumerate(level_data):
        for x, tile_type in enumerate(row):
            if tile_type != -1:  # -1 signifie pas de plateforme
                platforms.append(Platforms.Plateform(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, textures[level_data[y][x]], False))
    return platforms

# Charge le niveau
loading_level_data = load_level("Ilan/Levels/level0_data.csv")
level_data = [[int(x) for x in inner] for inner in loading_level_data] # Convertit les valeurs en entiers
# print(level_data)
platforms = create_platforms(level_data) # Crée les plateformes à partir des données du niveau
# print(platforms)
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
        platform.Display(screen, platform.posX, platform.posY)
    
    
    # Met à jour et dessine le joueur
    player.Movement()
    player.DisplayPlayer(screen)

    # Gestion des collisions
    for platform in platforms:
        if platform.CheckCollision(player.playerRect, player.maxValues): # Vérifie si le joueur est en collision avec une plateforme
            player.PlayerOnGround(platform.Rect.y)  # Ajuste cette méthode si nécessaire

    pygame.display.flip()  # Met à jour l'écran avec tout ce que nous avons dessiné
    clock.tick(60)  # Maintient le jeu à 60 FPS

pygame.quit()
