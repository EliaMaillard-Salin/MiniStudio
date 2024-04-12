import pygame

class Player:
    
    def __init__(self, posX, posY, width, height):
        
    
        self.saveY = 0
        self.health = 5
        self.posX = posX
        self.posY = posY
        self.width = width 
        self.height = height
        self.isDead = False
        self.onPause = False

        #Player info 
        self.playerVelocity = 300
        self.jumpForce = 600
        self.gravity = 30
        self.verticalVelocity = 0
        self.playerDirection = 0
        self.onGround = False
        self.newGround = 0

        # Action Bools 
        self.isDashing = False
        self.isJumping = False 
        self.isAttacking = False 

        #Dash infos 
        self.dashVelocity = 1000
        self.dashCoolDown = 0
        self.dashDirection = 1

        # Attacks info 
        self.ticksAttack = 0
        self.attackDirection = 0
        
        # Rects for display 

        self.playerRect = pygame.Rect(self.posX,self.posY,self.width,self.height)
        self.weaponRect = pygame.Rect((self.posX + ( self.playerRect.width / 2) ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 100, 30 )

        #img 
        self.imgHeart = pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/ui/coeurVie.png"), (50,50))
        self.imgBrokenHeart = pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/ui/CoeurMort.png"), (47,47))
        self.listHP = [self.imgHeart,self.imgHeart,self.imgHeart,self.imgHeart,self.imgHeart]
        self.dashState = 0
        self.dashStartCoolDown = 60
        self.dashImages = [ pygame.transform.scale( pygame.image.load("PythonFiles/Assets/PNG/ui/marteauDash.png"),  (174,104)  ), 
                            pygame.transform.scale( pygame.image.load("PythonFiles/Assets/PNG/ui/marteauDash3.png"), (174,104)  ), 
                            pygame.transform.scale( pygame.image.load("PythonFiles/Assets/PNG/ui/marteauDash2.png"), (174,104)  ), 
                            pygame.transform.scale( pygame.image.load("PythonFiles/Assets/PNG/ui/marteauDash1.png"), (174,104)  ),
                            pygame.transform.scale( pygame.image.load("PythonFiles/Assets/PNG/ui/marteauDash0.png"), (174,104)  ) ]


    def DisplayPlayer(self, surface, cam): 
        display_rect = pygame.Rect(self.posX - cam.pos_cam_x ,self.posY - cam.pos_cam_y ,self.width,self.height)
        pygame.draw.rect(surface, "white", display_rect)
        if self.isAttacking == True : 
            if pygame.time.get_ticks() - self.ticksAttack >= 0.5*1000 or self.attackDirection != self.playerDirection: 
                self.isAttacking = False 
            else: 
                displayWeapon = pygame.Rect((self.posX + ( display_rect.width / 2) ) - self.playerDirection*100 - cam.pos_cam_x, self.posY+(display_rect.height/4) - cam.pos_cam_y, 100, 30 )
                pygame.draw.rect(surface,"blue", displayWeapon)



    def Attack(self): 
        self.isAttacking = True
        self.ticksAttack = pygame.time.get_ticks()
        self.attackDirection = self.playerDirection

    def LooseOrWinHP(self, updateHP : int): 
        self.listHP = []
        self.health += updateHP
        if self.health == 0: 
            self.isDead = True
        if self.health > 5 :
            self.health = 5 
        for i in range(self.health): 
            self.listHP.append(self.imgHeart)
        if len(self.listHP) < 5 : 
            for i in range( self.health, 5):
                self.listHP.append(self.imgBrokenHeart) 




    def Movement(self, dt) : 
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
    
    def PlayerOnGround(self, Y): 
        if (self.verticalVelocity > 0 ):
            self.posY = Y - self.height
            self.verticalVelocity = 0
            self.isJumping = False  
            self.onGround = False 

    def StopJump(self):
        if(self.isJumping == False):
            return

        self.verticalVelocity = 0
        self.isJumping = False  

    def AttackCollision(self, objectRect):
        if self.isAttacking == True : 
            if (self.playerRect.left + self.playerRect.width >=objectRect.left and 
            self.playerRect.left <=objectRect.left +objectRect.width and
            self.playerRect.top + self.playerRect.height >=objectRect.top and 
            self.playerRect.top <=objectRect.top +objectRect.height):
                return True
            return False
        






        

