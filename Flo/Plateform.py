
import pygame

class Plateform: 
    def __init__(self,posX,posY,width,height,color): 
        self.posX = posX
        self.posY = posY    
        self.width = width
        self.height = height    
        self.Rect = pygame.Rect(posX,posY,self.width,self.height)
        self.color = color

    def CreatePlateform(self,plateformeList):
        plateformeList.append(self)

    def Display(self,surface): 
        pygame.draw.rect(surface,self.color, self.Rect)

    def PlateformCollision(self, Rect):
        if (self.Rect.left + self.Rect.width >= Rect.left and 
            self.Rect.left <= Rect.left + Rect.width and
            self.Rect.top + self.Rect.height >= Rect.bottom - 10  and 
            self.Rect.top <= Rect.top + Rect.height): #Collision avec le sol  
            return True
        return False

    def update(self, screenPos : tuple[int,int], screenSize : tuple[int,int]):
        self.posX = screenPos[0]
        self.posY = screenPos[1]
        self.width = screenSize[0]
        self.height = screenSize[1]    
        self.Rect = pygame.Rect(self.posX,self.posY,self.width,self.height)

    def CheckCollision(self, Rect): 
        if self.PlateformCollision(Rect) :
                return True
        return False
    