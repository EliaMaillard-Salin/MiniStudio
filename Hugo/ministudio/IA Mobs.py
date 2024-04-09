import pygame
import sys
import PlayerMovement as Player
import PlatformsClass as Platforms



# Initialisation de Pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

player = Player.Player(300,200,50,50)
ground  = pygame.Rect(0,400,500,100)

allPlateforms=[]


P1 = Platforms.Plateform(300, 475, 400, 20, "green",False)
P1.CreatePlateform(allPlateforms)

P2 = Platforms.Plateform(0, 305, 200, 20, "green",False)
P2.CreatePlateform(allPlateforms)

P3 = Platforms.Plateform(600, 400, 200, 20, "green",False)
P3.CreatePlateform(allPlateforms)

P4 = Platforms.Plateform(200, 330, 200, 20, "green",False)
P4.CreatePlateform(allPlateforms)


def collision(rectA: pygame.rect.Rect, rectB: pygame.rect.Rect):
    #0 None
    #1 Left
    #2 Top
    #3 Bottom
    #4 Right

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
            print(index)

    #on retourne la face
    return index + 1



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
        if not player.isJumping:
            player.isJumping = True
            player.verticalVelocity = -player.jumpForce

player.Movement()

     
for i in allPlateforms: 
    if(i.CheckCollision(player.playerRect, player.maxValues)):
        player.PlayerOnGround(i.Rect.top) 

player.CheckWalls()

if player.posY + player.height >= screen_height :
        player.posX = 300
        player.posY = 200

# Déstruction d'un bot en sautant dessus
bot_rect = pygame.Rect(bot_x,bot_y,bot_width,bot_height)
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
col = collision(player_rect,bot_rect)
print(col)
if col == 2 :
    checkpoint1 = False
    checkpoint2 = False
    bot_height = 0
    bot_width = 0
    bot_x = -1111111
    bot_y = -1111111
    pv -= 1
    vertical_velocity = -jump_attack
if col == 1 or col == 4 or col == 3:
    player_height = 0
    player_width = 0
    



       

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



# Affichage
screen.fill("black")

for i in allPlateforms:
        i.Display(screen)

player.UpdatePlayer(screen)
    
pygame.display.update()

pygame.quit()
sys.exit()
