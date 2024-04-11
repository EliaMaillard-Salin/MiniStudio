import pygame
import PlatformsClass

class Buildings : 
    def __init__(self, X : int, Y : int, indx : int ): 
        self.posX : int = X 
        self.posY : int = Y 
        self.indx :int = indx

        self.allImages : list[pygame.Surface] = [
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Blocking Maison/Maison_carré.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Blocking Maison/Maison_carré_Double.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Blocking Maison/Maison_Carré_Haute.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Blocking Maison/Maison_Ronde.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Blocking Maison/Maison_Ronde_fenetre.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison 2 étages couleur/Maison_2étages_barrière.png"), 
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison 2 étages couleur/Maison_2étages_coloré_final_rouge.png"),           
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison 2 étages couleur/Maison_2étages_coloré_final.png"),  
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison Champignon/Maison_champignon_final.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison Champignon/Maison_champignon_final_rouge.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison Tour 2 étages/Maison_Tour_barriere.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison Tour 2 étages/Maison_Tour_final.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison Tour 2 étages/Maison_Tour_Rouge.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison arriere plan/hutteGrandecopie 2.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison arriere plan/Maison_Tour copie.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Maison arriere plan/maisonCarreGrande copie 2.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Pillier/Pillier.png"),
            pygame.load("PythonFiles/Assets/PNG/Asset Bâtiment/Temple_final.png"),
        ]
    
        self.allInfos : list[list[int]] = [
            

        ]