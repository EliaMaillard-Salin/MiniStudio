import pygame

class Bot:
    def __init__(self, posX, posY, width, height):
        self.posX = posX
        self.posY = posY
        self.Width = width
        self.Height = height


        # Bot Info
        self.BotVelocity = 1

        # Bot Checkpoint Info
        self.Check = [(50,550,20,20)]
        self.Check1 = [(750,550,20,20)]
        self.Checkpoint1 = True
        self.Checkpoint2 = False

        # Rects for display 
        self.BotRect = pygame.Rect(self.posX,self.posY,self.Width,self.Height)

    def MovementBot(self):

        if self.Checkpoint1 :
            self.posX -= self.BotVelocity
        if self.Checkpoint2 :
            self.posX += self.BotVelocity
    
    def DisplayBot(self, surface): 
        self.BotRect = pygame.Rect(self.posX,self.posY,self.Width,self.Height)
        pygame.draw.rect(surface, "blue", self.BotRect)

    def DisplayCheckBot(self,surface):
        self.CheckRect = pygame.Rect((50,550,20,20))
        #pygame.draw.rect(surface, (0,0,0), (50,550,20,20))
        self.Check1Rect = pygame.Rect((750,550,20,20))
        #pygame.draw.rect(surface, (0,0,0), (750,550,20,20))

    def BotOnGround(self, Y): 
            if (self.verticalVelocity > 0 ):
                self.posY = Y - self.Height
                self.verticalVelocity = 0 
                self.onGround = False 

    def CheckCollision(self):
        # Vérifier la collision avec le checkpoint 1 pour bot
        for self.Plateforms in self.Check:
            check_rect = pygame.Rect(50,550,20,20)
            if self.BotRect.colliderect(check_rect):
                self.Checkpoint1 = False
                self.Checkpoint2 = True


                
        # Vérifier la collision avec le checkpoint 1 pour bot
        for self.Plateform in self.Check1:
            check_rect = pygame.Rect(750,550,20,20)
            if self.BotRect.colliderect(check_rect):
                self.Checkpoint2 = False
                self.Checkpoint1 = True

