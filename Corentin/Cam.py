import pygame
import PlayerMovement 
import Plateform

"""
Manque à verifier avec le DeltaTime
"""

#Screen dimention
s_width : int = 1600
s_height : int = 900

ongoing : bool = True

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()

#Color
gray : tuple = (150, 150, 150)
red : tuple = (255, 0, 0)
blue : tuple = (0, 0, 255)
green : tuple = (0, 255, 0)

#Player parameter

player_p = pygame.image.load("Pictures/Test.png")

#Element parametter
plateform = Plateform.Plateform(0, 0, 0, 0, gray)

allPlateforme = []

P1 = Plateform.Plateform(800, 400, 40, 100, "red")
P1.CreatePlateform(allPlateforme)

P2 = Plateform.Plateform(400, 40, 35, 120, "blue")
P2.CreatePlateform(allPlateforme)

P3 = Plateform.Plateform(0, 800, 1600, 120, "green")
P3.CreatePlateform(allPlateforme)

# Set the camera
class Camera:
        
    def __init__(self):

        self.camera_offset_x : int = 0
        self.camera_offset_y : int = 0

        self.pos_cam_x : int = s_width//2
        self.pos_cam_y : int = s_height//4

        
        self.oldPosX : int = s_width//2
        self.oldPosY : int = s_height//4


        self.camVelocity = 5
        self.camDirection = 0




        self.limit_left : int = 0
        self.limit_right : int = 3200
        self.limit_top : int = -700
        self.limit_bottom : int = s_height//4

    def CamFollow(self, player):
        ispressed = pygame.key.get_pressed()

        if ispressed[pygame.K_d] and self.pos_cam_x < self.limit_right:
            self.pos_cam_x += self.camVelocity
            self.camera_offset_x -= self.camVelocity

        if ispressed[pygame.K_q] and  self.pos_cam_x > self.limit_left:
            self.pos_cam_x -=  self.camVelocity
            cam.camera_offset_x +=  self.camVelocity

        if player.posY < self.pos_cam_y  and  self.pos_cam_y > self.limit_top: 
            self.pos_cam_y += player.verticalVelocity
        if player.posY > self.pos_cam_y  and  self.pos_cam_y < self.limit_bottom: 
            self.pos_cam_y  += player.verticalVelocity
        

cam = Camera()

player = PlayerMovement.Player(10, 600, 32, 32)

#Game
while ongoing:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ongoing = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not player.isJumping: 
                player.isJumping == True
                player.verticalVelocity = -player.jumpForce


    player.Movement()

    for i in allPlateforme:
        if(i.CheckCollision(player.playerRect)):
            player.PlayerOnGround(i.Rect.top)

    cam.CamFollow(player)



    
    screen.fill(gray)

    for i in allPlateforme:
        i.PlateformMove(cam,player)
        i.Display(screen)

    player.DisplayPlayer(screen)
    

    
    cam.oldPosX = cam.pos_cam_x
    cam.oldPosY = cam.pos_cam_y

    pygame.display.flip()



pygame.quit()
