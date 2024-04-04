import pygame as py
from random import *
import time

class Boss:
    def __init__(self, x,y,c,w,h):
        self.x = x
        self.y = y
        self.color = c
        self.width = w
        self.height = h

    def move(self):
        self.x -= 5
    
    def attack(self) :
        py.draw.rect(fen, (255,0,0), (athena.x,athena.y,athena.width,athena.height))
        py.display.flip()

    def parry(self):
        if -100 <= self.x - player.x <= 100 :
            p = randint(1,100)
            if p <= +(self.x - player.x):
                py.draw.rect(fen, (255,255,0), (athena.x,athena.y,athena.width,athena.height))
                py.display.flip()
                p_duration = randint(10,30)
                

class Player:
    def __init__(self, x,y,c,w,h):
        self.x = x
        self.y = y
        self.color = c
        self.width = w
        self.height = h
    
    def move(self, m):
        self.x += m*5


h_screen = 800
w_screen = 600
fen = py.display.set_mode((h_screen, w_screen))
base_ground = 9*(w_screen/10)
player = Player((w_screen/5)+20,base_ground-50,(0,255,255),50,50)#x,y,color,w,h
athena = Boss(4*(w_screen/5),base_ground-70,(255,255,255),70,70)#x,y,color,w,h
clock = py.time.Clock()
attack_t = 0

continuer = True

while continuer :
    start_t = py.time.get_ticks()
    fen.fill((150,150,150))
    ground = py.draw.rect(fen,(255,0,255),(0,base_ground,h_screen,w_screen/10))
    py.draw.rect(fen, player.color, (player.x,player.y,player.width,player.height))
    py.draw.rect(fen, athena.color, (athena.x,athena.y,athena.width,athena.height))
    py.display.flip()
    pressed = py.key.get_pressed()
    if pressed[py.K_d]:
        player.move(1)
    elif pressed[py.K_q] :
        player.move(-1)
    if attack_t >= 40 :
        action = randint(1,8)
        if action < 6 :
            athena.attack()
        else:
            athena.parry()
        attack_t = 0
    for event in py.event.get():
        if event.type == py.QUIT:
            continuer = False
    
    end_t = py.time.get_ticks()
    attack_t += end_t - start_t
    clock.tick(60)
