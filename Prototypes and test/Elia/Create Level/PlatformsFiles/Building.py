import pygame
from . import PlatformsClass

class Buildings : 
    def __init__(self, X : int, Y : int, indx : int): 
        self.posX : int = X 
        self.posY : int = Y 
        self.indx :int = indx
        self.barrierePosY : int = 175
        self.placeBarrer : bool = False


        self.plateformsCoor : list[list[PlatformsClass.Plateform]] = [
            [PlatformsClass.Plateform(self.posX + 20, self.posY,175,14,None,None,False)],
            [PlatformsClass.Plateform(self.posX + 20, self.posY,169,13,None,None,False), PlatformsClass.Plateform(self.posX,self.posY + 123,195,10,None,None,False)],
            [PlatformsClass.Plateform(self.posX, self.posY + 107, 195, 8, None,None,False), PlatformsClass.Plateform(self.posX + 20, self.posY,169,13,None,None,False)],
            [PlatformsClass.Plateform(self.posX, self.posY + 117, 195, 10, None,None,False)],
            [PlatformsClass.Plateform(self.posX, self.posY + 110, 215, 10, None ,None,False)],
            [PlatformsClass.Plateform(self.posX, self.posY + 116, 215, 9, None ,None,False), PlatformsClass.Plateform(self.posX , self.posY + 211, 215, 9, None,None,True)],
            [PlatformsClass.Plateform(self.posX, self.posY + 116, 215, 9, None ,None,False), PlatformsClass.Plateform(self.posX , self.posY + 211, 215, 9, None,None,True)],
            [PlatformsClass.Plateform(self.posX + 9, self.posY + 123, 196, 11, None,None,False)],
            [PlatformsClass.Plateform(self.posX + 9, self.posY + 123, 196, 11, None,None,False)],
            [PlatformsClass.Plateform(self.posX + 24, self.posY  + 334, 209, 18, None,None,False), PlatformsClass.Plateform(self.posX, self.posY + 525, 257, 15, None,None,True)],
            [PlatformsClass.Plateform(self.posX + 24, self.posY  + 334, 209, 18, None,None,False), PlatformsClass.Plateform(self.posX, self.posY + 525, 257, 15, None,None,True)],
            [],
            [],
            [],  
            [PlatformsClass.Plateform(self.posX, self.posY, 155, 15, None,None,False)],
            [PlatformsClass.Plateform(self.posX + 15 ,  self.posY + 546, 1020, 30, None,None,False)]
        ]

        self.allImages : list[pygame.Surface] = [
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Blocking Maison/Maison_carré.png"),(195,222)),
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Blocking Maison/Maison_carré_Double.png"),(195,222)),
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Blocking Maison/Maison_Carré_Haute.png"),(195,222)),
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Blocking Maison/Maison_Ronde.png"),(195,222)), 
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Blocking Maison/Maison_Ronde_fenetre.png"),(215,245)), 
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison 2 étages couleur/Maison_2étages_coloré_final_rouge.png"),(215,335)),        
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison 2 étages couleur/Maison_2étages_coloré_final.png"), (215,335)),
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison Champignon/Maison_champignon_final.png"), (215,273)), 
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison Champignon/Maison_champignon_final_rouge.png"), (215,273)),
            pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison Tour 2 étages/Maison_Tour_final.png"),
            pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison Tour 2 étages/Maison_Tour_Rouge.png"),
            pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maisons arriere plan/hutteGrande copie 2.png"),
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maisons arriere plan/Maison_Tour copie.png"), (166,400)),
            pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maisons arriere plan/maisonCarreGrande copie 2.png"), 
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Pillier/Pillier.png"),(155,400)), 
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Temple/Temple_final.png"), (1050,700)),
        ]

        self.barriereImg : list[pygame.Surface] = [
            pygame.transform.scale(pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison 2 étages couleur/Maison_2étages_barrière.png"),(218,39)), 
            pygame.image.load("PythonFiles/Assets/PNG/Asset Batiment/Maison Tour 2 étages/Maison_Tour_barriere.png"),
        ]
    
    def PlaceBuilding(self, platforms : list[PlatformsClass.Plateform]): 
        if self.indx == 5 or self.indx == 6 or self.indx == 9 or self.indx == 10 : 
            self.placeBarrer = True
        self.img = self.allImages[self.indx]
        if self.plateformsCoor[self.indx] == []:
            return
        else : 
            for i in self.plateformsCoor[self.indx]: 
               i.CreatePlateform(platforms)

    def DrawBuilding(self, surface : pygame.Surface, camPos : tuple[int,int] ):
        surface.blit(self.allImages[self.indx], (self.posX - camPos[0],self.posY - camPos[1]))

    def DrawBarrer(self, surface : pygame.Surface , camPos : tuple[int,int]):
        if self.indx == 5 or self.indx == 6:
            surface.blit(self.barriereImg[0], (self.posX - camPos[0] ,self.posY + self.barrierePosY - camPos[1]))
        elif self.indx == 9 or self.indx == 10 :
            surface.blit(self.barriereImg[1], (self.posX - camPos[0] ,self.posY - camPos[1] ))
