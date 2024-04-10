import pygame
from pygame import mixer
import PlayerMovement as Player
import PlatformsClass as Platforms
import BotInfo as Bot
import Collision

pygame.mixer.pre_init(44100, -16 , 2 , 512)
mixer.init
pygame.init()

# Load Sound 
OST = pygame.mixer.Sound('Sound/Music/a_travers_la_Grece.mp3')
OST.set_volume(0.5)
OST.play()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

running = True

player = Player.Player(300,200,50,50)
ground  = pygame.Rect(0,400,500,100)
bot = Bot.Bot(530,540,40,40)

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

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not player.isJumping:
                player.isJumping = True
                player.verticalVelocity = -player.jumpForce


    # Déstruction d'un bot en sautant dessus
    bot_rect = pygame.Rect(bot.posX,bot.posY,bot.Width,bot.Height)
    player_rect = pygame.Rect(player.posX, player.posY, player.width, player.height)
    col = Collision.collision(player_rect,bot_rect)
    ColWeapon = Collision.collision(player.weaponRect, bot_rect)
    if col == 2:
        bot.Checkpoint1 = False
        bot.Checkpoint2 = False
        bot.Height = 0
        bot.Width = 0
        bot.posX = -11111
        bot.posY = -11111
        player.verticalVelocity = -player.jumpForce
    if ColWeapon == 1 or ColWeapon == 4:
        bot.Checkpoint1 = False
        bot.Checkpoint2 = False
        bot.Height = 0
        bot.Width = 0
        bot.posX = -11111
        bot.posY = -11111
    if col != 0 and col != 2:
        player.height = 0
        player.width = 0 
        player.posX = -11111
        player.posY = -11111

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
  
    player.DisplayPlayer(screen)
    bot.DisplayCheckBot(screen)

    pygame.display.update()

pygame.quit() 


