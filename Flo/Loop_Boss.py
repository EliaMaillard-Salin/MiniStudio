import pygame as py
import IA_Boss
import Sprite_Boss
import PlayerMovement
import Plateform
import Menu
from random import randint

###
w_screen = 1920
h_screen = 1080
###

fen = py.display.set_mode((w_screen, h_screen),py.FULLSCREEN)



###
base_ground = 9*(h_screen/10) + 22
player = PlayerMovement.Player(10,base_ground-50,(w_screen//30),(w_screen//20))#x,y,w,h
w_athena = (w_screen//20)
h_athena = (h_screen//6)
athena = IA_Boss.Boss(w_screen/2-w_athena/2,base_ground-h_athena,(255,255,255),w_athena,h_athena, player)#x,y,color,w,h,player
Sprite_Boss.load_anim(athena)
clock = py.time.Clock()
end_game = 0
menu = Menu.Menu(w_screen,h_screen)
BG = py.image.load("Flo/Salle_Athena.png")
Start_Figth = False
###


list_plateform = []
ground = Plateform.Plateform(0,base_ground,w_screen,h_screen/10,(255,0,255))
ground.CreatePlateform(list_plateform)
statue_g = Plateform.Plateform(792,630,378,13,(255,0,255))
statue_g.CreatePlateform(list_plateform)
pillar1 = Plateform.Plateform(25,335,215,13,(255,0,255))
pillar1.CreatePlateform(list_plateform)
pillar2 = Plateform.Plateform(330,495,180,13,(255,0,255))
pillar2.CreatePlateform(list_plateform)
pillar3 = Plateform.Plateform(1440,495,180,13,(255,0,255))
pillar3.CreatePlateform(list_plateform)
pillar1 = Plateform.Plateform(1685,335,215,13,(255,0,255))
pillar1.CreatePlateform(list_plateform)

def update_screen (w,h):
    
    fen.fill((0,0,0))
    #Update
    for i in list_plateform :
        if (i.CheckCollision(player.playerRect)):
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
    if player.hp > 0 :
        player.UpdatePlayer(fen)
    #Menu
    if menu.status_pause :
        menu.pause(w,h,fen)
    py.display.flip()



while not menu.quit :
    
    start_t = py.time.get_ticks()
    update_screen(w_screen,h_screen)
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
        if player.hp > 0:
            player.Movement()
        if Start_Figth :
            if athena.movement :
                athena.move()
                if athena.time_walk >= 200 :
                    if athena.walk_nb < len(athena.walk)-1 :
                        athena.walk_nb += 1
                    else :
                        athena.walk_nb = 0
                    athena.time_walk = 0
            
        
        
            if (athena.time_attack >= 2000 and player.hp > 0) or (athena.time_attack >= 1000 and athena.parry_nb != 0) or (athena.status_aoe and ((athena.time_attack >= 200 and athena.launch_aoe) or (athena.time_attack >= 50 and athena.launch_aoe == False))) or (athena.status_attack and athena.time_attack > 150) :
                athena.pattern_boss()
                athena.time_attack = 0
                if athena.status_aoe :
                    if athena.collide_aoe(player.playerRect) and player.hp > 0 and athena.status_damage:
                                player.hp -= 1
                                athena.status_damage = False
                if athena.status_attack :
                    if athena.collide_attack(player.playerRect) and player.hp > 0 and athena.status_damage:
                                player.hp -= 1
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
    if player.hp == 0:
        end_game += py.time.get_ticks() - start_t
        if end_game > 1500 :
             menu.quit = True