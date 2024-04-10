
import pygame

class Camera:
        
    def __init__(self,s_width, s_height, camvelocity):

 
        self.pos_cam_x : int = 0
        self.pos_cam_y : int = 0
        
        self.s_camX : int = s_width//2
        self.s_camY : int = s_height//3

        self.camVelocity: int = camvelocity

        self.limit_left : int = 0
        self.limit_right : int = 3200
        self.limit_top : int = -700
        self.limit_bottom : int = s_height//4


    def CamFollow(self, player , dt :int ) -> None:


        ispressed = pygame.key.get_pressed()

        if ispressed[pygame.K_d] and self.pos_cam_x < self.limit_right and player.posX >= self.s_camX :
            
            self.pos_cam_x += self.camVelocity * dt
            self.s_camX += self.camVelocity * dt


        if ispressed[pygame.K_q] and  self.pos_cam_x > self.limit_left and player.posX <= self.s_camX :

            self.pos_cam_x -=  self.camVelocity * dt
            self.s_camX -= self.camVelocity * dt


