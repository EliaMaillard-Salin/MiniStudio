
import pygame

class Camera:
        
    def __init__(self,s_width: int , s_height : int, camvelocity : int):

        self.s_height :int = s_height

        self.onPause : bool = False
        self.pos_cam_x : int = 0
        self.pos_cam_y : int = -30
        
        self.s_camX : int = s_width//2
        self.s_camY : int = (self.s_height//3)*2

        self.camVelocity: int = camvelocity
        self.velocity = 20

        self.limit_left : int = 0
        self.limit_right : int = 6500
        self.limit_top : int = -450
        self.limit_bottom : int = -30


    def CamFollow(self, player , dt :int ) -> None:
        self.s_camY = self.pos_cam_y + (self.s_height//3)*2

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

        if player.posY < self.s_camY and self.pos_cam_y> self.limit_top: 
            self.pos_cam_y -= (self.s_camY - player.posY)* self.velocity * dt

        if player.posY > self.s_camY  and self.pos_cam_y < self.limit_bottom: 
            self.pos_cam_y -= (self.s_camY - player.posY)* self.velocity * dt




