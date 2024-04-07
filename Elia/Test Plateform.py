
import pygame
from PlayerMovement import *

pygame.init()


class Plateform: 
    def __init__(self,posX,posY,width,height,color,solidity,isImg): 
        self.posX = posX
        self.posY = posY
        self.isImg = isImg
        self.plateformImage = pygame.image.load("Elia/img/Fichier_7.png").convert_alpha()
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
    




screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

running = True

player = Player(300,200,50,50)

ground  = pygame.Rect(0,400,500,100)


allPlateforms=[]



P1 = Plateform(300, 475, 200, 20, "green",True, "img/Sol simple.png")
P1.CreatePlateform(allPlateforms)

P2 = Plateform(0, 305, 200, 20, "green",True, "img/Sol simple.png")
P2.CreatePlateform(allPlateforms)

P3 = Plateform(500, 400, 200, 20, "green",True, "img/Sol simple.png")
P3.CreatePlateform(allPlateforms)

P4 = Plateform(200, 330, 200, 20, "green",False, "img/Sol simple.png")
P4.CreatePlateform(allPlateforms)






while running: 

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not player.isJumping:
                player.isJumping = True
                player.verticalVelocity = -player.jumpForce

    player.Movement()

    for i in allPlateforms: 
        if(i.CheckCollision(player.playerRect)):
            player.PlayerOnGround(i.Rect.top) 

  

    # Affichage
    screen.fill("black")

    for i in allPlateforms:
        i.Display(screen)

    player.UpdatePlayer(screen)
    
    pygame.display.update()


pygame.quit() 








if player.posY > screen_height + player.height: 
        player.posX = 300
        player.posY = 400
        player.onGround = True