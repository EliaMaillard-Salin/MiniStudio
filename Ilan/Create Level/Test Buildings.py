import pygame
import PlayerFiles.PlayerMovement as Player
import PlatformsFiles.PlatformsClass as Platforms
import CameraFiles.Camera as Camera
import PropsFiles.Props as Props
import csv
import PropsFiles.coinsManager as coinsManager
import PlatformsFiles.Building as Building

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mon Jeu de Plateforme")

# Couleurs
WHITE = (255, 255, 255)
BG_COLOR = (144, 201, 120)

# Paramètres du jeu - Init grid 
ROWS = 16
TILE_SIZE = SCREEN_HEIGHT // ROWS # Assure-toi que cette valeur correspond à celle utilisée dans l'éditeur
TILE_TYPES = 12


############# LEVEL IMPORT ###############

#load images - BackGround Paralaxe - FUCK

'''
pine1_img = pygame.image.load('Ilan/img/Background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('Ilan/img/Background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('Ilan/img/Background/mountain.png').convert_alpha()
sky_img = pygame.image.load('Ilan/img/Background/sky_cloud.png').convert_alpha()

'''

# Store textures in a list - List des Blocs 

textures : list[pygame.Surface] = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'PythonFiles/Assets/PNG/Blocs/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	textures.append(img)


def load_level(level_path):
    with open(level_path, 'r') as file: #recup csv level 
        return list(csv.reader(file))

def create_platforms(level_data : list[list[str]] ) -> list[Platforms.Plateform]:  #Create Plateform par Bloc 
    platforms : list[Platforms.Plateform]= []
    for y, row in enumerate(level_data):
        for x, tile_type in enumerate(row):
            if tile_type != -1:  # -1 signifie pas de plateforme
                platforms.append(Platforms.Plateform(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE,None, textures[level_data[y][x]], False))
    return platforms

# Charge le niveau

loading_level_data = load_level("Ilan/Levels/level_1.csv")

level_data = [[int(x) for x in inner] for inner in loading_level_data] # Convertit les valeurs en entiers

platforms : list[Platforms.Plateform] = create_platforms(level_data) # Crée les plateformes à partir des données du niveau


clock = pygame.time.Clock()

running : bool = True

player  = Player.Player(300,200,54,93)
ground  = pygame.Rect(0,400,500,100)



allplateforms : list[Platforms.Plateform] = []

P6 = Platforms.Plateform(0, SCREEN_HEIGHT - 20, 10000, 20, "red",None,True)
P6.CreatePlateform(allplateforms)


backGround = pygame.image.load("PythonFiles/Assets/PNG/BackGround.png")


allProps : list[Props.Props] = []


square = Props.Props(True,False,20,150,50,50,True,1,0, False)
allProps.append(square)

food = Props.Props(False,True,650,300,50,50,False,1,1, False)
allProps.append(food)

cam = Camera.Camera(SCREEN_WIDTH,SCREEN_HEIGHT,player.playerVelocity)



allBuildings : list[Building.Buildings]= []

allFrontBuildings : list[Building.Buildings] = []

# Index for Buildings : 0 = Maison Carré, 1 = Maison Carré Double, 2 = Maison Carré Haute, 3 = Maison Ronde, 4 = Maison Ronde Fenetre, 5 = Maison 2etage Rouge 
# 6 = Maison 2 etages Jaunes, 7 = Maison Champignon Jaune, 8 = Maison Champignon Rouge, 9 = Tour Jaune,10 = Tour Rouge, 11 = Hutte arriere plan, 12 = tour arrier plan 
# 13 = maison carre arriere plan, 14 = Pillier, 15 = Temple 

House1 = Building.Buildings(50,300,0) ; House1.PlaceBuilding(allplateforms) ; allBuildings.append(House1)
if House1.placeBarrer == True : 
    allFrontBuildings.append(House1) 

House2 = Building.Buildings(250,300,1) ; House2.PlaceBuilding(allplateforms) ; allBuildings.append(House2)
if House2.placeBarrer == True : 
    allFrontBuildings.append(House2) 

House3 = Building.Buildings(450,300,2) ; House3.PlaceBuilding(allplateforms) ; allBuildings.append(House3)
if House3.placeBarrer == True : 
    allFrontBuildings.append(House3) 

House4 = Building.Buildings(650,300,3) ; House4.PlaceBuilding(allplateforms) ; allBuildings.append(House4)
if House4.placeBarrer == True : 
    allFrontBuildings.append(House4) 

House5 = Building.Buildings(850,300,4) ; House5.PlaceBuilding(allplateforms) ; allBuildings.append(House5)
if House5.placeBarrer == True : 
    allFrontBuildings.append(House5) 

