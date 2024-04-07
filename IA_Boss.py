import pygame as py
from random import *

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
        self.w_weapon = 100
        self.h_weapon = 20
        #Shield
        self.w_shield = 10
        self.h_shield = h + 10

    def move(self):
        self.x -= 5
    
    def collide_attack(self):
        if (((self.x_weapon - self.w_weapon) <= player.x+player.width 
            and self.x >= player.x 
            and self.y_weapon <= player.y + player.height 
            and self.y_weapon >= player.y)
            or ((self.x_weapon + self.w_weapon) >= player.x
            and self.x + self.width <= player.x +player.width 
            and self.y_weapon <= player.y + player.height 
            and self.y_weapon >= player.y)):
               return True
        return False
           
    def attack(self) :
        clock.tick(60)
        r = self.range_weapon-self.w_weapon+1
        attack = True
        a_duration = 0
        start = py.time.get_ticks()
        if self.x > player.x :
            for _ in range (r//2):
                update_screen()
                self.w_weapon+=2
                if self.collide_attack() and player.hp > 0 and attack:
                    player.hp -= 1
                    attack = False
        else :
            for _ in range(r//2):
                update_screen()
                self.w_weapon+=2
                if self.collide_attack() and player.hp > 0:
                    player.hp -= 1
                    attack = False
        self.w_weapon = self.range_weapon - r - 1
        while a_duration < 150 :
            a_duration = py.time.get_ticks() - start

    def attack_aoe(self):
        py.draw.rect(fen, (255,0,0), (self.x/2,self.y/2,60,30))
        py.display.flip()

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
 

h_screen = 800
w_screen = 600
fen = py.display.set_mode((h_screen, w_screen))
base_ground = 9*(w_screen/10)
player = Player((w_screen/5)+20,base_ground-50,(0,255,255),50,50,3)#x,y,color,w,h
w_athena = 50
h_athena = 100
athena = Boss(4*(w_screen/5),base_ground-h_athena,(255,255,255),w_athena,h_athena)#x,y,color,w,h
clock = py.time.Clock()
attack_t = 0
end_game = 0

continuer = True

def update_screen ():
    fen.fill((150,150,150))
    py.draw.rect(fen,(255,0,255),(0,base_ground,h_screen,w_screen/10))
    if player.hp > 0 :
        py.draw.rect(fen, player.color, (player.x,player.y,player.width,player.height))
    if athena.status_parry == False :
        if athena.x > player.x :
            py.draw.rect(fen, (255,0,0), (athena.x_weapon-athena.w_weapon,athena.y_weapon,athena.w_weapon,athena.h_weapon))
            py.draw.rect(fen, athena.color, (athena.x,athena.y,athena.width,athena.height))
        else :
            py.draw.rect(fen, athena.color, (athena.x,athena.y,athena.width,athena.height))
            py.draw.rect(fen, (255,0,0), (athena.x_weapon,athena.y_weapon,athena.w_weapon,athena.h_weapon))
    else :
        py.draw.rect(fen, (255,255,0), (athena.x,athena.y,athena.width,athena.height))
    py.display.flip()


def pattern_boss():
    if athena.status_parry == False :
        action = randint(1,8)
        if action > 5 and (0 <= athena.x - player.x <= 100 or 0 <= player.x - athena.x <= 100) :
            athena.parry()
        else:
            athena.attack()
    else :
        athena.parry()
    
def player_action():
    pressed = py.key.get_pressed()
    if pressed[py.K_d]:
        player.move(1)
    elif pressed[py.K_q] :
        player.move(-1)


while continuer and end_game < 1500 :
    start_t = py.time.get_ticks()
    update_screen()
    if player.hp > 0:
        player_action()
    if attack_t >= 400 and player.hp > 0 :
       pattern_boss()
       attack_t = 0
    for event in py.event.get():
        if event.type == py.QUIT:
            continuer = False
    
    end_t = py.time.get_ticks()
    attack_t += end_t - start_t
    if player.hp == 0:
        end_game += end_t - start_t
    clock.tick(90)
