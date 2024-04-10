import pygame
import PlayerFiles.PlayerMovement as Player
import PlatformsFiles.PlatformsClass as Platforms
import CameraFiles.Camera as Camera
import PropsFiles.Props as Props


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

running = True

player = Player.Player(300,200,50,50)
ground  = pygame.Rect(0,400,500,100)


allPlateforms=[]


P1 = Platforms.Plateform(300, 475, 400, 20, "green",False)
P1.CreatePlateform(allPlateforms)

P2 = Platforms.Plateform(0, 305, 200, 20, "green",False)
P2.CreatePlateform(allPlateforms)

P3 = Platforms.Plateform(600, 450, 200, 20, "green",False)
P3.CreatePlateform(allPlateforms)

P4 = Platforms.Plateform(200, 310, 200, 20, "green",False)
P4.CreatePlateform(allPlateforms)

P5 = Platforms.Plateform(320, 380, 200, 20, "red",True)
P5.CreatePlateform(allPlateforms)


P6 = Platforms.Plateform(600, 330, 200, 20, "red",True)
P6.CreatePlateform(allPlateforms)



backGround = pygame.image.load("Elia\Asset\BackGround.png")


allProps = []


square = Props.Props(True,False,20,150,50,50,True,1,0)
allProps.append(square)

food = Props.Props(False,True,650,300,50,50,False,1,1)
allProps.append(food)

cam = Camera.Camera(screen_width,screen_height,player.playerVelocity)

while running: 

    dt = clock.tick(60)
    dt /= 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not player.isJumping:
                player.isJumping = True
                player.verticalVelocity = -player.jumpForce
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            player.Attack() 
            player.LooseOrWinHP(-1)

    player.Movement(dt)

    cam.CamFollow(player, dt)

    # left, right, top, bottom
    sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    for i in allPlateforms: 

        side, distance = i.GetCollision(player.playerRect)

        if side == 0:
            continue

        side -= 1

        if side == 3 and i.solidity == False:
            continue

        direction = sides[side]
        player.posX += direction[0] * distance
        player.posY += direction[1] * distance

        if side == 2:
            player.PlayerOnGround(i.Rect.top)


    # Affichage

    screen.blit(backGround, (0,0))

    for i in allPlateforms:
        i.Display(screen, [cam.pos_cam_x, cam.pos_cam_y ] )


    player.DisplayPlayer(screen, cam)

    # UI

    count = 0

    for i in player.listHP: 
        screen.blit(i, (screen_width - 70 - (count*60), 20))
        count +=1
    screen.blit(player.dashImages[player.dashState], (screen_width - 240 , 100 ))
    
    pygame.display.update()

pygame.quit() 


