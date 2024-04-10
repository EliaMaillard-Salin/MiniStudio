import pygame
import PlayerFiles.PlayerMovement as Player
import PlatformsFiles.PlatformsClass as Platforms
import CameraFiles.Camera as Camera
import PropsFiles.Props as Props
import csv
import PropsFiles.coinsManager as coinsManager

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

# print(textures) 
# print(textures[6])

#############################################################################################
    
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



#########################################


clock = pygame.time.Clock()

running : bool = True

player  = Player.Player(300,200,50,50)
ground  = pygame.Rect(0,400,500,100)



P6 = Platforms.Plateform(0, 550, 10000, 20, "red",None,True)
P6.CreatePlateform(platforms)



backGround = pygame.image.load("PythonFiles/Assets/PNG/BackGround.png")


allProps : list[Props.Props] = []


square = Props.Props(True,False,20,150,50,50,True,1,0, False)
allProps.append(square)

food = Props.Props(False,True,650,300,50,50,False,1,1, False)
allProps.append(food)

cam = Camera.Camera(SCREEN_WIDTH,SCREEN_HEIGHT,player.playerVelocity)

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


    for i in platforms: 

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
        for i in platforms: 
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

    for i in platforms:
        i.Display(screen, [cam.pos_cam_x, cam.pos_cam_y ] )

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

    player.DisplayPlayer(screen, cam)

    # UI

    count = 0

    for i in player.listHP: 
        screen.blit(i, (SCREEN_WIDTH - 70 - (count*60), 20))
        count +=1
    screen.blit(player.dashImages[player.dashState], (SCREEN_WIDTH - 240 , 100 ))
    
    pygame.display.update()

pygame.quit() 


