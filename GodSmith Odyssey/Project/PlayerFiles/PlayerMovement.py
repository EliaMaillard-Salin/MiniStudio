import pygame

class Player:
    def __init__(self, posX : int , posY : int, width : int, height : int):


        self.saveY : int  = 0
        self.onPause : bool = False
        self.maxHealth :int = 3
        self.health : int = 3
        self.posX: int = posX
        self.posY : int = posY
        self.width : int = width 
        self.height : int = height
        self.isDead : bool = False

        #Player info 
        self.playerVelocity : int = 300
        self.jumpForce : int = 800
        self.gravity : int = 30
        self.verticalVelocity : int = 0
        self.playerDirection : int = 0
        self.onGround : bool = False
        self.immortality : bool = False 
        self.startImmortality : int = 0
        self.getHit = False

        self.dash_time = 0
        self.jump_time = 0
        self.PauseIdle = 0
        self.PauseMove = 0
        self.timeWalk = 0
        self.hurt = 0
        self.attack_time = 0
        self.death = 0
        self.playwalk = False
        self.playdash = False
        self.playjump = False
        self.playattack = False
        

        # Action Bools 
        self.isDashing : bool = False
        self.isJumping  :bool = False 
        self.isAttacking :bool = False 

        #Dash infos 
        self.dashVelocity : int = 1300
        self.dashCoolDown : int = 0
        self.dashDirection : int = 1

        # Attacks info 
        self.ticksAttack : int = 0
        self.attackDirection : int = 0
        
        # Rects for display 

        self.playerRect : pygame.rect.Rect = pygame.Rect(self.posX,self.posY,self.width,self.height)
        self.weaponRect : pygame.rect.Rect = pygame.Rect(-11111,-11111,10,10)

        #img 
        self.imgHeart :  pygame.Surface = pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/coeurVie.png"), (45,45))
        self.imgBrokenHeart :  pygame.Surface = pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/CoeurMort.png"), (40,40))

        self.listHP : list[ pygame.Surface] = [self.imgHeart,self.imgHeart,self.imgHeart]
        #self.listHP[-1] = pygame.transform.scale(self.listHP[-1], (50,50))
        self.dashState : int = 0
        self.dashStartCoolDown : int = 60
        self.dashImages : list[ pygame.Surface] = [pygame.transform.scale( pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/marteauDash.png"),  (140,82)  ), 
                                                        pygame.transform.scale( pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/marteauDash3.png"), (140,82)  ), 
                                                        pygame.transform.scale( pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/marteauDash2.png"), (140,82)  ), 
                                                        pygame.transform.scale( pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/marteauDash1.png"), (140,82)  ),
                                                        pygame.transform.scale( pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/marteauDash0.png"), (140,82)  ) 
                                                    ]
        
        self.playerIcon : pygame.Surface = pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/ui/Tete Vie Andonis.png")

        self.playeridle = ['GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0001.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0002.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0003.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0004.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0005.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0006.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0007.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0008.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0009.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0010.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0011.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0012.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0013.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0014.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0015.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0016.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0017.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0018.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0019.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Idle/Idle0020.png',]
        self.playeridle_nb = 0
        
        self.playerwalk = ['GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0001.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0002.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0003.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0004.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0005.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0006.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0007.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0008.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0009.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Marche/Marche0010.png',]
        self.playerwalk_nb = 0
        self.playerwalk_nb_save = 0

        
        self.playerdash = ['GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30001.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30002.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30003.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30004.png',
                          'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30005.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30006.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30007.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30008.png',
                          'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30009.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30010.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30011.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30012.png',
                          'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30013.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30014.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30015.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30016.png',
                          'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30017.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30018.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30019.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30020.png',
                          'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30021.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30022.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30023.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30024.png',
                          'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30025.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30026.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30027.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dash/Sans nom-30028.png']
        self.playerdash_nb = 0  
        
        self.playerjump = ['GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0001.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0002.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0003.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0004.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0005.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0006.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0007.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0008.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0009.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0010.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0011.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0012.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0013.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0014.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0015.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0016.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0017.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0018.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0019.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0020.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0021.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Saut/Saut0022.png',]
        self.playerjump_nb = 0
        
        self.playerattack = ['GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0001.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0002.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0003.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0004.png',
                             'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0005.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0006.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0007.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0008.png',
                             'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0009.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0010.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0011.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0012.png',
                             'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0013.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0014.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Attaque/Attaque0015.png',]
        self.playerattack_nb = 0
        
        self.playerhurt = ['GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0001.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0002.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0003.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0004.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0005.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0006.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0007.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0008.png',
                           'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0009.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0010.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0011.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/Dégat subit/Anim dégat subis0012.png',]
        self.playerhurt_nb = 0
        
        self.playerdeath = ['GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0001.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0002.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0003.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0004.png',
                            'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0005.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0006.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0007.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0008.png',
                            'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0009.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0010.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0011.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0012.png',
                            'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0013.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0014.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0015.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0016.png',
                            'GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0017.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0018.png','GodSmith Odyssey/Project/Assets/PNG/Animations/Player/KO/KO0019.png',]
        self.playerdeath_nb = 0
        
        self.huddeath = ['GodSmith Odyssey/Project/Assets/PNG/ui/ded.png']
        
        self.all_anim : list[list[str]] = [self.playerdash,self.playeridle,self.playerwalk,self.playerjump, self.playerattack,self.playerhurt,self.playerdeath,self.huddeath]

        self.imganim : list[list[pygame.Surface]]= []

            # Load les images 
    def load_anim_player(self):
        for elt in self.all_anim:
            newAmin : list[pygame.Surface] = []
            for i in range(len(elt)):
                newAmin.append(pygame.image.load(elt[i]))
            self.imganim.append(newAmin)
            
        # Animation Dash  
    def Dash(self,fen : pygame.Surface, camPos : tuple[int,int]):
            if self.dashDirection == -1:
                walk = pygame.transform.flip(pygame.transform.scale(self.imganim[0][self.playerdash_nb],(self.width + 180,self.height + 40)), True,False)
                fen.blit(walk,(self.posX - 85 - camPos[0],self.posY - 20- camPos[1]))
            elif self.dashDirection == 1:
                walk = pygame.transform.scale(self.imganim[0][self.playerdash_nb],(self.width + 180,self.height + 40))
                fen.blit(walk,(self.posX - 95- camPos[0],self.posY - 20- camPos[1]))
                 
       # Animation Idle         
    def Idle(self, fen: pygame.Surface, camPos : tuple[int,int]):     
        if self.playerDirection == 1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[1][self.playeridle_nb],(self.width + 220,self.height + 60)), True,False)
            fen.blit(walk,(self.posX - 105- camPos[0],self.posY - 35- camPos[1]))
        elif self.playerDirection == 0:
            walk = pygame.transform.scale(self.imganim[1][self.playeridle_nb],(self.width + 220,self.height + 60))
            fen.blit(walk,(self.posX - 115- camPos[0],self.posY - 35- camPos[1])) 
        
        # Animation Marche
    def PlayerWalk(self,fen: pygame.Surface, camPos : tuple[int,int]): 
        if self.playerDirection == 1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[2][self.playerwalk_nb],(self.width + 220,self.height + 60)), True,False)
            fen.blit(walk,(self.posX - 105- camPos[0],self.posY - 35- camPos[1]))
        elif self.playerDirection == 0:
            walk = pygame.transform.scale(self.imganim[2][self.playerwalk_nb],(self.width + 220,self.height + 60))
            fen.blit(walk,(self.posX - 115- camPos[0],self.posY - 35- camPos[1])) 
            
        # Animation Jump
    def PlayerJump(self,fen: pygame.Surface, camPos : tuple[int,int]) :
        if self.playerDirection == 1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[3][self.playerjump_nb],(self.width + 220,self.height + 60)), True,False)
            fen.blit(walk,(self.posX - 105- camPos[0],self.posY - 35- camPos[1]))
        elif self.playerDirection == 0:
            walk = pygame.transform.scale(self.imganim[3][self.playerjump_nb],(self.width + 220,self.height + 60))
            fen.blit(walk,(self.posX - 115- camPos[0],self.posY - 35- camPos[1])) 
            
        # Animation attack
    def PlayerAttack(self,fen: pygame.Surface, camPos : tuple[int,int]):
        if self.playerDirection == 1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[4][self.playerattack_nb],(self.width + 220,self.height + 60)), True,False)
            fen.blit(walk,(self.posX - 105 - camPos[0] ,self.posY - 35 - camPos[1]))
        elif self.playerDirection == 0:
            walk = pygame.transform.scale(self.imganim[4][self.playerattack_nb],(self.width + 220,self.height + 60))
            fen.blit(walk,(self.posX - 115 - camPos[0] ,self.posY - 35 - camPos[1])) 
            
        # Animation de dégats
    def PlayerHurt(self,fen: pygame.Surface, camPos : tuple[int,int]):
        if self.playerDirection == 1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[5][self.playerhurt_nb],(self.width + 220,self.height + 60)), True,False)
            fen.blit(walk,(self.posX - 105 - camPos[0] ,self.posY - 35 - camPos[1]))
        elif self.playerDirection == 0:
            walk = pygame.transform.scale(self.imganim[5][self.playerhurt_nb],(self.width + 220,self.height + 60))
            fen.blit(walk,(self.posX - 115 - camPos[0] ,self.posY - 35 - camPos[1]))
            
        # Animation de KO    
    def PlayerDeath(self,fen: pygame.Surface, camPos : tuple[int,int]) :
        if self.playerDirection == 1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[6][self.playerdeath_nb],(self.width + 220,self.height + 60)), True,False)
            fen.blit(walk,(self.posX - 105 - camPos[0],self.posY - 35- camPos[1] ))
        elif self.playerDirection == 0:
            walk = pygame.transform.scale(self.imganim[6][self.playerdeath_nb],(self.width + 220,self.height + 60))
            fen.blit(walk,(self.posX - 115  - camPos[0],self.posY - 35 - camPos[1]))
            
            
    def HUDdeath(self,fen):
            walk = pygame.transform.scale(self.imganim[7][0],(800,600))
            fen.blit(walk,(0,25))
        

        # Print Hitbox of player 
    def DisplayPlayer(self, surface): 
        self.playerRect = pygame.Rect(self.posX,self.posY,self.width,self.height)
        #pygame.draw.rect(surface, "blue", self.playerRect)
        if self.isAttacking == True : 
            if pygame.time.get_ticks() - self.ticksAttack >= 0.5*1000 or self.attackDirection != self.playerDirection: 
                self.isAttacking = False 
            else: 
                self.weaponRect = pygame.Rect((self.posX + ( self.playerRect.width / 2) + 20 ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 60, 30 )
                #pygame.draw.rect(surface,"purple", self.weaponRect)



    def DisplayPlayer(self, surface: pygame.Surface , cam ) -> None : 
        display_rect : pygame.rect.Rect = pygame.Rect(self.posX - cam.pos_cam_x ,self.posY - cam.pos_cam_y ,self.width,self.height)
        #pygame.draw.rect(surface, "white", display_rect)
        if self.isAttacking == True : 
            if pygame.time.get_ticks() - self.ticksAttack >= 0.5*1000 or self.attackDirection != self.playerDirection: 
                self.isAttacking = False 
                self.weaponRect : pygame.rect.Rect = pygame.Rect(-11111,-11111,10,10)
            else: 
                displayWeapon : pygame.rect.Rect = pygame.Rect((self.posX + ( display_rect.width / 2) ) - self.playerDirection*100 - cam.pos_cam_x, self.posY+(display_rect.height/4) - cam.pos_cam_y, 100, 30 )
                #pygame.draw.rect(surface,"blue", displayWeapon)


    def Attack(self) -> None : 
        self.weaponRect = pygame.Rect((self.posX + ( self.playerRect.width / 2) + 20 ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 60, 30 )        
        self.playattack = True
        self.isAttacking = True
        self.ticksAttack = pygame.time.get_ticks()
        self.attackDirection = self.playerDirection

    def LooseOrWinHP(self, updateHP : int) -> None: 
        if updateHP == -1: 
            if self.immortality == True :
                return
            else:         
                self.immortality = True
                self.startImmortality = pygame.time.get_ticks()
        self.listHP: list [pygame.Surface] = []
        self.health += updateHP
        if self.health == 0: 
            self.isDead = True
        if self.health > self.maxHealth :
            self.health = self.maxHealth 
        for i in range(self.health): 
            self.listHP.append(self.imgHeart)
        #self.listHP[-1] = pygame.transform.scale(self.listHP[-1], (60,60))
        if len(self.listHP) < self.maxHealth : 
            for i in range( self.health, self.maxHealth):
                self.listHP.append(self.imgBrokenHeart) 




    def Movement(self) -> None: 
        if self.onPause == True : 
            return

        keys = pygame.key.get_pressed()
        
    # Gestion du dash
        if keys[pygame.K_LSHIFT] and not self.isDashing and self.dashCoolDown <= 0:
            self.playdash = True
            self.isDashing = True
            self.dashState = 4
            self.dashCoolDown = 60
            self.dashDirection = 0
            if keys[pygame.K_q]:
                self.dashDirection = -1
            elif keys[pygame.K_d]:
                self.dashDirection = 1
            else: 
                self.isDashing = False
                self.dashCoolDown = 0
                self.dashState = 0


        if self.isDashing:
            self.immortality = True
            self.posX += self.dashDirection * self.dashVelocity 
            self.dashCoolDown -= 1
            if self.dashCoolDown <= 50:
                self.isDashing = False

        if not self.isDashing:

            # Déplacement horizontal
            if keys[pygame.K_q]:
                self.playwalk = True      
                self.posX -= self.playerVelocity  
                self.playerDirection = 1
                self.PauseIdle = 1
            if keys[pygame.K_d]:
                self.playwalk = True      
                self.playerDirection = 0
                self.posX += self.playerVelocity 
                self.PauseIdle = 1

        # Appliquer la gravité
        

        self.verticalVelocity += self.gravity 
        self.posY += self.verticalVelocity 
        
        if not self.isDashing:
            self.immortality =False
            self.dashCoolDown -= 1  

        if self.dashCoolDown > 0: 
            if self.dashCoolDown <=  (self.dashStartCoolDown/4) * self.dashState: 
                self.dashState -= 1


        self.playerRect = pygame.Rect(self.posX,self.posY,self.width,self.height)
    
    def PlayerOnGround(self, Y : int) -> None: 
        if (self.verticalVelocity > 0 ):
            self.posY = Y - self.height
            self.verticalVelocity = 0
            self.isJumping = False  
            self.onGround = False 

    def StopJump(self) -> None:
        if(self.isJumping == False):
            return

        self.verticalVelocity = 0
        self.isJumping = False  

    def AttackCollision(self, objectRect : pygame.rect.Rect ) -> bool:
        if self.isAttacking == True : 
            if (self.playerRect.left + self.playerRect.width >=objectRect.left and 
            self.playerRect.left <=objectRect.left +objectRect.width and
            self.playerRect.top + self.playerRect.height >=objectRect.top and 
            self.playerRect.top <=objectRect.top +objectRect.height):
                return True
            return False
        return False
        






        

