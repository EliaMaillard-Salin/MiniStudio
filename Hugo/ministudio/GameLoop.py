import pygame
import PlayerMovement as Player
import PlatformsClass as Platforms
import BotInfo as Bot

pygame.init()


screen_width = 800
screen_height = 600 
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

running = True

player = Player.Player(300,200,50,50)
ground  = pygame.Rect(0,400,500,100)
bot = Bot.Bot(530,540,40,40)
bot.load_anim()
allPlateforms=[]


P1 = Platforms.Plateform(300, 475, 400, 20, "green",False)
P1.CreatePlateform(allPlateforms)

P2 = Platforms.Plateform(0, 305, 200, 20, "green",False)
P2.CreatePlateform(allPlateforms)

P3 = Platforms.Plateform(600, 400, 200, 20, "green",False)
P3.CreatePlateform(allPlateforms)

P4 = Platforms.Plateform(200, 330, 200, 20, "red",True)
P4.CreatePlateform(allPlateforms)

P5 = Platforms.Plateform(0, 580, 800, 20, "red",True)
P5.CreatePlateform(allPlateforms)

while running: 
    start = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not player.isJumping:
                player.isJumping = True
                player.verticalVelocity = -player.jumpForce


    bot.CollisionBot(player)

    player.Movement()

    bot.MovementBot()
    bot.CheckCollision()
     
    for i in allPlateforms: 
        if(i.CheckCollision(player.playerRect)):
            player.PlayerOnGround(i.Rect.top) 
        if i.solidity: 
            if(i.CheckWalls(player)) :
                player.PlayerOnGround(i.Rect.top)


    if player.posY + player.height >= screen_height :
        player.posX = 300
        player.posY = 200


    # Affichage
    screen.fill("black")



    for i in allPlateforms:
        i.Display(screen)

    bot.DisplayBot(screen)
    bot.walking(screen)
  
    player.DisplayPlayer(screen)
    bot.DisplayCheckBot(screen)

    pygame.display.update()
    end = pygame.time.get_ticks() - start 
    bot.botdesign_nb += 1
    if bot.botdesign_nb == 5 :
        bot.botdesign_nb = 0
    print(end)
    clock.tick(60)
pygame.quit() 


