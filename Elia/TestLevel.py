import pygame, PlatformsFiles.PlatformsClass, PlayerFiles.PlayerMovement

import pygame
import PlayerFiles.PlayerMovement as Player
import PlatformsFiles.PlatformsClass as Platforms
import PropsFile as Prop

pygame.init()

backGround = pygame.image.load("Elia\Asset\BackGround.png")

screen_width = 1920
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

running = True

player = Player.Player(10,950,50,50)
ground  = pygame.Rect(0,400,500,100)


allPlateforms=[]



SquareHouseBottom = pygame.image.load("Elia/Asset/Blocking Maison/Maison_Mur_Bas.png").convert_alpha()
SquareHouseMid = pygame.image.load("Elia/Asset/Blocking Maison/Maison_Mur_Bas_Fenetre.png").convert_alpha()
SquareHouseTop = pygame.image.load("Elia/Asset/Blocking Maison/Toit_Rond.png").convert_alpha()
SquareHouseRebord = pygame.image.load("Elia/Asset/Blocking Maison/Maison_Rebord.png").convert_alpha()

House2StagesBarrer = pygame.image.load("Elia/Asset/Maison 2 étages couleur/Maison_2étages_barrière.png").convert_alpha()
House2StagesRebord = pygame.image.load("Elia/Asset/Maison 2 étages couleur/Maison_2étages_accroche.png").convert_alpha()
House2StagesYel = pygame.image.load("Elia/Asset/Maison 2 étages couleur/Maison_2étages_coloré_final.png").convert_alpha()

MushHouse = pygame.image.load("Elia/Asset/Maison Champignon/Maison_champignon_final.png").convert_alpha()
MushHouseRebord = pygame.image.load("Elia/Asset/Maison Champignon/Maison_champignon_accroche.png").convert_alpha()

Wall = pygame.image.load("Elia/Asset/Maison et Mur non interractif/Mur.png").convert_alpha()
WallWin = pygame.image.load("Elia/Asset/Maison et Mur non interractif/Mur fenetre cercle.png").convert_alpha()
HouseBG = pygame.image.load("Elia/Asset/Maison et Mur non interractif/Maison Ronde sable.png").convert_alpha()

Tower = pygame.image.load("Elia/Asset/Maison Tour 2 étages/Maison_Tour_final.png").convert_alpha()
TowerRebord = pygame.image.load("Elia/Asset/Maison Tour 2 étages/Maison_Tour_rebord.png").convert_alpha()
TowerBarriere = pygame.image.load("Elia/Asset/Maison Tour 2 étages/Maison_Tour_barriere.png").convert_alpha()

Pillar = pygame.image.load("Elia/Asset/Pillier/Pillier.png").convert_alpha()

Temple = pygame.image.load("Elia/Asset/Temple/Temple_final.png").convert_alpha()
TempleGround = pygame.image.load("Elia/Asset/Temple/Temple_final_Sol.png").convert_alpha()

Ground = pygame.image.load("Elia/Asset/Tiles/Bloc simple.png").convert_alpha()
GroundL = pygame.image.load("Elia/Asset/Tiles/Bloc bordure droite.png").convert_alpha()
GroundR = pygame.image.load("Elia/Asset/Tiles/Bloc bordure gauche.png").convert_alpha()
GroundLPente = pygame.image.load("Elia/Asset/Tiles/Bloc pente gauche.png").convert_alpha()
GroundRPente = pygame.image.load("Elia/Asset/Tiles/Bloc pente droite.png").convert_alpha()


PGround = Platforms.Plateform(0, 950, screen_width, 50, "green",False)
PGround.CreatePlateform(allPlateforms)

PMush = Platforms.Plateform(400,781,200,10,"green", True)
PMush.CreatePlateform(allPlateforms)

PSquareHouseB = Platforms.Plateform(1700, 850, 200, 10, "green",False)
PSquareHouseB.CreatePlateform(allPlateforms)
PSquareHouseT = Platforms.Plateform(1700, 750, 200, 10, "green",False)
PSquareHouseT.CreatePlateform(allPlateforms)

