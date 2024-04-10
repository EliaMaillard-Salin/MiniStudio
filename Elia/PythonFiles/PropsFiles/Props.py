
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
        self.propsImg = [pygame.transform.scale(pygame.image.load("Elia/Asset/Props/bol.png"), (60,55)), 
                         pygame.transform.scale(pygame.image.load("Elia/Asset/Props/bol de tentacules.png"), (85,60)),
                         pygame.transform.scale(pygame.image.load("Elia/Asset/Props/fasolada.png"),  (60,55)),
                         pygame.transform.scale(pygame.image.load("Elia/Asset/Props/moussaka.png"),  (60,55))
                        ]
        
        self.img = self.propsImg[indxImg]
        self.maxValues = [-1,-1,-1,-1, [-1, -1],[-1, -1],[-1, -1],[-1, -1]]
        
        self.dashVelocity = 0
        self.weight = weight        
        self.verticalVelocity = 0
        self.gravity = 30 * self.weight
        

    def DisplayProp(self,surface, camPos : tuple[int,int]  ): 
        surface.blit(self.img, (self.posX - camPos[0], self.posY - camPos[1] ) )

    def CheckFalling(self, dt):
        if self.hasGravity:
            if self.onGround == False:
                self.verticalVelocity += self.gravity 
                self.posY += self.verticalVelocity * dt
        self.Rect = pygame.Rect(self.posX, self.posY, self.width, self.height)

    def PropsGetCollision(self, rect: pygame.rect.Rect) -> tuple[int, int]:
        #0 => None
        #1 => Left
        #2 => Right
        #3 => Top
        #4 => Bottom 

        if rect.right < self.Rect.left:
            return 0, 0
        
        if rect.left > self.Rect.right:
            return 0, 0
        
        if rect.top > self.Rect.bottom:
            return 0, 0
        
        if rect.bottom < self.Rect.top:
            return 0, 0

        distances: list[int] = []
        distances.append(abs(rect.right - self.Rect.left))
        distances.append(abs(rect.left - self.Rect.right))
        distances.append(abs(rect.bottom - self.Rect.top))
        distances.append(abs(rect.top - self.Rect.bottom))

        minDistance = 2000
        side: int = 0
        for i in range(0, len(distances)):
            if minDistance > distances[i]:
                minDistance = distances[i]
                side = i + 1
        
        return side, minDistance

    def Collider(self, player, dt): 

        if self.hasCollide : 
            if self.PropsGetCollision(player.playerRect)[0] == 3:
                player.PlayerOnGround(self.posY)
            elif self.PropsGetCollision(player.playerRect)[0] != 0: 
                if player.isDashing == True : 
                        self.dashVelocity = (player.dashVelocity / self.weight)
                else: 
                    self.dashVelocity = 0

                if ( (self.posY + self.height) >= player.posY) and ( self.posY <=  (player.posY + player.height) ):
                    
                    if (player.posX + player.width >= self.posX) and (player.posX < self.posX): 
                        self.posX +=  ( player.playerVelocity / self.weight + self.dashVelocity ) * dt
                        player.posX -= self.weight * dt

                    if (player.posX <= (self.posX + self.width)) and ((player.posX + player.width) > self.posX+self.width): 
                        self.posX -=  ( (player.playerVelocity / self.weight) + self.dashVelocity ) * dt
                        player.posX += self.weight * dt

            
        if self.isFood : 
            if self.PropsGetCollision(player.playerRect) != (0,0) :
                player.LooseOrWinHP(1)
                self.isFood = False
                self.img = self.propsImg[0]
            
     
            