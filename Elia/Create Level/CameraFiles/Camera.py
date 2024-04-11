
import pygame

class Camera:
        
    def __init__(self,s_width, s_height, camvelocity):

        self.onPause : bool = False
        self.pos_cam_x : int = 0
        self.pos_cam_y : int = - 50
        
        self.s_camX : int = s_width//2
        self.s_camY : int = s_height//3

        self.camVelocity: int = camvelocity

        self.limit_left : int = 0
        self.limit_right : int = 8000
        self.limit_top : int = -800
        self.limit_bottom : int = -50 + s_height


    def CamFollow(self, player , dt :int ) -> None:
        
        if self.onPause == True : 
            return

        dashValue = 0
        if player.isDashing == True : 
            dashValue = player.dashVelocity
        ispressed = pygame.key.get_pressed()

        if ispressed[pygame.K_d] and self.pos_cam_x < self.limit_right and player.posX >= self.s_camX :
            
            self.pos_cam_x += ( self.camVelocity + dashValue ) * dt 
            self.s_camX += ( self.camVelocity + dashValue ) * dt 


        if ispressed[pygame.K_q] and  self.pos_cam_x > self.limit_left and player.posX <= self.s_camX :

            self.pos_cam_x -=  ( self.camVelocity + dashValue ) * dt 
            self.s_camX -= ( self.camVelocity + dashValue ) * dt


