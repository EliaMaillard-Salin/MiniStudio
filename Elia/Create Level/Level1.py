import pygame
import PlayerFiles.PlayerMovement as Player
import PlatformsFiles.PlatformsClass as Platforms
import CameraFiles.Camera as Camera
import PropsFiles.Props as Props
import csv
import PropsFiles.coinsManager as coinsManager
import PlatformsFiles.Building as Building
import time
import IA.Mobs.BotInfo as Bots



walktime = 0
hurt = 0
attack = 0
death = 0
idle = 0
stop = 0
pause  = False

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
keys = pygame.key.get_pressed()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GodSmith Odyssey")


# Paramètres du jeu - Init grid 
ROWS = 16
TILE_SIZE = SCREEN_HEIGHT // ROWS # Assure-toi que cette valeur correspond à celle utilisée dans l'éditeur
TILE_TYPES = 12

font : pygame.font.Font = pygame.font.Font('PythonFiles/Assets/Fonts/Unbounded-Regular.ttf', 30)

# Store textures in a list - List des Blocs 

textures : list[pygame.Surface] = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'PythonFiles/Assets/PNG/Blocs/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	textures.append(img)


def load_level(level_path):
    with open(level_path, 'r') as file: #recup csv level 
        return list(csv.reader(file))

def create_platforms(level_data : list[list[str]], emptyTiles : list[Platforms.Plateform]) -> list[Platforms.Plateform]:  #Create Plateform par Bloc 
    platforms : list[Platforms.Plateform]= []
    for y, row in enumerate(level_data):
        for x, tile_type in enumerate(row):
            if tile_type == -1 : 
                continue
            if tile_type == 11: 
                emptyTiles.append(Platforms.Plateform(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE,None, textures[level_data[y][x]], True))

            platforms.append(Platforms.Plateform(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE,None, textures[level_data[y][x]], True))
    return platforms

# Charge le niveau

EndLevel :pygame.Surface = pygame.transform.scale(pygame.image.load("Elia/Create Level/Assets/PNG/Asset Batiment/Temple/Entrée du temple/Visuel Final.png"), (832,800))

loading_level_data = load_level("Elia/Create Level/Levels/level1_data.csv")

level_data = [[int(x) for x in inner] for inner in loading_level_data] # Convertit les valeurs en entiers

emptyTiles : list[Platforms.Plateform] = []

platforms : list[Platforms.Plateform] = create_platforms(level_data, emptyTiles) # Crée les plateformes à partir des données du niveau

Stair1 = Platforms.Plateform(7800,310,300,25,None, None, True) ; Stair1.CreatePlateform(platforms)
Stair2 = Platforms.Plateform(7910,290,300,25,None, None, True); Stair2.CreatePlateform(platforms)
Stair3 = Platforms.Plateform(8010,270,300,25,None, None, True); Stair3.CreatePlateform(platforms)
Stair4 = Platforms.Plateform(8110,250,300,25,None, None, True); Stair4.CreatePlateform(platforms)

TP = Platforms.Plateform(8300,100,30,400,None,None,False)

clock = pygame.time.Clock()

running : bool = True

player  = Player.Player(50,250,50,50)
player.load_anim_player()
ground  = pygame.Rect(0,400,500,100)


allProps : list[Props.Props] = []

allBuildings : list[Building.Buildings]= []

allFrontBuildings : list[Building.Buildings] = []

allMobs : list[Bots.Bot] = []

cam = Camera.Camera(SCREEN_WIDTH,SCREEN_HEIGHT,player.playerVelocity)

backGround = pygame.image.load("PythonFiles/Assets/PNG/BackGround.png")

# Index for Buildings : 0 = Maison Carré, 1 = Maison Carré Double, 2 = Maison Carré Haute, 3 = Maison Ronde, 4 = Maison Ronde Fenetre, 5 = Maison 2etage Rouge 
# 6 = Maison 2 etages Jaunes, 7 = Maison Champignon Jaune, 8 = Maison Champignon Rouge, 9 = Tour Jaune,10 = Tour Rouge, 11 = Hutte arriere plan, 12 = tour arrier plan 
# 13 = maison carre arriere plan, 14 = Pillier, 15 = Temple 

