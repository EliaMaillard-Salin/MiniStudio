

import pygame

pygame.init()

class Plateform: 
    def __init__(self,posX,posY,width,height,color): 
        self.Rect = pygame.Rect(posX,posY,width,height)
        self.color = color
    def CreatePlateform(self,plateformeList):
        plateformeList.append(self)
    def Display(self,surface): 
        pygame.draw.rect(surface,self.color,self.Rect)



screen = pygame.display.set_mode((500,500))

running = True 
allPlateforms=[]

Spawn = Plateform(0,450,60,50,"green")
Spawn.CreatePlateform(allPlateforms)

End = Plateform(450,50,60,50,"blue")
End.CreatePlateform(allPlateforms)

while running: 

    screen.fill("grey")
    
    for i in allPlateforms:
        i.Display(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()
