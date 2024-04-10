
import pygame

class Plateform: 
     
    def __init__(self,posX,posY,width,height,color,solidity): 
        self.solidity = solidity
        self.maxValues = [-1,-1,-1,-1, [-1, -1],[-1, -1],[-1, -1],[-1, -1]]
        self.posX = posX
        self.posY = posY        
        self.Rect = pygame.Rect(posX,posY,width,height)
        self.color = color
        self.solidCollide = False

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


    def SetMaxValue(self, objectRect): 
        

        if (self.Rect.left + self.Rect.width > objectRect.left) and  (self.Rect.left < objectRect.left + objectRect.width ):


            if (self.Rect.bottom <= objectRect.top): 
                self.maxValues[0] = self.Rect.bottom
                self.maxValues[6][0] = self.Rect.bottom
                self.maxValues[7][0] = self.Rect.bottom
            
            else : 
                self.maxValues[0] = -1
                self.maxValues[6][0] = -1
                self.maxValues[7][0] = -1

            if (self.Rect.top >= objectRect.top + objectRect.height): 
                self.maxValues[1] = self.Rect.top
                self.maxValues[4][0] = self.Rect.top
                self.maxValues[5][0] = self.Rect.top
            
            else : 
                self.maxValues[1] = -1
                self.maxValues[4][0] = -1
                self.maxValues[5][0] = -1

        else : 

            self.maxValues[0] = -1 ; self.maxValues[1] = -1
            self.maxValues[4][0] = -1 
            self.maxValues[5][0] = -1 
            self.maxValues[6][0] = -1 
            self.maxValues[7][0] = -1 




        if ( self.Rect.top + self.Rect.height > objectRect.top) and (self.Rect.top <  objectRect.top +objectRect.height):

            if(self.Rect.right<= objectRect.left):
                self.maxValues[2] = self.Rect.right  
                self.maxValues[5][1] = self.Rect.right
                self.maxValues[7][1] = self.Rect.right 

            else : 
                self.maxValues[2] = -1
                self.maxValues[5][1] = -1
                self.maxValues[7][1] = -1

            if (self.Rect.left>= objectRect.right): 
                self.maxValues[3] = self.Rect.left 
                self.maxValues[4][1] = self.Rect.left
                self.maxValues[6][1] = self.Rect.left  

            else : 
                self.maxValues[3] = -1 
                self.maxValues[4][1] = -1
                self.maxValues[6][1] = -1


        else : 
            self.maxValues[2] = -1 ; self.maxValues[3] = -1
            self.maxValues[4][1] = -1 
            self.maxValues[5][1] = -1 
            self.maxValues[6][1] = -1 
            self.maxValues[7][1] = -1 


    def CheckWalls(self, objectToCollide): 
    # max value : [ max top, min bottom, min left, max right, top left, top right, bottom left, bottom right]
        setOnGround = False
        if (objectToCollide.posY <= self.maxValues[0] ) and (self.maxValues[0] != -1): 
            objectToCollide.posY = self.maxValues[0]

        if (objectToCollide.posY + objectToCollide.height >= self.maxValues[1] ) and (self.maxValues[1] != -1): 
            objectToCollide.posY = self.maxValues[1] - objectToCollide.height
            setOnGround = True
        if (objectToCollide.posX <= self.maxValues[2] ) and (self.maxValues[2] != -1): 
            objectToCollide.posX = self.maxValues[2]

        if (objectToCollide.posX + objectToCollide.width >= self.maxValues[3] ) and (self.maxValues[3] != -1): 
            objectToCollide.posX = self.maxValues[3] - objectToCollide.width

    #top left
        if (objectToCollide.posX + objectToCollide.width >= self.maxValues[4][1] )and (objectToCollide.posY + objectToCollide.height >= self.maxValues[4][0] )  and (self.maxValues[4][0] != -1) and (self.maxValues[4][1] != -1):
            objectToCollide.posX = self.maxValues[4][1] - objectToCollide.width
            objectToCollide.posY = self.maxValues[4][0] - objectToCollide.height
            setOnGround = True
    #top right
        if (objectToCollide.posX <= self.maxValues[5][1] ) and (objectToCollide.posY + objectToCollide.height  >= self.maxValues[5][0] ) and (self.maxValues[5][0] != -1) and (self.maxValues[5][1] != -1):
            objectToCollide.posX = self.maxValues[5][1]
            objectToCollide.posY = self.maxValues[5][0] - objectToCollide.height 

    #bottom left
        if (objectToCollide.posX + objectToCollide.width >= self.maxValues[6][1] ) and (objectToCollide.posY <= self.maxValues[6][0] ) and (self.maxValues[6][0] != -1) and (self.maxValues[6][1] != -1):
            objectToCollide.posX = self.maxValues[6][1] - objectToCollide.width
            objectToCollide.posY = self.maxValues[6][0]

    #bottom right
        if (objectToCollide.posX <= self.maxValues[7][1] ) and (objectToCollide.posY <= self.maxValues[7][0]) and (self.maxValues[7][0] != -1) and (self.maxValues[7][1] != -1):
            objectToCollide.posX = self.maxValues[7][1]
            objectToCollide.posY = self.maxValues[7][0]
        
        if setOnGround : 
            return True
        else: 
            return False

    def CheckCollision(self, Rect): 
        if self.solidity : 
            self.maxValues = [-1,-1,-1,-1, [-1, -1],[-1, -1],[-1, -1],[-1, -1]]
            self.SetMaxValue(Rect)
        else : 
            if self.PlateformCollision(Rect) :
                return True
            return False
    