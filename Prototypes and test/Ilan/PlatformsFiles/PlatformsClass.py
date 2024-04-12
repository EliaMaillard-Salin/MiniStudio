
import pygame

class Plateform: 
     
    def __init__(self,posX,posY,width,height,color,solidity): 
        self.solidity = solidity
        self.posX = posX
        self.posY = posY
        self.Rect = pygame.Rect(posX,posY,width,height)
        self.color = color

    def CreatePlateform(self,plateformeList):
        plateformeList.append(self)

    def Display(self, surface, posX = None, posY = None):
        if posX != None and posY != None : 
            self.posX = posX
            self.posY = posY
            surface.blit(self.color, (self.posX,self.posY))
        else:
            pygame.draw.rect(surface,self.color, self.Rect)

    def PlateformCollision(self, Rect):
        # [(x1, y1), (x2, y2), (x3, y3)]
        # if self.color ==  :
            
        if (self.Rect.left + self.Rect.width >= Rect.left and 
            self.Rect.left <= Rect.left + Rect.width and
            self.Rect.top + self.Rect.height >= Rect.bottom - 10  and 
            self.Rect.top <= Rect.top + Rect.height): # Collision avec le sol

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


    def SetMaxValue(self, objectRect, maxvalue : list[int]): 

        if (self.Rect.left + self.Rect.width > objectRect.left) and  (self.Rect.left < objectRect.left + objectRect.width ):
            if (self.Rect.bottom <= objectRect.top): 
                maxvalue[0] = self.Rect.bottom
            else : 
                maxvalue[0] = -1
            if (self.Rect.top >= objectRect.top + objectRect.height): 
                maxvalue[1] = self.Rect.top
            else : 
                maxvalue[1] = -1
        else : 
            maxvalue[0] = -1 ; maxvalue[1] = -1
        if ( self.Rect.top + self.Rect.height > objectRect.top) and (self.Rect.top <  objectRect.top +objectRect.height):
            if(self.Rect.right<= objectRect.left):
                maxvalue[2] = self.Rect.right   
            else : 
                maxvalue[2] = -1
            if (self.Rect.left>= objectRect.right): 
                maxvalue[3] = self.Rect.left   
            else : 
                maxvalue[3] = -1 
        else : 
            maxvalue[2] = -1 ; maxvalue[3] = -1


    def CheckCollision(self, Rect, maxvalue: list[int]): 
        if self.solidity : 
            self.SetMaxValue(Rect, maxvalue)
        else : 
            if self.PlateformCollision(Rect) :
                return True
            return False
        
        return False
    