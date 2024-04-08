
import pygame

class Plateform: 
    def __init__(self,posX,posY,width,height,color): 
        self.posX = posX
        self.posY = posY  
        self.width = width
        self.height = height      
        self.Rect = pygame.Rect(posX,posY,width,height)
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
    

    def PlateformMove(self,cam,player ):
        if cam.oldPosX < cam.pos_cam_x and cam.pos_cam_x < cam.limit_right: 
            self.posX -= player.playerVelocity
        if cam.oldPosX > cam.pos_cam_x and cam.pos_cam_x > cam.limit_left:
            self.posX += player.playerVelocity

        if cam.oldPosY < cam.pos_cam_y :
            self.posY -= cam.pos_cam_y - cam.oldPosY
        if cam.oldPosY > cam.pos_cam_y : 
            self.posY += cam.oldPosY - cam.pos_cam_y

        self.Rect = pygame.Rect(self.posX,self.posY,self.width,self.height)

    def CheckCollision(self, Rect): 
        if self.PlateformCollision(Rect) :
                return True
        return False
    