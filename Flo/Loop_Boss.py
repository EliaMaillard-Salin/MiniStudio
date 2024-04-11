import pygame as py
import IA_Boss
import Sprite_Boss
import PlayerMovement
import Plateform
import Menu
from random import randint


w_screen = 1920
h_screen = 1080
fen = py.display.set_mode((w_screen, h_screen),py.FULLSCREEN)
base_ground = 9*(h_screen/10)
player = PlayerMovement.Player((w_screen/5)+20,base_ground-50,(w_screen//30),(w_screen//20))#x,y,w,h
w_athena = (w_screen//20)
h_athena = (h_screen//6)
athena = IA_Boss.Boss(4*(h_screen/5),base_ground-h_athena,(255,255,255),w_athena,h_athena, player)#x,y,color,w,h,player
Sprite_Boss.load_anim(athena)
clock = py.time.Clock()
end_game = 0
list_plateform = []
ground = Plateform.Plateform(0,base_ground,w_screen,h_screen/10,(255,0,255))
ground.CreatePlateform(list_plateform)
menu = Menu.Menu(w_screen,h_screen)
fen.fill((0,0,0))
BG = py.image.load("Flo/Temple Athéna Intérieur.png")
bg_resize = py.transform.scale(BG,(1920,1060))

def update_screen (w,h):
    
    fen.fill((0,0,0))
    #Update
    for i in list_plateform :
        if (i.CheckCollision(player.playerRect)):
            player.PlayerOnGround(i.Rect.top)
            athena.BossOnGround(i.Rect.top)
    for i in list_plateform :
        i.Display(fen)
    #fen.blit(bg_resize,(0,0))
    if athena.parry_nb == 0 :
        if athena.x > player.posX :
            py.draw.rect(fen, (255,0,0), (athena.x_weapon-athena.w_weapon,athena.y_weapon,athena.w_weapon,athena.h_weapon))#Weapon
            #py.draw.rect(fen, athena.color, (athena.x,athena.y,athena.width,athena.height))#Athena
        else :
            #py.draw.rect(fen, athena.color, (athena.x,athena.y,athena.width,athena.height))#Athena
            py.draw.rect(fen, (255,0,0), (athena.x_weapon,athena.y_weapon,athena.w_weapon,athena.h_weapon))#Weapon
        if athena.movement :
            Sprite_Boss.walking(athena,fen,player)
        if athena.status_attack:
            Sprite_Boss.attacking(athena,fen,player)
        if athena.status_aoe :
            Sprite_Boss.attacking_aoe(athena,fen,player)
    else :
        py.draw.rect(fen, (255,255,0), (athena.x,athena.y,athena.width,athena.height))
        Sprite_Boss.parrying(athena,fen,player)
    if athena.status_aoe == True :
            py.draw.rect(fen, (0,255,0), (athena.shockwave_r_x,athena.shockwave_y,athena.w_shockwave,athena.h_shockwave))
            py.draw.rect(fen, (0,255,0), (athena.shockwave_l_x,athena.shockwave_y,athena.w_shockwave,athena.h_shockwave))
    
    if player.hp > 0 :
        player.UpdatePlayer(fen)
    #Menu
    if menu.status_pause :
        menu.pause(w,h,fen)
    py.display.flip()





while not menu.quit :
    
    start_t = py.time.get_ticks()
    update_screen(w_screen,h_screen)
    if menu.status_pause == False :
        if athena.movement :
            athena.move()
            if athena.time_walk >= 200 :
                if athena.walk_nb < len(athena.walk)-1 :
                    athena.walk_nb += 1
                else :
                    athena.walk_nb = 0
                athena.time_walk = 0
            athena.pos_img = [athena.x- athena.size_img[0]/3, base_ground - athena.size_img[1]]
        if player.hp > 0:
            player.Movement()
        
        
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
                    if randint(1,3) == 1 :
                        athena.jump()
              
    athena.time_attack += py.time.get_ticks() - start_t
    athena.time_walk += py.time.get_ticks() - start_t
    if player.hp == 0:
        end_game += py.time.get_ticks() - start_t
        if end_game > 1500 :
             menu.quit = True
    clock.tick(200)
print(1)