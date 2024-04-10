import pygame
import sys
import BotInfo as Bot
import Collision 
import PlayerMovement as Player

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)  # Couleur des plateformes
red = (255,0,0)
bleu = (0,0,255)
purple = (80,00,80)

# Paramètres du joueur
hp = 1
player_x = 50
player_y = 50
player_width = 50
player_height = 50
player_velocity = 5
dash_velocity = 20
is_jumping = False
is_dashing = False
dash_cooldown = 0
jump_force = 10  # Force du saut simplifiée
jump_attack = 5
gravity = 0.5
vertical_velocity = 0

# Paramètre Bot
bot = Bot.Bot(530,540,40,40)
player = Player.Player(50,50,50,50)

# Plateformes
platforms = [(0, screen_height - 20, screen_width, 20),  # Sol
             (300, 475, 200, 20),
             (50, 400, 200, 20),
             (500, 300, 200, 20),
             (50, 200, 200, 20)]

# Horloge pour contrôler les FPS
clock = pygame.time.Clock()

# Boucle de jeu
running = True
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
        dash_direction = 0
        if keys[pygame.K_q]:
            dash_direction = -1
        elif keys[pygame.K_d]:
            dash_direction = 1
        dash_cooldown = 60

    if is_dashing:
        player_x += dash_direction * dash_velocity
        dash_cooldown -= 1
        gravity = 0
        if dash_cooldown <= 50:
            gravity = 0.5
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


    # Déstruction d'un bot en sautant dessus
    bot_rect = pygame.Rect(bot.posX,bot.posY,bot.Width,bot.Height)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    col = Collision.collision(player_rect,bot_rect)
    if col == 2 :
        bot.Checkpoint1 = False
        bot.Checkpoint2 = False
        bot.Height = 0
        bot.Width = 0
        bot.posX = -11111
        bot.posY = -11111
        vertical_velocity = -jump_attack
    if col != 0 and col != 2:
        player_height = 0
        player_width = 0   


    player.Movement()

    bot.MovementBot()
    bot.CheckCollision()

    # Vérifier la collision avec les plateformes
    for platform in platforms:
        platform_rect = pygame.Rect(platform)
        if player_rect.colliderect(platform_rect) and vertical_velocity > 0:
            player_y = platform_rect.top - player_height
            vertical_velocity = 0
            is_jumping = False  # Réinitialiser l'état de saut à l'atterrissage

    if not is_dashing:
        dash_cooldown -= 1

    # Affichage
    screen.fill(black)
    for platform in platforms:
        pygame.draw.rect(screen, green, platform)

    bot.DisplayBot(screen)
    bot.DisplayCheckBot(screen)

    player.DisplayPlayer(screen)    
    pygame.display.update()

pygame.quit()
sys.exit()