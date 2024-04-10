
import pygame
import sys

class Plateform: 
     
    def __init__(self,posX,posY,width,height,color,solidity): 
        self.solidity = solidity
        self.posX = posX
        self.posY = posY   
        self.width = width
        self.height = height     
        self.Rect = pygame.Rect(posX,posY,width,height)
        self.color = color



    def CreatePlateform(self,plateformeList):
        plateformeList.append(self)

    def Display(self,surface, camPos : tuple[int,int]): 
        display_rect = pygame.Rect(self.posX - camPos[0], self.posY - camPos[1], self.width, self.height )
        pygame.draw.rect(surface,self.color, display_rect)


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


