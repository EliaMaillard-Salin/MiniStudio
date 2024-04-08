import pygame as py
from random import *
import PlayerMovement

class Boss:
    def __init__(self, x,y,c,w,h):
        #Athena
        self.x = x
        self.y = y
        self.color = c
        self.width = w
        self.height = h
        self.status_parry = False
        #Weapon 
        self.x_weapon = self.x + (self.width/2)
        self.y_weapon = self.y + (self.height/2)
        self.range_weapon = 250
        self.w_weapon = 50
        self.base_w_weapon = self.w_weapon
        self.h_weapon = 20
        self.attackRect = py.Rect(self.x_weapon,self.y_weapon,self.w_weapon,self.h_weapon)
        #Shield
        self.w_shield = 10
        self.h_shield = h + 10
        #Aoe
        self.w_shockwave = 30
        self.h_shockwave = 20
        self.shockwave_y = base_ground-self.h_shockwave
        self.shockwave_l_x = self.x-self.w_shockwave
        self.shockwave_r_x = self.x+self.width
        self.AoeRect_l = py.Rect(self.shockwave_l_x,self.shockwave_y,self.w_shockwave,self.h_shockwave)
        self.AoeRect_r = py.Rect(self.shockwave_r_x,self.shockwave_y,self.w_shockwave,self.h_shockwave)
        #Condition
        self.time_attack = 0
        self.movement = True
        self.status_aoe = False
        self.status_attack = False
        self.status_damage = True

    def move(self):
        if self.x > player.posX+player.width :
            self.x -= 0.5
        elif self.x + self.width < player.posX :
            self.x += 0.5
        self.x_weapon = self.x + (self.width/2)
        self.shockwave_l_x = self.x-self.w_shockwave
        self.shockwave_r_x = self.x+self.width
    
    def collide_attack(self,weapon,object):
        if (weapon.right >= object.left and 
            weapon.left <= object.right and
            weapon.top <= object.bottom  and 
            weapon.bottom >= object.top):  
            return True
        return False
           
    def attack(self) :
        self.status_attack = True
        self.movement = False
        r = (self.range_weapon-(self.w_weapon//2))+1
        if self.x > player.posX :
            if self.w_weapon < r :
                self.w_weapon+=15
            else :
                self.w_weapon = self.base_w_weapon
                self.movement = True
                self.status_attack = False
        else :
            if self.w_weapon < r :
                self.w_weapon+=15
            else :
                self.w_weapon = self.base_w_weapon
                self.movement = True
                self.status_attack = False

    def attack_aoe(self):
        self.status_aoe = True
        self.movement = False
        min_x = 0
        max_x = w_screen
        if self.shockwave_l_x >= min_x or self.shockwave_r_x <= max_x :
            self.shockwave_l_x -= self.w_shockwave
            self.shockwave_r_x += self.w_shockwave
        else :
            self.status_aoe = False
            self.movement = True

    def parry(self):
        if self.status_parry == False:
            py.draw.rect(fen, (255,255,0), (self.x,self.y,self.width,self.height))
            py.display.flip()
            self.status_parry = True
        else:
            py.draw.rect(fen, self.color, (self.x,self.y,self.width,self.height))
            py.display.flip()
            self.status_parry = False
    
     

class Player:
    def __init__(self, x,y,c,w,h,hp):
        self.x = x
        self.y = y
        self.color = c
        self.width = w
        self.height = h
        self.hp = hp
    
    def move(self, m):
        self.x += m*5
 


w_screen = 800
h_screen = 600
fen = py.display.set_mode((w_screen, h_screen))
base_ground = 9*(h_screen/10)
player = PlayerMovement.Player((w_screen/5)+20,base_ground-50,50,50)#x,y,w,h
w_athena = 50
h_athena = 100
athena = Boss(4*(h_screen/5),base_ground-h_athena,(255,255,255),w_athena,h_athena)#x,y,color,w,h
clock = py.time.Clock()
end_game = 0

continuer = True

def update_screen ():
    fen.fill((150,150,150))
    py.draw.rect(fen,(255,0,255),(0,base_ground,w_screen,h_screen/10))
    if player.hp > 0 :
        player.UpdatePlayer(fen)
    if athena.status_parry == False :
        if athena.x > player.posX :
            py.draw.rect(fen, (255,0,0), (athena.x_weapon-athena.w_weapon,athena.y_weapon,athena.w_weapon,athena.h_weapon))
            py.draw.rect(fen, athena.color, (athena.x,athena.y,athena.width,athena.height))
        else :
            py.draw.rect(fen, athena.color, (athena.x,athena.y,athena.width,athena.height))
            py.draw.rect(fen, (255,0,0), (athena.x_weapon,athena.y_weapon,athena.w_weapon,athena.h_weapon))
    else :
        py.draw.rect(fen, (255,255,0), (athena.x,athena.y,athena.width,athena.height))
    if athena.status_aoe == True :
            py.draw.rect(fen, (0,255,0), (athena.shockwave_r_x,athena.shockwave_y,athena.w_shockwave,athena.h_shockwave))
            py.draw.rect(fen, (0,255,0), (athena.shockwave_l_x,athena.shockwave_y,athena.w_shockwave,athena.h_shockwave))
    py.display.flip()


def pattern_boss():
    if athena.status_aoe == True :
        athena.attack_aoe()
        return None
    else :
        athena.shockwave_l_x = athena.x-athena.w_shockwave
        athena.shockwave_r_x = athena.x+athena.width
    if athena.status_attack :
        athena.attack()
        return None
    if athena.status_parry == False:
        action = randint(1,8)
        athena.status_damage = True
        if action > 5 and (0 <= athena.x - player.posX <= 100 or 0 <= player.posX - athena.x <= 100) :
            athena.parry()
        else:
            if randint(1,3) == 1 :
                athena.attack_aoe()
            else : 
                athena.attack()
    else :
        athena.parry()


while continuer and end_game < 1500 :
    start_t = py.time.get_ticks()
    update_screen()
    #if athena.movement :
    #    athena.move()
    if player.hp > 0:
        player.Movement()
    if (athena.time_attack >= 500 and player.hp > 0) or (athena.time_attack >= 400 and athena.status_parry) or (athena.status_aoe and athena.time_attack >= 10) or (athena.status_attack) :
        pattern_boss()
        athena.time_attack = 0
        if athena.status_aoe :
            if (athena.collide_attack(athena.AoeRect_l,player.playerRect)) or (athena.collide_attack(athena.AoeRect_r,player.playerRect)) and player.hp > 0 and athena.status_damage:
                        player.hp -= 1
                        athena.status_damage = False
        if athena.status_attack :
            if athena.collide_attack(athena.attackRect,player.playerRect) and player.hp > 0 and athena.status_damage:
                        player.hp -= 1
                        athena.status_damage = False
    for event in py.event.get():
        if event.type == py.QUIT:
            continuer = False
    
    athena.time_attack += py.time.get_ticks() - start_t
    print(athena.time_attack)

    if player.hp == 0:
        end_game += py.time.get_ticks() - start_t
    clock.tick(90)