def ImportBuilding(): 
    House8 = Building.Buildings(1100,470,11) ; House8.PlaceBuilding(platforms) ; allBuildings.append(House8)
    if House8.placeBarrer == True : 
        allFrontBuildings.append(House8) 
    House9 = Building.Buildings(1300,470,13) ; House9.PlaceBuilding(platforms) ; allBuildings.append(House9)
    if House9.placeBarrer == True : 
        allFrontBuildings.append(House9) 
    House10 = Building.Buildings(960,272,12) ; House10.PlaceBuilding(platforms) ; allBuildings.append(House10)
    if House10.placeBarrer == True : 
        allFrontBuildings.append(House10) 
    House1 = Building.Buildings(50,650,0) ; House1.PlaceBuilding(platforms) ; allBuildings.append(House1)
    if House1.placeBarrer == True : 
        allFrontBuildings.append(House1) 
    House2 = Building.Buildings(250,650,1) ; House2.PlaceBuilding(platforms) ; allBuildings.append(House2)
    if House2.placeBarrer == True : 
        allFrontBuildings.append(House2) 
    House3 = Building.Buildings(750,335,5) ; House3.PlaceBuilding(platforms) ; allBuildings.append(House3)
    if House3.placeBarrer == True : 
        allFrontBuildings.append(House3) 
    House4 = Building.Buildings(980,400,7) ; House4.PlaceBuilding(platforms) ; allBuildings.append(House4)
    if House4.placeBarrer == True : 
        allFrontBuildings.append(House4) 
    House5 = Building.Buildings(1400,430,4) ; House5.PlaceBuilding(platforms) ; allBuildings.append(House5)
    if House5.placeBarrer == True : 
        allFrontBuildings.append(House5) 
    House7 = Building.Buildings(1200,450,2) ; House7.PlaceBuilding(platforms) ; allBuildings.append(House7)
    if House7.placeBarrer == True : 
        allFrontBuildings.append(House7) 
    House12 = Building.Buildings(1830,450,3) ; House12.PlaceBuilding(platforms) ; allBuildings.append(House12)
    if House12.placeBarrer == True : 
        allFrontBuildings.append(House12) 
    House11 = Building.Buildings(1600,335,6) ; House11.PlaceBuilding(platforms) ; allBuildings.append(House11)
    if House11.placeBarrer == True : 
        allFrontBuildings.append(House11) 
    House6 = Building.Buildings(2100,-25,10) ; House6.PlaceBuilding(platforms) ; allBuildings.append(House6)
    if House6.placeBarrer == True : 
        allFrontBuildings.append(House6) 

    Pillier1 = Building.Buildings(2800,605,14) ; Pillier1.PlaceBuilding(platforms) ; allBuildings.append(Pillier1)
    if Pillier1.placeBarrer == True : 
        allFrontBuildings.append(Pillier1) 

    # Pillier2 = Building.Buildings(3800,540,14) ; Pillier2.PlaceBuilding(platforms) ; allBuildings.append(Pillier2)
    # if Pillier2.placeBarrer == True : 
    #     allFrontBuildings.append(Pillier2) 
    # Pillier3 = Building.Buildings(4250,360,14) ; Pillier3.PlaceBuilding(platforms) ; allBuildings.append(Pillier3)
    # if Pillier3.placeBarrer == True : 
    #     allFrontBuildings.append(Pillier3) 
    # Pillier4 = Building.Buildings(4600,240,14) ; Pillier4.PlaceBuilding(platforms) ; allBuildings.append(Pillier4)
    # if Pillier4.placeBarrer == True : 
    #     allFrontBuildings.append(Pillier4) 

    TempleDeco = Building.Buildings(5000,-350,15) ; TempleDeco.PlaceBuilding(platforms) ; allBuildings.append(TempleDeco)
    if TempleDeco.placeBarrer == True : 
        allFrontBuildings.append(TempleDeco) 

    Pillier2 = Building.Buildings(7200,240,14) ; Pillier2.PlaceBuilding(platforms) ; allBuildings.append(Pillier2)
    if Pillier2.placeBarrer == True : 
        allFrontBuildings.append(Pillier2) 
    Pillier3 = Building.Buildings(6600,240,14) ; Pillier3.PlaceBuilding(platforms) ; allBuildings.append(Pillier3)
    if Pillier3.placeBarrer == True : 
        allFrontBuildings.append(Pillier3) 

ImportBuilding()

#Index Props : 0 - bol, 1 - tentacles, 2 - fasolada, 3 - moussaka, 4 - Pièce Agora, 5- Pièce Dionysos
# 6 - Pièce Temple Zeus, 7 - arbre, 8 - arbre2, 9 - Box, 10 - linge, 11 - lys, 12 - nuage1, 13- nuage2, 14- Statue Athena, 15 - Statue Chouette, 
# 16 - Vase motifs, 17 - Vase NoMotifs, 18 - vase fleurs