PTowerB = Platforms.Plateform(750, 800, 250,10, "green", False)
PTowerB.CreatePlateform(allPlateforms)
PTowerT = Platforms.Plateform(772, 638, 200,15, "green", False)
PTowerT.CreatePlateform(allPlateforms)

PGroundTop = Platforms.Plateform(0, 500, 490, 50, "red", False)
PGroundTop.CreatePlateform(allPlateforms)



allProps = []

square = Prop.Props(True,False,50,350,40,40,True,1,None)
allProps.append(square)


def DisplayImagesBG(Surface): 
    BlocGround = pygame.transform.scale(Ground,(120,120))
    for i in range(28):
        Surface.blit(BlocGround,(-23 + (i*70),920))
    for i in range(7): 
        Surface.blit(BlocGround,(-23+(i*70),470))
    BlocHouseBG = pygame.transform.scale(HouseBG, (200,200))
    Surface.blit(BlocHouseBG,(30, 750))
    BlocMushHouse = pygame.transform.scale(MushHouse, (200,300))
    Surface.blit(BlocMushHouse,(400,650))
    BlocMushHouseRebord = pygame.transform.scale(MushHouseRebord, (200,10))
    Surface.blit(BlocMushHouseRebord, (400,780))

    BlocSquareHouseBottom = pygame.transform.scale(SquareHouseBottom, (200,100))
    Surface.blit(BlocSquareHouseBottom, (1700,850))
    BlocSquareHouseMid = pygame.transform.scale(SquareHouseMid, (200,100))
    Surface.blit(BlocSquareHouseMid, (1700,750))
    BlocSquareHouseTop = pygame.transform.scale(SquareHouseTop, (200,200))
    Surface.blit(BlocSquareHouseTop, (1700,645))

    BlocTower = pygame.transform.scale(Tower, (250,600))
    Surface.blit(BlocTower,(750,350))

    BlocHouse2StagesYel = pygame.transform.scale(House2StagesYel, (200,300))
    Surface.blit(BlocHouse2StagesYel, (10,200))




def DisplayImagesFront(Surface):
    BlocTowerBarriere =pygame.transform.scale(TowerBarriere, (250,600))
    Surface.blit(BlocTowerBarriere, (750,350))
    BlocHouse2StagesBarriere = pygame.transform.scale(House2StagesBarrer, (200,50))
    Surface.blit(BlocHouse2StagesBarriere,(10,343) )



player.jumpForce += 5

def DisplayTemple(Surface): 
    BlocTemple = pygame.transform.scale(Temple, (750,550))
    Surface.blit(BlocTemple, (1100,80))
    BlocPillar = pygame.transform.scale(Pillar, (210,400))
    Surface.blit(BlocPillar, (50,800))
    Surface.blit(BlocPillar, (450,700))
    Surface.blit(BlocPillar, (850,600))


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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            player.Attack() 
            player.LooseOrWinHP(-1)


    player.Movement()

     
    for i in allPlateforms: 

        if(i.CheckCollision(player.playerRect)):
            player.PlayerOnGround(i.Rect.top) 
        if i.solidity: 
            if i.CheckWalls(player) :
                player.PlayerOnGround(i.Rect.top)  

    for j in allProps: 
        j.CheckFalling()
        j.Collider(player)

    for j in allProps: 
        j.onGround = False
        for i in allPlateforms:
            if i.CheckCollision(j.Rect) : 
                oncollide = True
                j.onGround = True
                j.posY = i.posY - j.height
            if i.solidity:
                if i.CheckWalls(j): 
                    j.onGround = True
                    j.posY = i.posY - j.height


    if player.posY + player.height >= screen_height :
        player.posX = 300
        player.posY = 200


    # Affichage
    screen.blit(backGround, (0,0))
    DisplayImagesBG(screen)
    player.DisplayPlayer(screen)
    DisplayImagesFront(screen)


    for i in allProps: 
        i.DisplayProp(screen)

    # UI 
    count = 0

    for i in player.listHP: 
        screen.blit(i, (screen_width - 70 - (count*60), 20))
        count +=1
    screen.blit(player.dashImages[player.dashState], (screen_width - 240 , 100 ))
    
    pygame.display.update()

pygame.quit() 


