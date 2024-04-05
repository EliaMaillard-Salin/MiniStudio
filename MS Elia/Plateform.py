
import pygame

class Plateform: 
    def __init__(self,posX,posY,width,height,color,solidity,isImg): 
        self.posX = posX
        self.posY = posY
        self.isImg = isImg
        self.plateformImage = pygame.image.load("img/Fichier_7.png").convert_alpha()
        self.plateformImage = pygame.transform.scale(self.plateformImage, (width,screen_height - height))
        
        self.solid = solidity
        self.Rect = pygame.Rect(posX,posY,width,height)
        self.color = color
        self.Ground = pygame.Rect(posX + 1 , posY - 1, width - 2 , 1)

    def CreatePlateform(self,plateformeList):
        plateformeList.append(self)

    def Display(self,surface): 
        if self.isImg:
            surface.blit(self.plateformImage, (self.posX,self.posY))
        else : 
            pygame.draw.rect(surface,self.color, self.Rect)
        pygame.draw.rect(surface,"red",self.Ground)

    def PlateformCollision(self, Rect):
        if (self.Ground.left + self.Ground.width >= Rect.left and
            self.Ground.left <= Rect.left + Rect.width and
            self.Ground.top + self.Ground.height >= Rect.bottom - 10  and 
            self.Ground.top <= Rect.top + Rect.height): #Collision avec le sol  
            return True
        return False


    def CheckCollision(self, Rect): 
        if self.PlateformCollision(Rect) :
                return True
        return False
    