def ImportProps():


    Coin1 =  Props.Props(False,False,2200, 100, 50,50,False,1,4,True) ; allProps.append(Coin1)
    Coin2 =  Props.Props(False,False,3770, 870, 50,50,False,1,5,True) ; allProps.append(Coin2)
    Coin3 =  Props.Props(False,False,5500 , 20, 50,50,False,1,6,True) ; allProps.append(Coin3)


    Food2 =  Props.Props(False,True, 4300 , 250, 50,50,False,1,2,False) ; allProps.append(Food2)
    Food3 =  Props.Props(False,True, 7250, 150, 50,50,False,1,3,False) ; allProps.append(Food3)
    
    Box1 =  Props.Props(True,False, 3900 , 820, 70,70,True,2,9,False) ; allProps.append(Box1)
    Box2 =  Props.Props(True,False, 4200 , 200, 70,70,True,2,9,False) ; allProps.append(Box2)
    Box3 =  Props.Props(True,False, 4500 , 100, 70,70,True,2,9,False) ; allProps.append(Box3)

ImportProps()


Mob1 = Bots.Bot(3400,500,80,140, [3220,500], [3700,500]) ;  Mob1.load_anim_bot() ; allMobs.append(Mob1)
Mob2 = Bots.Bot(5400,200,80,140, [4900,200],[6220,200]);  Mob2.load_anim_bot() ;  allMobs.append(Mob2)
Mob3 = Bots.Bot(5850,200,80,140, [4900,200],[6220,200]); Mob3.load_anim_bot() ;  allMobs.append(Mob3)

StartAthena = False

