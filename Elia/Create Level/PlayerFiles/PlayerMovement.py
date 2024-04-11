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
        self.weaponRect : pygame.rect.Rect = pygame.Rect((self.posX + ( self.playerRect.width / 2) ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 100, 30 )

        #img 
        self.imgHeart :  pygame.Surface = pygame.transform.scale(pygame.image.load("Elia/Create Level/Assets/PNG/ui/coeurVie.png"), (45,45))
        self.imgBrokenHeart :  pygame.Surface = pygame.transform.scale(pygame.image.load("Elia/Create Level/Assets/PNG/ui/CoeurMort.png"), (40,40))

        self.listHP : list[ pygame.Surface] = [self.imgHeart,self.imgHeart,self.imgHeart]
        #self.listHP[-1] = pygame.transform.scale(self.listHP[-1], (50,50))
        self.dashState : int = 0
        self.dashStartCoolDown : int = 60
        self.dashImages : list[ pygame.Surface] = [pygame.transform.scale( pygame.image.load("Elia/Create Level/Assets/PNG/ui/marteauDash.png"),  (140,82)  ), 
                                                        pygame.transform.scale( pygame.image.load("Elia/Create Level/Assets/PNG/ui/marteauDash3.png"), (140,82)  ), 
                                                        pygame.transform.scale( pygame.image.load("Elia/Create Level/Assets/PNG/ui/marteauDash2.png"), (140,82)  ), 
                                                        pygame.transform.scale( pygame.image.load("Elia/Create Level/Assets/PNG/ui/marteauDash1.png"), (140,82)  ),
                                                        pygame.transform.scale( pygame.image.load("Elia/Create Level/Assets/PNG/ui/marteauDash0.png"), (140,82)  ) ]
        self.playerIcon : pygame.Surface = pygame.image.load("Elia/Create Level/Assets/PNG/ui/Tete Vie Andonis.png")



    def DisplayPlayer(self, surface: pygame.Surface , cam ) -> None : 
        display_rect : pygame.rect.Rect = pygame.Rect(self.posX - cam.pos_cam_x ,self.posY - cam.pos_cam_y ,self.width,self.height)
        pygame.draw.rect(surface, "white", display_rect)
        if self.isAttacking == True : 
            if pygame.time.get_ticks() - self.ticksAttack >= 0.5*1000 or self.attackDirection != self.playerDirection: 
                self.isAttacking = False 
            else: 
                displayWeapon : pygame.rect.Rect = pygame.Rect((self.posX + ( display_rect.width / 2) ) - self.playerDirection*100 - cam.pos_cam_x, self.posY+(display_rect.height/4) - cam.pos_cam_y, 100, 30 )
                pygame.draw.rect(surface,"blue", displayWeapon)



    def Attack(self) -> None : 
        self.isAttacking = True
        self.ticksAttack = pygame.time.get_ticks()
        self.attackDirection = self.playerDirection

    def LooseOrWinHP(self, updateHP : int): 
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




    def Movement(self, dt : int) -> None: 
        if self.onPause == True : 
            return

        keys = pygame.key.get_pressed()
        
    # Gestion du dash
        if keys[pygame.K_LSHIFT] and not self.isDashing and self.dashCoolDown <= 0:
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
            self.posX += self.dashDirection * self.dashVelocity * dt
            self.dashCoolDown -= 1
            if self.dashCoolDown <= 50:
                self.isDashing = False

        if not self.isDashing:

            # Déplacement horizontal
            if keys[pygame.K_q]:
                self.posX -= self.playerVelocity  * dt
                self.playerDirection = 1
            if keys[pygame.K_d]:
                self.playerDirection = 0
                self.posX += self.playerVelocity * dt

        # Appliquer la gravité
        

        self.verticalVelocity += self.gravity 
        self.posY += self.verticalVelocity * dt
        
        if not self.isDashing:
            self.dashCoolDown -= 1  

        if self.dashCoolDown > 0: 
            if self.dashCoolDown <=  (self.dashStartCoolDown/4) * self.dashState: 
                self.dashState -= 1


        self.playerRect = pygame.Rect(self.posX,self.posY,self.width,self.height)
        self.weaponRect = pygame.Rect((self.posX + ( self.playerRect.width / 2) ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 100, 30 )
    
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
        






        

