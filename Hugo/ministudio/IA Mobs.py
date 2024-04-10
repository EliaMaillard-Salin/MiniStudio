import pygame
import sys



# Initialisation de Pygame
pygame.init()


def collision(rectA: pygame.rect.Rect, rectB: pygame.rect.Rect):
    # 0 None
    # 1 Left
    # 2 Top
    # 3 Bottom
    # 4 Right
 
    if rectA.left > rectB.right:
        return 0
    
    if rectA.right < rectB.left:
        return 0

    if rectA.top > rectB.bottom:
        return 0

    if rectA.bottom < rectB.top:
        return 0

    #calculer les 4 distanes, on stockera dans un tableau de 4 cases
    distance = list(range(0))    
    distance.append(rectA.right - rectB.left) #0
    distance.append(rectA.bottom - rectB.top) #1
    distance.append(rectB.bottom - rectA.top) #2
    distance.append(rectB.right - rectA.left) #3
    print(distance)
   
    #on parcourt le tableau, on cherche la distance la plus grande
    smallest = 1000
    for i in range(len(distance)) :
        if distance[i] < smallest :
            smallest = distance[i]
            index = i
    return index + 1  
 
  

    


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

# Paramètre d'un bot
pv = 1
bot_x = 530
bot_y = 540
bot_width = 40
bot_height = 40
bot_velocity = 1
checkpoint1 = True
checkpoint2 = False


# Plateformes
platforms = [(0, screen_height - 20, screen_width, 20),  # Sol
             (300, 475, 200, 20),
             (50, 400, 200, 20),
             (500, 300, 200, 20),
             (50, 200, 200, 20)]

check = [(50,550,20,20)]
check1 = [(750,550,20,20)]



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

    


    if checkpoint1:
        bot_x -= bot_velocity
    if checkpoint2:
        bot_x += bot_velocity
  


    # Appliquer la gravité
    vertical_velocity += gravity
    player_y += vertical_velocity


    # Déstruction d'un bot en sautant dessus
    bot_rect = pygame.Rect(bot_x,bot_y,bot_width,bot_height)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    col = collision(player_rect,bot_rect)
    if col == 2 :
        checkpoint1 = False
        checkpoint2 = False
        bot_height = 0
        bot_width = 0
        bot_x = -1111111
        bot_y = -1111111
        pv -= 1
        vertical_velocity = -jump_attack
    if col != 0 and col != 2:
        player_height = 0
        player_width = 0
        player_x = -11111
        player_y = -11111
   

       
       

    # Vérifier la collision avec le checkpoint 1 pour bot
    for plateforms in check:
        check_rect = pygame.Rect(50,550,20,20)
        if bot_rect.colliderect(check_rect):
            checkpoint1 = False
            checkpoint2 = True


            
    # Vérifier la collision avec le checkpoint 1 pour bot
    for plateforms in check1:
        check_rect = pygame.Rect(750,550,20,20)
        if bot_rect.colliderect(check_rect):
            checkpoint2 = False
            checkpoint1 = True

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
    
    if pv == 1:
        pygame.draw.rect(screen, bleu, (bot_x, bot_y, bot_width, bot_height))

    pygame.draw.rect(screen, black,  plateforms)
    pygame.draw.rect(screen, black,  plateforms)
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    if hp == 1:
            pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))









    pygame.display.update()

pygame.quit()
sys.exit()