while running: 

    Pause = False
    dt = clock.tick(60)
    dt/=1000


    if player.immortality == True and pygame.time.get_ticks() - player.startImmortality >= 1000: 
        player.immortality =False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.playjump = True
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not player.isJumping:
                player.isJumping = True
                player.verticalVelocity = -player.jumpForce
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            player.Attack() 
    
    if stop != 1:
        for i in allMobs:
            i.CollisionBot(player)
        player.Movement(dt)

    print(player.posX, player.posY)

    if player.posY >= SCREEN_HEIGHT + cam.limit_bottom :
        player.posX = 50
        player.posY = 250
        cam.pos_cam_x = 0
        cam.pos_cam_y = -30

    if player.posY + player.height <=cam.limit_top : 
        player.posX = 50
        player.posY = 250
        cam.pos_cam_x = 0
        cam.pos_cam_y = -30


    for i in allMobs: 
        i.MovementBot()
        i.CheckCollision()
    

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
        if j.posY >= SCREEN_HEIGHT + cam.limit_bottom  or j.posY + j.height <= cam.limit_top: 
            j.posY = j.spawnY ; j.posX = j.spawnX
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
        
    if TP.GetCollision(player.playerRect) != (0,0): 
        StartAthena = True
        running = False


    # Affichage

    screen.blit(backGround, (0,0))

    for i in allBuildings:
        i.DrawBuilding(screen, [cam.pos_cam_x, cam.pos_cam_y ] )
    
    for i in platforms:
        i.Display(screen, [cam.pos_cam_x, cam.pos_cam_y ] )
        
    for i in emptyTiles: 
        i.Display(screen, [cam.pos_cam_x, cam.pos_cam_y])

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
                        player.posY = j.posY
                        allProps.remove(j)
                        coin.coin = 0
                        player.playerVelocity = 300
                


            
        elif Pause == False:   
            j.DisplayProp(screen, [cam.pos_cam_x, cam.pos_cam_y ])


    if Pause == False : 

        for i in allMobs:       
            if i.PlayerDeath == True and stop != 1:
                player.PlayerDeath(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                player.death += 1
                if player.death == 2 :
                    player.playerdeath_nb += 1
                    player.death = 0
                if player.playerdeath_nb == 19 : 
                    player.playerdeath_nb = 0
                    i.PlayerDeath == False
                    stop = 1
            
            if i.damage == True and i.PlayerDeath == False and stop != 1:
                player.PlayerHurt(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                player.hurt += 1
                if player.hurt == 3 :
                    player.playerhurt_nb += 1
                    player.hurt = 0
                if player.playerhurt_nb == 12 :
                    player.playerhurt_nb = 0
                    i.damage = False
            
            if player.playattack == True and i.damage == False and i.PlayerDeath == False and stop != 1:
                if player.playdash == False : 
                    player.PlayerAttack(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                    player.attack_time += 1
                    if player.attack_time == 2 :
                        player.playerattack_nb += 1
                        player.attack_time = 0        
                    if player.playerattack_nb == 15:
                        player.playerattack_nb = 0
                        player.playattack = False
                

            if player.playjump == True  and player.playattack == False and i.PlayerDeath == False and stop != 1:
                if player.playdash == False :  
                    player.PlayerJump(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                    player.jump_time += 1     
                    if player.jump_time == 2 :
                        player.playerjump_nb += 1
                        player.jump_time = 0        
                    if player.playerjump_nb == 22:
                        player.playerjump_nb = 0
                        player.playjump = False
                        player.PauseIdle == 0
                        player.PauseMove == 0
            
            if player.playdash == True and i.damage == False and i.PlayerDeath == False and stop != 1:
                player.Dash(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                player.dash_time += 1     
                if player.dash_time == 2 :
                    player.playerdash_nb += 1
                    player.dash_time = 0        
                if player.playerdash_nb == 28:
                    player.playerdash_nb = 0
                    player.playdash = False

            #Animation idle player
            ##########################################
            if player.PauseIdle == 0 and player.playdash == False and player.playjump == False and player.playattack == False and i.damage == False and i.PlayerDeath == False and stop != 1:
                player.Idle(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                idle += 1
                if idle == 4 :
                    player.playeridle_nb += 1
                    idle = 0
                if player.playeridle_nb == 20 :
                    player.playeridle_nb = 0
            ##########################################
        
            if player.playwalk == True and player.playdash == False and player.PauseMove == 0 and player.playjump == False and player.playattack == False and i.damage == False and i.PlayerDeath == False and stop != 1:
                player.PauseIdle = 1
                player.PlayerWalk(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                player.timeWalk += 1
                if player.timeWalk == 4 :
                    player.playerwalk_nb += 1
                    player.timeWalk = 0
                    player.playerwalk_nb_save = player.playerwalk_nb
                if player.playerwalk_nb == len(player.imganim[2]) :
                    player.playerwalk_nb = 0
                    if keys[pygame.K_d] or keys[pygame.K_q]:
                        player.playwalk = True
                    else :
                        player.playwalk = False
                        player.PauseIdle = 0

        
        walktime += 1  
        for i in allMobs :

            if i.hp != 0:
                i.walking(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                
            # Attack
            if i.attack == True and stop != 1:
                pause = True
                attack += 1
                i.walk = False
                i.Checkpoint1 = False
                i.Checkpoint2 = False
                i.BotAttack(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                if attack == 2 :
                    i.botAttack_nb += 1
                    attack = 0
                
            if i.botAttack_nb == 23:
                i.botAttack_nb = 0
                i.attack = False
                i.walk = True
                if i.BotDirection == -1 :
                    i.Checkpoint1 = True
                elif i.BotDirection == 1:
                    i.Checkpoint2 = True
                
            # Death 
            if i.death == True and stop != 1:
                pause = True
                death += 1
                i.walk = False
                i.Checkpoint1 = False
                i.Checkpoint2 = False
                i.BotDeath(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                if death == 2 :
                    i.botdeath_nb += 1
                    death = 0
                    
            if i.botdeath_nb == 30:
                i.botdeath_nb = 0
                i.Death()
                i.death = False
                i.walk = True
                if i.BotDirection == -1 :
                    i.Checkpoint1 = True
                elif i.BotDirection == 1:
                    i.Checkpoint2 = True
                
                
            # Hurt
            if i.hurt == True and stop != 1:
                pause = True
                hurt += 1
                i.walk = False
                i.Checkpoint1 = False
                i.Checkpoint2 = False
                i.BotHurt(screen, [cam.pos_cam_x, cam.pos_cam_y ])
                if hurt == 4:
                    i.bothurt_nb += 1
                    hurt = 0
            
            if i.bothurt_nb == 19:
                i.bothurt_nb = 0
                i.hurt = False
                i.walk = True
                if i.BotDirection == -1 :
                    i.Checkpoint1 = True
                elif i.BotDirection == 1:
                    i.Checkpoint2 = True
                    
                # Walk
            if stop != 1 :
                walktime += 1  
                if walktime == 10:
                    i.botdesign_nb += 1
                    walktime = 0
            
                if i.botdesign_nb == 5 :
                    i.botdesign_nb = 0

            i.DisplayCheckBot(screen)

        screen.blit(EndLevel, (7800 -cam.pos_cam_x, -465 - cam.pos_cam_y))

        for i in allFrontBuildings:
            i.DrawBarrer(screen, [cam.pos_cam_x, cam.pos_cam_y ] )


        # UI
                
        screen.blit(player.playerIcon, (15,35))

        count = 0
        for i in player.listHP: 
            screen.blit(i, ( 305  + (count*60), 70))
            count +=1
        screen.blit(player.dashImages[player.dashState], ( 150,50 ))
        currentFPS = int(1000/(dt*1000))
        displayFPS : pygame.Surface = pygame.transform.scale(font.render(str(currentFPS), True, (0,0,0)), (35,30) )
        screen.blit(displayFPS, (25,150))





    if player.isDead == True : 
        player.HUDdeath(screen)

    pygame.display.update()




            



#Food1 =  Props.Props(False,True, 5000 , 100, 50,50,False,1,1,False) ; allProps.append(Food1)

if StartAthena == True : 
    running = True 
    while running : 
        #all Athena Code 
        print("Help")




if player.isDead :
    #DisplayDead
    print("Dead")
pygame.quit()

