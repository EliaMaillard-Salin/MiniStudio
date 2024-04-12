
import pygame
import coinsManager

class Props: 
    def __init__(self, hasCollide, isFood, posX, posY, width, height, hasGravity, weight, indxImg, isCoin):
        self.hasCollide = hasCollide
        self.isFood = isFood
        self.isCoin = isCoin
        self.posX = posX
        self.posY = posY
        self.width = width 
        self.height = height
        self.hasGravity = hasGravity
        self.onGround = False
        self.Rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        self.propsImg = [pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/nourriture/bol.png"), (50,50)), 
                         pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/nourriture/bol de tentacules.png"), (50,50)),
                         pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/nourriture/fasolada.png"), (50,50)),
                         pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/nourriture/moussaka.png"), (50,50)),
                         pygame.transform.scale(pygame.image.load("Noa/asset/img/coinsANDexplain/Agora.png"), (50,50)),
                         pygame.transform.scale(pygame.image.load("Noa/asset/img/coinsANDexplain/coinDionysos.png"), (50,50)),
                         pygame.transform.scale(pygame.image.load("Noa/asset/img/coinsANDexplain/coin_Temple_de_Zeus.png"), (50,50))
                        ]
        
        self.img = self.propsImg[indxImg]
        self.index = indxImg
        self.maxValues = [-1,-1,-1,-1, [-1, -1],[-1, -1],[-1, -1],[-1, -1]]
        
        self.dashVelocity = 0
        self.weight = weight        
        self.verticalVelocity = 0
        self.gravity = 0.5 * self.weight
        self.coinReveal = False
        

    def DisplayProp(self,surface, camPos : tuple[int,int]  ): 
        surface.blit(self.img, (self.posX - camPos[0], self.posY - camPos[1] ) )

    def CheckFalling(self, dt):
        if self.hasGravity:
            if self.onGround == False:
                self.verticalVelocity += self.gravity 
                self.posY += self.verticalVelocity * dt

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

    def Collider(self, player): 

        if self.hasCollide and self.PropsGetCollision(player.playerRect) != 3: 
            if player.isDashing == True : 
                self.dashVelocity = (player.dashVelocity / self.weight)
            else: 
                self.dashVelocity = 0

            if ( (self.posY + self.height) >= player.posY) and ( self.posY <=  (player.posY + player.height) ):
                
                if (player.posX + player.width >= self.posX) and (player.posX < self.posX): 
                   self.posX += player.playerVelocity / self.weight + self.dashVelocity
                   player.posX -= self.weight 

                if (player.posX <= (self.posX + self.width)) and ((player.posX + player.width) > self.posX+self.width): 
                    self.posX -= (player.playerVelocity / self.weight) + self.dashVelocity
                    player.posX += self.weight 

        if self.isFood : 
            if self.PropsGetCollision(player.playerRect) != (0,0) :
                player.LooseOrWinHP(1)
                self.isFood = False
                self.img = self.propsImg[0]
                
        if self.isCoin : 
            if self.PropsGetCollision(player.playerRect) != (0,0) :
                self.coinReveal = True
                player.saveY = player.posY

            