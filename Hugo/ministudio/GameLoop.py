import pygame
import PlayerMovement as Player
import PlatformsClass as Platforms


pygame.init()


bot_velocity = 1
checkpoint1 = True
checkpoint2 = False


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
    #on retourne la face
    return index + 1


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

running = True

player = Player.Player(300,540,50,50)
ground  = pygame.Rect(0,400,500,100)
bot = Player.Bot(530,540,40,40)


allPlateforms=[]


P1 = Platforms.Plateform(300, 475, 400, 20, "green",False)
P1.CreatePlateform(allPlateforms)

P2 = Platforms.Plateform(0, 305, 200, 20, "green",False)
P2.CreatePlateform(allPlateforms)

P3 = Platforms.Plateform(600, 400, 200, 20, "green",False)
P3.CreatePlateform(allPlateforms)

P4 = Platforms.Plateform(200, 330, 200, 20, "red",True)
P4.CreatePlateform(allPlateforms)

P5 = Platforms.Plateform(0, 580, 800, 20, "green",False)
P5.CreatePlateform(allPlateforms)   

check = (50,550,20,20)
check1 = (750,550,20,20)

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
        if(i.CheckCollision(player.playerRect)):
            player.PlayerOnGround(i.Rect.top) 
        if i.solidity: 
            if(i.CheckWalls(player)) :
                player.PlayerOnGround(i.Rect.top)


    if player.posY + player.height >= screen_height :
        player.posX = 300
        player.posY = 200

    

    # Déstruction d'un bot en sautant dessus
    bot_rect = pygame.Rect(bot.posX,bot.posX,bot.width,bot.height)
    player_rect = pygame.Rect(player.posX, player.posY, player.width, player.height)
    col = collision(player_rect,bot_rect)
    print(col)
    if col == 2 :
        checkpoint1 = False
        checkpoint2 = False
        bot.height = 0
        bot.width = 0
        bot.posX = -1111111
        bot.posY = -1111111
        player.verticalVelocity = -player.jumpForce - 5
    if col == 1 or col == 4 or col == 3:
        player.height = 0
        player.width = 0
    
    if checkpoint1 == True:
        bot.posX -= bot.botVelocity 
        bot.botDirection = 1
        
                
    if checkpoint2 == True:
        bot.botDirection = 0
        bot.posX += bot.botVelocity                
    
    check_rect = pygame.Rect(check)
    check1_rect = pygame.Rect(check1)
    colcheck = collision(bot_rect,check_rect)
    colcheck1 = collision(bot_rect,check1_rect)
    if colcheck == 4:
        checkpoint1 = False
        checkpoint2 = True
    if colcheck1 == 1:
        checkpoint2 = False
        checkpoint1 = True


    # Affichage
    screen.fill("black")

    for i in allPlateforms:
        i.Display(screen)

    bot.DisplayBot(screen)
    player.DisplayPlayer(screen)
    pygame.draw.rect(screen, (115,0,115), check)
    pygame.draw.rect(screen, (115,115,115), check1)

    pygame.display.update()

pygame.quit() 


