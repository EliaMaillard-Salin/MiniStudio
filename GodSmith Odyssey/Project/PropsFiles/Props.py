
import pygame


class Props: 
    def __init__(self, hasCollide : bool , isFood : bool , posX : int, posY : int, width : int, height : int, hasGravity :bool, weight : int, indxImg :bool, isCoin : bool ):
        

        self.spawnX = posX
        self.spawnY = posY
        self.index : int = indxImg
        self.isCoin : bool= isCoin
        self.coinReveal : bool = False
        self.hasCollide : bool = hasCollide
        self.isFood : bool = isFood
        self.posX : int = posX
        self.posY : int = posY
        self.width : int = width 
        self.height : int = height
        self.hasGravity : bool = hasGravity
        self.onGround : bool = False
        self.Rect : pygame.rect.Rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        self.propsImg  : list[pygame.Surface] =   [pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/nourriture/bol.png"), (60,55)), 
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/nourriture/bol de tentacules.png"), (84,60)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/nourriture/fasolada.png"),  (60,55)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/nourriture/moussaka.png"), (60,55)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/Coins/Pièce Agora.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/Coins/Pièce Dionysos.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/Coins/Pièce Temple de Zeus.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/arbre.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/arbre2.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/box.png"), (70,70)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/linge.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/lys.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/nuage1.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/nuage2.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/Statut_Athena.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/Statut_Chouette.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/vaseMotofs.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/vaseSansMotifs.png"), (50,50)),
                                                        pygame.transform.scale(pygame.image.load("GodSmith Odyssey/Project/Assets/PNG/props/vaseSansMotifsFleurs.png"), (50,50)),
                                                    ]  
        
        self.img : pygame.Surface = self.propsImg[self.index]
        
        self.dashVelocity : int = 0
        self.weight :int = weight        
        self.verticalVelocity : int = 0
        self.gravity : int = 30 * self.weight
        

    def DisplayProp(self,surface : pygame.Surface , camPos : tuple[int,int]  ) -> None: 
        surface.blit(self.img, (self.posX - camPos[0], self.posY - camPos[1] ) )

    def CheckFalling(self, dt : int ):
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

    def Collider(self, player, dt : int )  -> None : 

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
                        player.posX = self.posX - player.width - 1

                    if (player.posX <= (self.posX + self.width)) and ((player.posX + player.width) > self.posX+self.width): 
                        self.posX -=  ( (player.playerVelocity / self.weight) + self.dashVelocity ) * dt
                        player.posX = self.posX +self.width + 1

            
        if self.isFood : 
            if self.PropsGetCollision(player.playerRect) != (0,0) :
                player.LooseOrWinHP(1)
                self.isFood = False
                self.img = self.propsImg[0]
        
        if self.isCoin : 
            if self.PropsGetCollision(player.playerRect) != (0,0) :
                self.coinReveal = True
                player.saveY = player.posY
            
     
            