House6 = Building.Buildings(1150,300,5) ; House6.PlaceBuilding(allplateforms) ; allBuildings.append(House6)
if House6.placeBarrer == True : 
    allFrontBuildings.append(House6) 


House7 = Building.Buildings(1250,300,6) ; House7.PlaceBuilding(allplateforms) ; allBuildings.append(House7)
if House7.placeBarrer == True : 
    allFrontBuildings.append(House7) 


House8 = Building.Buildings(1450,300,7) ; House8.PlaceBuilding(allplateforms) ; allBuildings.append(House8)
if House8.placeBarrer == True : 
    allFrontBuildings.append(House8) 

House9 = Building.Buildings(1650,300,8) ; House9.PlaceBuilding(allplateforms) ; allBuildings.append(House9)
if House9.placeBarrer == True : 
    allFrontBuildings.append(House9) 

House10 = Building.Buildings(1850,300,9) ; House10.PlaceBuilding(allplateforms) ; allBuildings.append(House10)
if House10.placeBarrer == True : 
    allFrontBuildings.append(House10) 

House11 = Building.Buildings(2050,300,10) ; House11.PlaceBuilding(allplateforms) ; allBuildings.append(House11)
if House11.placeBarrer == True : 
    allFrontBuildings.append(House11) 

House12 = Building.Buildings(2250,300,11) ; House12.PlaceBuilding(allplateforms) ; allBuildings.append(House12)
if House12.placeBarrer == True : 
    allFrontBuildings.append(House12) 

House13 = Building.Buildings(2450,300,12) ; House13.PlaceBuilding(allplateforms) ; allBuildings.append(House13)
if House13.placeBarrer == True : 
    allFrontBuildings.append(House13) 

House14 = Building.Buildings(2650,300,13) ; House14.PlaceBuilding(allplateforms) ; allBuildings.append(House14)
if House14.placeBarrer == True : 
    allFrontBuildings.append(House14) 

House15 = Building.Buildings(2850,300,14) ; House15.PlaceBuilding(allplateforms) ; allBuildings.append(House15)
if House15.placeBarrer == True : 
    allFrontBuildings.append(House15) 

House16 = Building.Buildings(2850,300,15) ; House16.PlaceBuilding(allplateforms) ; allBuildings.append(House16)
if House16.placeBarrer == True : 
    allFrontBuildings.append(House16) 



while running: 

    Pause = False

    dt : int = clock.tick(60)
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


    player.Movement(dt)

    cam.CamFollow(player, dt)

    # left, right, top, bottom
    sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    for i in allplateforms: 

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
    


    for j in allProps : 
        j.onGround = False
        for i in allplateforms: 
            if j.hasCollide == True: 
                side, distance = i.GetCollision(j.Rect)

                if side == 0:
                    continue

                side -= 1

                if side == 3 and i.solidity == False:
                    continue

                direction = sides[side]
                j.posX += direction[0] * distance
                j.posY += direction[1] * distance

                if side == 2:
                    j.onGround = True

        j.Collider(player, dt)
        j.CheckFalling(dt)
        



    # Affichage

    screen.blit(backGround, (0,0))

    
    for j in allProps :

        if j.coinReveal == True : 
            Pause = True
            player.onPause = True
            cam.onPause = True
            player.verticalVelocity = 0
            player.playerVelocity = 0
            coin = coinsManager.coins(j.index-3)
            player.isDashing = False
            coin.show(screen)
            for eventMenu in pygame.event.get():
                if eventMenu.type == pygame.KEYDOWN:
                    if eventMenu.key == pygame.K_ESCAPE and coin.coin != 0:
                        displayImage = False
                        player.onPause = False
                        cam.onPause = False
                        player.saveY = 0
                        j.coinReveal = False
                        player.posY = i.posY
                        allProps.remove(i)
                        coin.coin = 0
                
            pygame.display.update()

            
        elif Pause == False:   
            j.DisplayProp(screen, [cam.pos_cam_x, cam.pos_cam_y ])




    for i in allBuildings:
        i.DrawBuilding(screen, [cam.pos_cam_x, cam.pos_cam_y ] )
    
    for i in allplateforms:
        i.Display(screen, [cam.pos_cam_x, cam.pos_cam_y ] )

    player.DisplayPlayer(screen, cam)

    for i in allFrontBuildings:
        i.DrawBarrer(screen, [cam.pos_cam_x, cam.pos_cam_y ] )



    
    #screen.blit( barrer, (50,80))

    # UI

    count = 0

    for i in player.listHP: 
        screen.blit(i, (SCREEN_WIDTH - 70 - (count*60), 20))
        count +=1
    screen.blit(player.dashImages[player.dashState], (SCREEN_WIDTH - 240 , 100 ))
    
    pygame.display.update()

pygame.quit() 


