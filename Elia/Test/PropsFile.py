
import pygame


class Props: 
    def __init__(self, hasCollide, isFood, posX, posY, width, height, hasGravity, weight, indxImg):
        self.hasCollide = hasCollide
        self.isFood = isFood
        self.posX = posX
        self.posY = posY
        self.width = width 
        self.height = height
        self.hasGravity = hasGravity
        self.onGround = False
        self.Rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        self.propsImg = [pygame.transform.scale(pygame.image.load("Elia/Asset/Props/bol.png"), (90,51)), 
                         pygame.transform.scale(pygame.image.load("Elia/Asset/Props/bol de tentacules.png"), (90,51)),
                         pygame.transform.scale(pygame.image.load("Elia/Asset/Props/fasolada.png"), (50,50)),
                         pygame.transform.scale(pygame.image.load("Elia/Asset/Props/moussaka.png"), (50,50))
                        ]
        
        self.img = self.propsImg[indxImg]
        self.maxValues = [-1,-1,-1,-1, [-1, -1],[-1, -1],[-1, -1],[-1, -1]]
        
        self.dashVelocity = 0
        self.weight = weight        
        self.verticalVelocity = 0
        self.gravity = 0.5 * self.weight
        



    def DisplayProp(self,surface): 
        self.Rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        surface.blit(self.img, (self.posX, self.posY))

    def CheckFalling(self):
        if self.hasGravity:
            if self.onGround == False:
                self.verticalVelocity += self.gravity 
                self.posY += self.verticalVelocity

    def  SetPropMaxValues(self,playerRect):
        
        if (self.Rect.left + self.Rect.width > playerRect.left) and  (self.Rect.left < playerRect.left + playerRect.width ):


            if (self.Rect.bottom <= playerRect.top): 
                self.maxValues[0] = self.Rect.bottom
                self.maxValues[6][0] = self.Rect.bottom
                self.maxValues[7][0] = self.Rect.bottom
            
            else : 
                self.maxValues[0] = -1
                self.maxValues[6][0] = -1
                self.maxValues[7][0] = -1

            if (self.Rect.top >= playerRect.top + playerRect.height): 
                self.maxValues[1] = self.Rect.top
                self.maxValues[4][0] = self.Rect.top
                self.maxValues[5][0] = self.Rect.top
            
            else : 
                self.maxValues[1] = -1
                self.maxValues[4][0] = -1
                self.maxValues[5][0] = -1

        else : 

            self.maxValues[0] = -1 ; self.maxValues[1] = -1
            self.maxValues[4][0] = -1 
            self.maxValues[5][0] = -1 
            self.maxValues[6][0] = -1 
            self.maxValues[7][0] = -1 




        if ( self.Rect.top + self.Rect.height > playerRect.top) and (self.Rect.top <  playerRect.top +playerRect.height):

            if(self.Rect.right<= playerRect.left):
                self.maxValues[2] = self.Rect.right  
                self.maxValues[5][1] = self.Rect.right
                self.maxValues[7][1] = self.Rect.right 

            else : 
                self.maxValues[2] = -1
                self.maxValues[5][1] = -1
                self.maxValues[7][1] = -1

            if (self.Rect.left>= playerRect.right): 
                self.maxValues[3] = self.Rect.left 
                self.maxValues[4][1] = self.Rect.left
                self.maxValues[6][1] = self.Rect.left  

            else : 
                self.maxValues[3] = -1 
                self.maxValues[4][1] = -1
                self.maxValues[6][1] = -1


        else : 
            self.maxValues[2] = -1 ; self.maxValues[3] = -1
            self.maxValues[4][1] = -1 
            self.maxValues[5][1] = -1 
            self.maxValues[6][1] = -1 
            self.maxValues[7][1] = -1 
    

    def CheckPropWall(self, player):
        
        setOnGround = False
        if (player.posY <= self.maxValues[0] ) and (self.maxValues[0] != -1): 
            player.posY = self.maxValues[0]

        if (player.posY + player.height >= self.maxValues[1] ) and (self.maxValues[1] != -1): 
            player.posY = self.maxValues[1] - player.height
            setOnGround = True
        if (player.posX <= self.maxValues[2] ) and (self.maxValues[2] != -1): 
            player.posX = self.maxValues[2]

        if (player.posX + player.width >= self.maxValues[3] ) and (self.maxValues[3] != -1): 
            player.posX = self.maxValues[3] - player.width

    #top left
        if (player.posX + player.width >= self.maxValues[4][1] )and (player.posY + player.height >= self.maxValues[4][0] )  and (self.maxValues[4][0] != -1) and (self.maxValues[4][1] != -1):
            player.posX = self.maxValues[4][1] - player.width
            player.posY = self.maxValues[4][0] - player.height
            setOnGround = True
    #top right
        if (player.posX <= self.maxValues[5][1] ) and (player.posY + player.height  >= self.maxValues[5][0] ) and (self.maxValues[5][0] != -1) and (self.maxValues[5][1] != -1):
            player.posX = self.maxValues[5][1]
            player.posY = self.maxValues[5][0] - player.height 

    #bottom left
        if (player.posX + player.width >= self.maxValues[6][1] ) and (player.posY <= self.maxValues[6][0] ) and (self.maxValues[6][0] != -1) and (self.maxValues[6][1] != -1):
            player.posX = self.maxValues[6][1] - player.width
            player.posY = self.maxValues[6][0]

    #bottom right
        if (player.posX <= self.maxValues[7][1] ) and (player.posY <= self.maxValues[7][0]) and (self.maxValues[7][0] != -1) and (self.maxValues[7][1] != -1):
            player.posX = self.maxValues[7][1]
            player.posY = self.maxValues[7][0]
        
        if setOnGround : 
            return True
        else: 
            return False
    
    
    def CollisionOnNoCollider(self, player):
        if (player.posX + player.width >=self.posX and 
            player.posX <=self.posX +self.width and
            player.posY + player.height >=self.posY and 
            player.posY <=self.posY +self.height):
            return True
        return False   


    def Collider(self, player): 

        Ontop = False
        self.SetPropMaxValues(player.playerRect)

        if self.hasCollide and not self.CheckPropWall(player): 
            if player.isDashing == True : 
                self.dashVelocity = (player.dashVelocity / self.weight)
            else: 
                self.dashVelocity = 0
            if ( (self.posY + self.height) >= player.posY) and ( self.posY <=  (player.posY + player.height) ) and not Ontop:
                
                if (player.posX + player.width >= self.posX) and (player.posX < self.posX): 
                   self.posX += player.playerVelocity / self.weight + self.dashVelocity
                   player.posX -= self.weight 

                if (player.posX <= (self.posX + self.width)) and ((player.posX + player.width) > self.posX+self.width): 
                    self.posX -= (player.playerVelocity / self.weight) + self.dashVelocity
                    player.posX += self.weight 
        elif self.hasCollide :
            player.PlayerOnGround(self.posY)

        if self.isFood : 
            if(self.CollisionOnNoCollider(player) ) :
                player.LooseOrWinHP(1)
                self.isFood = False
                self.img = self.propsImg[0]
            
     
            