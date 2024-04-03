

import pygame

class Plateform: 
    def __init__(self,posX,posY,width,height,color): 
        self.Rect = pygame.Rect(posX,posY,width,height)
        self.color = color
    def Display(self,surface): 
        pygame.draw.rect(surface,self.color,self.Rect)

    