from random import *


class Boss:
    def __init__(self, x,y,c,w,h,p):
        #Athena
        self.x = x
        self.y = y
        self.color = c
        self.width = w
        self.height = h
        self.size_img = [0,0]
        self.pos_img = [0,0]
        self.size_onde = [0,0]
        self.pos_onde = [0,0]

        #Movement
        self.velocity = 1
        self.jumpForce = 10
        self.gravity = 0.5
        self.verticalVelocity = 0
        self.maxPosY = 0
        self.x_goal = self.x_goal = randint(0,int(self.x))

        #Weapon 
        self.x_weapon = self.x + (self.width/2)
        self.y_weapon = self.y + (self.height/2)
        self.range_weapon = 250
        self.w_weapon = 50
        self.base_w_weapon = 200
        self.h_weapon = 20

        #Shield
        self.w_shield = 10
        self.h_shield = h + 10

        #Aoe
        self.w_shockwave = 40
        self.h_shockwave = 20
        self.shockwave_y = self.y + self.height -self.h_shockwave
        self.shockwave_l_x = self.x-self.w_shockwave
        self.shockwave_r_x = self.x+self.width

        #Player
        self.player = p

        #Condition
        self.time_attack = 0
        self.time_walk = 0
        self.provoc_status = False
        self.movement = True
        self.status_aoe = False
        self.status_attack = False
        self.status_damage = True
        self.isJumping = False
        self.onGround = False
        self.launch_aoe = True

        #Animations
        self.walk = ["Flo/AnimAthena/Anim Marche/Marche 1 sur 2.png", "Flo/AnimAthena/Anim Marche/Marche 2 sur 2.png"]
        self.walk_nb = 0
        self.attack_anim = ["Flo/AnimAthena/Anim Attaque/Pose Début.png","Flo/AnimAthena/Anim Attaque/Préparation Attaque.png",
                            "Flo/AnimAthena/Anim Attaque/Attaque 1 sur 2.png","Flo/AnimAthena/Anim Attaque/Attaque 2 sur 2.png",
                            "Flo/AnimAthena/Anim Attaque/Pose Fin.png"]
        self.attack_nb = 0
        self.parry_anim = ["Flo/AnimAthena/Anim Contre/Garde.png"]
        self.parry_nb = 0
        self.aoe_anim = ["Flo/AnimAthena/Anim Onde/Lancé 1 sur 3.png",
                         "Flo/AnimAthena/Anim Onde/Lancé 2 sur 3.png","Flo/AnimAthena/Anim Onde/Lancé 3 sur 3.png",
                         "Flo/AnimAthena/Anim Onde/Onde 1 sur 5.png","Flo/AnimAthena/Anim Onde/Onde 2 sur 5.png",
                         "Flo/AnimAthena/Anim Onde/Onde 3 sur 5.png","Flo/AnimAthena/Anim Onde/Onde 4 sur 5.png",
                         "Flo/AnimAthena/Anim Onde/Onde 5 sur 5.png","Flo/AnimAthena/Anim Onde/Récup 1 sur 5.png",
                         "Flo/AnimAthena/Anim Onde/Récup 2 sur 5.png","Flo/AnimAthena/Anim Onde/Récup 3 sur 5.png",
                         "Flo/AnimAthena/Anim Onde/Récup 4 sur 5.png","Flo/AnimAthena/Anim Onde/Récup 5 sur 5.png",]
        self.aoe_nb = 0
        self.idle_anim = ["Flo/AnimAthena/Anim Idle/Stand 1.png","Flo/AnimAthena/Anim Idle/Stand 2.png"]
        self.idle_nb = 0
        self.idle_time = 0
        self.provoc_anim = ["Flo/AnimAthena/Anim Provoc/Provoc 1 sur 2.png","Flo/AnimAthena/Anim Provoc/Provoc 2 sur 2.png"]
        self.provoc_nb = -1
        self.provoc_time = 0
        self.onde_anim = ["Flo/AnimAthena/Effet Onde/Effet 1 sur 2.png","Flo/AnimAthena/Effet Onde/Effet 2 sur 2.png"]
        self.onde_nb = 0
        self.all_anim = [self.walk, self.attack_anim, self.parry_anim, self.aoe_anim, self.idle_anim, self.provoc_anim, self.onde_anim]
        
    def choose_goal(self):
        if randint(1,2) == 1 :
            self.x_goal = randint(0,int(self.x))
        else:
            self.x_goal = randint(int(self.x)+self.width,1920-self.width)

    def move(self):
        if self.x > self.x_goal :
            self.x -= self.velocity
        elif self.x + self.width < self.x_goal:
            self.x += self.velocity
        else :
            self.choose_goal()
        self.x_weapon = self.x + (self.width/2)
        if self.isJumping :
            self.verticalVelocity += self.gravity
            self.y += self.verticalVelocity

        if (self.y <= self.maxPosY): 
            self.y = self.maxPosY
        
        self.shockwave_l_x = self.x-self.w_shockwave
        self.shockwave_r_x = self.x+self.width
        self.x_weapon = self.x + (self.width/2)
        self.y_weapon = self.y + (self.height/2)
    
    def jump(self):
        if not self.isJumping:
                self.isJumping = True
                self.verticalVelocity = -self.jumpForce

    def collide_attack(self,object):
        if (self.x_weapon+ self.base_w_weapon >= object.left and 
            self.x_weapon <= object.right and
            self.y_weapon <= object.bottom  and 
            self.y_weapon + self.h_weapon >= object.top):  
            return True
        return False
    
    def collide_aoe(self,object):
        if (self.shockwave_l_x+ self.w_shockwave >= object.left and 
            self.shockwave_l_x <= object.right and
            self.shockwave_y <= object.bottom  and 
            self.shockwave_y + self.h_shockwave >= object.top) or (self.shockwave_r_x+ self.w_shockwave >= object.left and 
            self.shockwave_r_x <= object.right and
            self.shockwave_y <= object.bottom  and 
            self.shockwave_y + self.h_shockwave >= object.top):  
            return True
        return False

    def attack(self) :
        self.status_attack = True
        self.movement = False
        
        r = (self.range_weapon-(self.w_weapon//2))+1
        if self.x > self.player.posX :
            if self.w_weapon < r :
                self.w_weapon+=24
            else :
                self.w_weapon = self.base_w_weapon
                self.movement = True
                self.status_attack = False
        else :
            if self.w_weapon < r :
                self.w_weapon+=24
            else :
                self.w_weapon = 50
                self.movement = True
                self.status_attack = False
        if self.attack_nb < len(self.attack_anim)-1 :
            self.attack_nb += 1
        else : 
            self.attack_nb = 0
        

    def attack_aoe(self):
        self.status_aoe = True
        self.movement = False
        min_x = 0
        max_x = 1920
        if self.aoe_nb >= 0 and self.launch_aoe:
            if self.aoe_nb < len(self.aoe_anim) :
                self.aoe_nb += 1
            else :
                self.launch_aoe = False
        if (self.shockwave_l_x >= min_x or self.shockwave_r_x <= max_x) and self.aoe_nb >= 3:
            self.shockwave_l_x -= self.w_shockwave
            self.shockwave_r_x += self.w_shockwave
            if self.onde_nb == 0 :
                self.onde_nb += 1
            else :
                self.onde_nb -=1
        elif (self.shockwave_l_x <= min_x or self.shockwave_r_x >= max_x):
            self.aoe_nb = 0
            self.status_aoe = False
            self.movement = True
            self.launch_aoe = True

    def parry(self):
        if self.parry_nb < len(self.parry_anim):
            self.parry_nb += 1
        else:
            self.parry_nb = 0
            self.movement = True

    def BossOnGround(self, Y): 
        if (self.verticalVelocity > 0 ):
            self.y = Y - self.height
            self.verticalVelocity = 0
            self.isJumping = False  
            self.onGround = True
            
    
    def pattern_boss(self):
        if self.status_aoe == True :
            self.attack_aoe()
            return None
        else :
            self.shockwave_l_x = self.x-self.w_shockwave
            self.shockwave_r_x = self.x+self.width
        if self.status_attack :
            self.attack()
            
            return None
        if self.parry_nb == 0:
            action = randint(1,8)
            self.status_damage = True
            if action > 5 and self.isJumping == False:
                self.parry()
                self.movement = False
            else:
                if randint(1,3) == 1 and self.isJumping == False:
                    self.attack_aoe()
                else : 
                    self.attack()
        else :
            self.parry()
        
    def active_provoc(self):
        if self.provoc_nb < len(self.provoc_anim)-1:
            self.provoc_nb += 1
    
    def active_idle(self):
        if self.idle_nb == 0 :
            self.idle_nb += 1
        else :
            self.idle_nb -= 1