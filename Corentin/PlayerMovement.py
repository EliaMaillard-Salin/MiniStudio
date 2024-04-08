
import pygame

class Player:
    def __init__(self, posX, posY, width, height):

        self.posX = posX
        self.posY = posY
        self.width = width 
        self.height = height

        #Player info 
        self.playerVelocity = 5
        self.jumpForce = 10
        self.gravity = 0.5
        self.verticalVelocity = 0
        self.playerDirection = 0
        self.onGround = False
        self.newGround = 0
        self.maxPosY = 0

        # Action Bools 
        self.isDashing = False
        self.isJumping = False 
        self.isAttacking = False 

        #Dash infos 
        self.dashVelocity = 20
        self.dashCooldown = 0
        self.dashDirection = 1

        # Attacks info 
        self.ticksAttack = 0
        self.attackDirection = 0
        
        # Rects for display 
        self.playerRect = pygame.Rect(self.posX,self.posY,self.width,self.height)
        self.weaponRect = pygame.Rect((self.posX + ( self.playerRect.width / 2) ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 100, 30 )

    def DisplayPlayer(self, surface): 
        self.playerRect = pygame.Rect(self.posX,self.posY,self.width,self.height)
        pygame.draw.rect(surface, "white", self.playerRect)
        if self.isAttacking == True : 
            if pygame.time.get_ticks() - self.ticksAttack >= 0.5*1000 or self.attackDirection != self.playerDirection: 
                self.isAttacking = False 
            else: 
                self.weaponRect = pygame.Rect((self.posX + ( self.playerRect.width / 2) ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 100, 30 )
                pygame.draw.rect(surface,"blue", self.weaponRect)

    def Attack(self): 
        self.isAttacking = True
        self.ticksAttack = pygame.time.get_ticks()
        self.attackDirection = self.playerDirection

    def Movement(self): 

        if pygame.mouse.get_pressed()[0]: 
            self.Attack()
        keys = pygame.key.get_pressed()
    # Gestion du dash
        if keys[pygame.K_LSHIFT] and not self.isDashing and self.dashCooldown <= 0:
            self.isDashing = True
            self.dashCooldown = 60
            self.dashDirection = 0
            if keys[pygame.K_q]:
                self.dashDirection = -1
            elif keys[pygame.K_d]:
                self.dashDirection = 1
            else: 
                self.isDashing = False
                self.dashCooldown = 0


        if self.isDashing:
            self.posX += self.dashDirection * self.dashVelocity
            self.dashCooldown -= 1
            if self.dashCooldown <= 50:
                self.isDashing = False

        if not self.isDashing:

            # Déplacement horizontal
            if keys[pygame.K_q]:
                self.posX -= self.playerVelocity
                self.playerDirection = 1
            if keys[pygame.K_d]:
                self.playerDirection = 0
                self.posX += self.playerVelocity

        # Appliquer la gravité
        

        self.verticalVelocity += self.gravity
        self.posY += self.verticalVelocity


        if not self.isDashing:
            self.dashCooldown -= 1  
    
    def PlayerOnGround(self, Y): 
        if (self.verticalVelocity > 0 ):
            self.posY = Y - self.height
            self.verticalVelocity = 0
            self.isJumping = False  
            self.onGround = False 





        

