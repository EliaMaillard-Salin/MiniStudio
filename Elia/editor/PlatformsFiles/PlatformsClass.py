
import pygame
import sys

class Plateform: 
     
    def __init__(self,posX : int ,posY : int ,width : int ,height : int, color : str | None , texture : pygame.Surface | None , solidity : bool ): 
        self.solidity : bool = solidity
        self.posX : int  = posX
        self.posY : int = posY   
        self.width : int = width
        self.height : int = height     
        self.Rect : pygame.Rect = pygame.Rect(posX,posY,width,height)
        self.color : str | None = color
        self.img : pygame.Surface | None = texture



    def CreatePlateform(self, plateformeList : list ) -> None:
        plateformeList.append(self)

    def Display(self,surface : pygame.Surface , camPos : tuple[int,int]) -> None: 
        if self.color != None: 
            display_rect = pygame.Rect(self.posX - camPos[0], self.posY - camPos[1], self.width, self.height )
            pygame.draw.rect(surface,self.color, display_rect)
        if self.img != None : 
            surface.blit(self.img, (self.posX - camPos[0], self.posY - camPos[1]))


    def GetCollision(self, rect: pygame.rect.Rect) -> tuple[int, int]:
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


