import pygame

class Player:
    def __init__(self, posX : int , posY : int, width : int, height : int):

        self.saveY : int  = 0
        self.onPause : bool = False
        self.health : int = 5
        self.posX: int = posX
        self.posY : int = posY
        self.width : int = width 
        self.height : int = height
        self.isDead : bool = False

        #Player info 
        self.playerVelocity : int = 300
        self.jumpForce : int = 600
        self.gravity : int = 30
        self.verticalVelocity : int = 0
        self.playerDirection : int = 0
        self.onGround : bool = False

        # Action Bools 
        self.isStanding : bool = True
        self.isDashing : bool = False
        self.isJumping  :bool = False 
        self.isAttacking :bool = False 
        
        # Key info
        self.prev_key = pygame.key.get_pressed()

        #Dash infos
        self.dash_cycle = [pygame.transform.scale(pygame.image.load(f"Ilan\Create Level\Assets\PNG\Anim Dash\{i}.png"), (54, 93)) for i in range(1, 10)]
        self.dash_animation_index = 0
        self.dash_animation_timer = 0
        self.dash_animation_delay = 30  # Adjust the delay to control the animation speed
        self.dashVelocity : int = 1000
        self.dashCoolDown : int = 0
        self.dashDirection : int = 1

        # Attacks info
        self.ticksAttack : int = 0
        self.attackDirection : int = 0
        self.attack_cycle = [pygame.transform.scale(pygame.image.load(f"Ilan\Create Level\Assets\PNG\Anim Attaque\Attaque{i}.png"), (154,262)) for i in range(1, 16)]
        self.attack_animation_index = 0
        self.attack_animation_timer = 0
        self.attack_animation_delay = 10  # Adjust the delay to control the animation speed
        
        # Rects for display
        self.playerRect : pygame.rect.Rect = pygame.Rect(self.posX,self.posY,self.width,self.height)
        self.weaponRect : pygame.rect.Rect = pygame.Rect((self.posX + ( self.playerRect.width / 2) ) - self.playerDirection*100, self.posY+(self.playerRect.height/4), 100, 30 )

        #img 
        self.imgHeart :  pygame.Surface = pygame.transform.scale(pygame.image.load("Elia/Test/Asset/UI/coeurVie.png"), (50,50))
        self.imgBrokenHeart :  pygame.Surface = pygame.transform.scale(pygame.image.load("Elia/Test/Asset/UI/CoeurMort.png"), (47,47))
        self.listHP : list[ pygame.Surface] = [self.imgHeart,self.imgHeart,self.imgHeart,self.imgHeart,self.imgHeart]
        self.dashState : int = 0
        self.dashStartCoolDown : int = 60
        self.dashImages : list[ pygame.Surface] = [pygame.transform.scale( pygame.image.load("Elia/Test/Asset/UI/marteauDash.png"),  (174,104)  ), 
                                                        pygame.transform.scale( pygame.image.load("Elia/Test/Asset/UI/marteauDash3.png"), (174,104)  ), 
                                                        pygame.transform.scale( pygame.image.load("Elia/Test/Asset/UI/marteauDash2.png"), (174,104)  ), 
                                                        pygame.transform.scale( pygame.image.load("Elia/Test/Asset/UI/marteauDash1.png"), (174,104)  ),
                                                        pygame.transform.scale( pygame.image.load("Elia/Test/Asset/UI/marteauDash0.png"), (174,104)  ) ]
        # Stand cycle
        self.stand_cycle = [pygame.transform.scale(pygame.image.load(f"Ilan/Create Level/Assets/PNG/Anim Idle/Stand {i}.png"), (54,93)) for i in range(1,3)]
        self.stand_animation_index = 0
        self.stand_animation_timer = 0
        self.stand_animation_delay = 17  # Adjust the delay to control the animation speed
        
        # Walk cycle
        self.walk_cycle = [pygame.transform.scale(pygame.image.load(f"Ilan/Create Level/Assets/PNG/Anim Marche/Marche {i}.png"), (54, 93)) for i in range(1, 3)]
        self.walk_animation_index = 0
        self.walk_animation_timer = 0
        self.walk_animation_delay = 17  # Adjust the delay to control the animation speed
        
        # Jump cycle
        self.jump_cycle = pygame.transform.scale(pygame.image.load("Ilan/Create Level/Assets/PNG/Anim Saut/Jump.png"), (54, 93))
        

    def DisplayPlayer(self, surface: pygame.Surface , cam ) -> None : 
        display_rect: pygame.rect.Rect = pygame.Rect(self.posX - cam.pos_cam_x, self.posY - cam.pos_cam_y, self.width, self.height)

        # Jump animation
        if self.isJumping:
            if self.playerDirection == 0:  # Right
                surface.blit(self.jump_cycle, display_rect)
            if self.playerDirection == 1:  # Left
                surface.blit(pygame.transform.flip(self.jump_cycle, True, False), display_rect)

        if not self.isJumping:
            # Walk animation
            if not self.isStanding:
                if self.walk_animation_index < len(self.walk_cycle):
                    if self.playerDirection == 0: # Right
                        surface.blit(self.walk_cycle[self.walk_animation_index], display_rect)
                    if self.playerDirection == 1: # Left
                        surface.blit(pygame.transform.flip(self.walk_cycle[self.walk_animation_index], True, False), display_rect)
            # Stand animation
            if self.isStanding:
                if self.stand_animation_index < len(self.stand_cycle):
                        if self.playerDirection == 0:  # Right
                            surface.blit(self.stand_cycle[self.stand_animation_index], display_rect)
                        if self.playerDirection == 1:  # Left
                            surface.blit(pygame.transform.flip(self.stand_cycle[self.stand_animation_index], True, False), display_rect)
        # Attacking animation
        if self.isAttacking == True : 
            if pygame.time.get_ticks() - self.ticksAttack >= 0.5*1000 or self.attackDirection != self.playerDirection: 
                self.isAttacking = False 
            else: 
                displayWeapon : pygame.rect.Rect = pygame.Rect((self.posX + ( display_rect.width / 2) ) - self.playerDirection*100 - cam.pos_cam_x, self.posY+(display_rect.height/4) - cam.pos_cam_y, 100, 30 )
                # pygame.draw.rect(surface,"blue", displayWeapon)
                if self.attack_animation_index < len(self.attack_cycle):
                    if self.playerDirection == 0: # Right
                        surface.blit(self.attack_cycle[self.attack_animation_index], display_rect)
                    if self.playerDirection == 1: # Left
                        surface.blit(pygame.transform.flip(self.attack_cycle[self.attack_animation_index], True, False), display_rect)
        
        # Dash animation
        if self.isDashing:
            if self.dashState < len(self.dash_cycle):
                if self.playerDirection == 0:  # Right
                    surface.blit(self.dash_cycle[self.dashState], display_rect)
                if self.playerDirection == 1:  # Left
                    surface.blit(pygame.transform.flip(self.dash_cycle[self.dashState], True, False), display_rect)

    def animate_walk(self):
        self.walk_animation_timer += 1
        if self.walk_animation_timer >= self.walk_animation_delay:
            self.walk_animation_timer = 0
            self.walk_animation_index += 1
            if self.walk_animation_index >= len(self.walk_cycle):
                self.walk_animation_index = 0

    def animate_stand(self):
        self.stand_animation_timer += 1
        if self.stand_animation_timer >= self.stand_animation_delay:
            self.stand_animation_timer = 0
            self.stand_animation_index += 1
            if self.stand_animation_index >= len(self.stand_cycle):
                self.stand_animation_index = 0
    
    def animate_dash(self):
        self.dash_animation_timer += 1
        if self.dash_animation_timer >= self.dash_animation_delay:
            self.dash_animation_timer = 0
            self.dash_animation_index += 1
            if self.dash_animation_index >= len(self.dash_cycle):
                self.dash_animation_index = 0
    
    def animate_attack(self):
        self.attack_animation_timer += 1
        if self.attack_animation_timer >= self.attack_animation_delay:
            self.attack_animation_timer = 0
            self.attack_animation_index += 1
            if self.attack_animation_index >= len(self.attack_cycle):
                self.attack_animation_index = 0

    def Attack(self) -> None : 
        self.isAttacking = True
        self.ticksAttack = pygame.time.get_ticks()
        self.attackDirection = self.playerDirection

    def LooseOrWinHP(self, updateHP : int): 
        self.listHP: list [pygame.Surface] = []
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


    def Movement(self, dt : int) -> None: 
        if self.onPause == True : 
            return

        keys = pygame.key.get_pressed()
        
        # Gestion du dash
        if keys[pygame.K_LSHIFT] and not self.isDashing and self.dashCoolDown <= 0:
            self.animate_dash()
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
                self.isStanding = False
                self.playerDirection = 1
                self.animate_walk()
                self.posX -= self.playerVelocity * dt
            if keys[pygame.K_d]:
                self.isStanding = False
                self.playerDirection = 0
                self.animate_walk()
                self.posX += self.playerVelocity * dt
            if not keys[pygame.K_q] and not keys[pygame.K_d]:
                self.isStanding = True
                self.animate_stand()

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
        






        

