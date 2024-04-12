import pygame as py

class coins :
    
    def __init__(self,val) -> None:
        
        self.coin = val
        
        

        self.explainLst = [py.transform.scale(py.image.load("Elia/Create Level/Assets/PNG/Coins/Acropole.png"), (1920,1080)),
        py.transform.scale(py.image.load("Elia/Create Level/Assets/PNG/Coins/DIONYSOS.png"), (1920,1080)),
        py.transform.scale(py.image.load("Elia/Create Level/Assets/PNG/Coins/olympiéon.png"), (1920,1080))]
        
        
    def show(self, fen) :
        if self.coin == 1 :
            fen.blit(self.explainLst[0],(0,0))
        elif self.coin == 2 :
            fen.blit(self.explainLst[1],(0,0))
        elif self.coin == 3 :
            fen.blit(self.explainLst[2],(0,0))
            
        