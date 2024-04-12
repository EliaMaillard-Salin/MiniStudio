import pygame as py
import IA_Boss
import Sprite_Boss
from PlatformsFiles.PlatformsClass import Plateform
import Menu
from random import randint
from PlayerFiles.PlayerMovement import Player 

###
w_screen = 1920
h_screen = 1080

walktime = 0
hurt = 0
attack = 0
death = 0
idle = 0
stop = 0
animpause  = False


###

fen = py.display.set_mode((w_screen, h_screen),py.FULLSCREEN)



###
base_ground = 9*(h_screen/10) + 22
player = Player(10,base_ground-50,(w_screen//30),(w_screen//20))#x,y,w,h
player.load_anim_player()
w_athena = (w_screen//20)
h_athena = (h_screen//6)
athena = IA_Boss.Boss(w_screen/2-w_athena/2,base_ground-h_athena,(255,255,255),w_athena,h_athena, player)#x,y,color,w,h,player
Sprite_Boss.load_anim(athena)
clock = py.time.Clock()
end_game = 0
menu = Menu.Menu(w_screen,h_screen)
BG = py.image.load("GodSmith Odyssey/Project/Athena/Salle_Athena.png")
Start_Figth = False
###

keys = py.key.get_pressed()


list_plateform = []
ground = Plateform(0,base_ground,w_screen,h_screen/10,(255,0,255), None, False)
ground.CreatePlateform(list_plateform)
statue_g = Plateform(792,630,378,13,(255,0,255), None, False)
statue_g.CreatePlateform(list_plateform)
pillar1 = Plateform(25,335,215,13,(255,0,255), None, False)
pillar1.CreatePlateform(list_plateform)
pillar2 = Plateform(330,495,180,13,(255,0,255), None, False)
pillar2.CreatePlateform(list_plateform)
pillar3 = Plateform(1440,495,180,13,(255,0,255), None, False)
pillar3.CreatePlateform(list_plateform)
pillar1 = Plateform(1685,335,215,13,(255,0,255), None, False)
pillar1.CreatePlateform(list_plateform)


font : py.font.Font = py.font.Font('GodSmith Odyssey/Project/Assets/Fonts/Unbounded-Regular.ttf', 30)

imgAthena = py.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/Tete Vie Athéna.png")

def update_screen (w,h):
    
    fen.fill((0,0,0))
    #Update
    sides = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in list_plateform: 

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
                athena.BossOnGround(i.Rect.top)
    fen.blit(BG,(0,0))
    #Show collide
    #for i in list_plateform :
    #    i.Display(fen)
    if Start_Figth :
        if athena.parry_nb == 0 :
            if athena.movement:
                Sprite_Boss.walking(athena,fen,player)
            if athena.status_attack:
                Sprite_Boss.attacking(athena,fen,player)
            if athena.status_aoe :
                Sprite_Boss.attacking_aoe(athena,fen,player)
        else :
            Sprite_Boss.parrying(athena,fen,player)
        if athena.status_aoe == True :
                Sprite_Boss.onde(athena, fen, player)
    else :
        if athena.provoc_nb >= -1 and athena.provoc_status:
            Sprite_Boss.provoc(athena, fen, player)
        if not athena.provoc_status :
            Sprite_Boss.idle(athena, fen, player)
    #Menu
    if menu.status_pause :
        menu.pause(w,h,fen)




while not menu.quit :
    
    start_t = py.time.get_ticks()
    dt = clock.tick(60)
    dt/=1000

    update_screen(w_screen,h_screen)

    if player.health > 0 :
            
            if player.isDead == True and stop != 1:
                player.PlayerDeath(fen, [0, 0 ])
                player.death += 1
                if player.death == 2 :
                    player.playerdeath_nb += 1
                    player.death = 0
                if player.playerdeath_nb == 19 : 
                    player.playerdeath_nb = 0
                    player.isDead == False
                    stop = 1
            
            if player.getHit == True and player.isDead == False and stop != 1:
                player.PlayerHurt(fen, [0, 0 ])
                player.hurt += 1
                if player.hurt == 3 :
                    player.playerhurt_nb += 1
                    player.hurt = 0
                if player.playerhurt_nb == 12 :
                    player.playerhurt_nb = 0
                    player.getHit = False
            
            if player.playattack == True and player.getHit == False and player.isDead == False and stop != 1:
                if player.playdash == False : 
                    player.PlayerAttack(fen, [0, 0 ])
                    player.attack_time += 1
                    if player.attack_time == 2 :
                        player.playerattack_nb += 1
                        player.attack_time = 0        
                    if player.playerattack_nb == 15:
                        player.playerattack_nb = 0
                        player.playattack = False
                

            if player.playjump == True  and player.playattack == False and player.isDead == False and stop != 1:
                if player.playdash == False :  
                    player.PlayerJump(fen, [0, 0 ])
                    player.jump_time += 1     
                    if player.jump_time == 2 :
                        player.playerjump_nb += 1
                        player.jump_time = 0        
                    if player.playerjump_nb == 22:
                        player.playerjump_nb = 0
                        player.playjump = False
                        player.PauseIdle == 0
                        player.PauseMove == 0
            
            if player.playdash == True and player.getHit == False and player.isDead == False and stop != 1:
                player.Dash(fen, [0, 0 ])
                player.dash_time += 1     
                if player.dash_time == 2 :
                    player.playerdash_nb += 1
                    player.dash_time = 0        
                if player.playerdash_nb == 28:
                    player.playerdash_nb = 0
                    player.playdash = False

            #Animation idle player
            ##########################################
            if player.PauseIdle == 0 and player.playdash == False and player.playjump == False and player.playattack == False and player.getHit == False and player.isDead == False and stop != 1:
                player.Idle(fen, [0, 0 ])
                idle += 1
                if idle == 4 :
                    player.playeridle_nb += 1
                    idle = 0
                if player.playeridle_nb == 20 :
                    player.playeridle_nb = 0
            ##########################################
        
            if player.playwalk == True and player.playdash == False and player.PauseMove == 0 and player.playjump == False and player.playattack == False and player.getHit == False and player.isDead == False and stop != 1:
                player.PauseIdle = 1
                player.PlayerWalk(fen, [0, 0 ])
                player.timeWalk += 1
                if player.timeWalk == 4 :
                    player.playerwalk_nb += 1
                    player.timeWalk = 0
                    player.playerwalk_nb_save = player.playerwalk_nb
                if player.playerwalk_nb == len(player.imganim[2]) :
                    player.playerwalk_nb = 0
                    if keys[py.K_d] or keys[py.K_q]:
                        player.playwalk = True
                    else :
                        player.playwalk = False
                        player.PauseIdle = 0
    
    ###UI###

    fen.blit(player.playerIcon, (15,35))

    count = 0
    for i in player.listHP: 
        fen.blit(i, ( 305  + (count*60), 70))
        count +=1
    fen.blit(player.dashImages[player.dashState], ( 150,50 ))
    currentFPS = int(1000/(dt*1000))
    displayFPS : py.Surface = py.transform.scale(font.render(str(currentFPS), True, (0,0,0)), (35,30) )
    fen.blit(displayFPS, (25,150))


    fen.blit(imgAthena, (w_screen//2, 35))
    

    
    py.display.flip()
    if not Start_Figth :
        if athena.provoc_time > 1000 :
            if athena.provoc_nb == 1:
                    Start_Figth = True
                    athena.time_attack = 0
                    athena.provoc_status = False
            if athena.x - player.posX <= 300 and not Start_Figth :
                athena.active_provoc()
                athena.provoc_status = True
            athena.provoc_time = 0
            
        
        if athena.idle_time > 600  and not athena.provoc_status:
            athena.idle_time = 0 
            athena.active_idle()
        
    if menu.status_pause == False :
        if player.health > 0:
            player.Movement(dt)
        if Start_Figth :
            if athena.movement :
                athena.move()
                if athena.time_walk >= 200 :
                    if athena.walk_nb < len(athena.walk)-1 :
                        athena.walk_nb += 1
                    else :
                        athena.walk_nb = 0
                    athena.time_walk = 0
            
        
        
            if (athena.time_attack >= 2000 and player.health > 0) or (athena.time_attack >= 1000 and athena.parry_nb != 0) or (athena.status_aoe and ((athena.time_attack >= 200 and athena.launch_aoe) or (athena.time_attack >= 50 and athena.launch_aoe == False))) or (athena.status_attack and athena.time_attack > 150) :
                athena.pattern_boss()
                athena.time_attack = 0
                if athena.status_aoe :
                    if athena.collide_aoe(player.playerRect) and player.health > 0 and athena.status_damage:
                                player.health -= 1
                                athena.status_damage = False
                if athena.status_attack :
                    if athena.collide_attack(player.playerRect) and player.health > 0 and athena.status_damage:
                                player.health -= 1
                                athena.status_damage = False

    if menu.status_pause == False:
        for event in py.event.get():
            if event.type == py.KEYDOWN :
                if event.key == py.K_p :
                    menu.status_pause = True
                elif event.key == py.K_SPACE :
                    if not player.isJumping:
                        player.isJumping = True
                        player.verticalVelocity = -player.jumpForce
                    if randint(1,3) == 1 and ((not athena.status_aoe) or athena.parry_nb != 0 or athena.status_attack) and Start_Figth :
                        athena.jump()
    if not athena.isJumping and not athena.provoc_status :          
        athena.time_attack += py.time.get_ticks() - start_t
    athena.time_walk += py.time.get_ticks() - start_t
    if not Start_Figth :
        athena.provoc_time += py.time.get_ticks() - start_t
        athena.idle_time += py.time.get_ticks() - start_t
    if player.health == 0:
        end_game += py.time.get_ticks() - start_t
        if end_game > 1500 :
             menu.quit = True