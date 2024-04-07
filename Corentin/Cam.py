import pygame

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
picture_perso = pygame.image.load("Pictures/Test.png")

pos_x : int = 10                    # pos x et y du joueur
pos_y : int = 600

gravity_y : int = 1
jump_height : int = 20

velocity_x : int = 10               #vitesse de déplacement
velocity_y : int = jump_height

jumping : bool = False

#Element parametter
rect_1 = pygame.Rect(800, 400, 40, 100)
rect_2 = pygame.Rect(400, 40, 35, 120)
rect_3 = pygame.Rect(0, 700, 1600, 120)

# Set the camera
class Camera:
        
    def __init__(self):

        self.camera_offset_x : int = 0
        self.camera_offset_y : int = 0

        self.pos_cam_x : int = s_width//2
        self.pos_cam_y : int = s_height//2

        self.limit_left : int = 0
        self.limit_right : int = 3200
        self.limit_top : int = -200
        self.limit_bottom : int = 1100

cam = Camera()

#Game
while ongoing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ongoing = False

        #Element display
        screen.fill(gray)
        rect_1_draw_pos = rect_1.move(cam.camera_offset_x, cam.camera_offset_y)
        pygame.draw.rect(screen, red, rect_1_draw_pos)
        rect_2_draw_pos = rect_2.move(cam.camera_offset_x, cam.camera_offset_y)
        pygame.draw.rect(screen, blue, rect_2_draw_pos)
        rect_3_draw_pos = rect_3.move(cam.camera_offset_x, cam.camera_offset_y)
        pygame.draw.rect(screen, green, rect_3_draw_pos)

        screen.blit(picture_perso, (pos_x+cam.camera_offset_x, pos_y+cam.camera_offset_y))

        #Mouvement
        ispressed = pygame.key.get_pressed()

        #Mouvement to right
        if ispressed[pygame.K_d] and pos_x < (cam.limit_right+s_width//4):
            pos_x += velocity_x
            if pos_x >= cam.pos_cam_x and cam.pos_cam_x < cam.limit_right: 
                cam.camera_offset_x -= velocity_x
                cam.pos_cam_x += velocity_x

        #Mouvement to left
        if ispressed[pygame.K_q] and pos_x > (cam.limit_left-s_width//2):
            pos_x -= velocity_x
            if pos_x <= cam.pos_cam_x and cam.pos_cam_x > cam.limit_left:
                cam.camera_offset_x += velocity_x
                cam.pos_cam_x -= velocity_x

        #Mouvement up and down ----> à adapter avec le joueur 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and cam.pos_cam_y > cam.limit_top:
                cam.camera_offset_y += velocity_y
                cam.pos_cam_y -= velocity_y
          
            if event.key == pygame.K_DOWN and cam.pos_cam_y < cam.limit_bottom:
                cam.camera_offset_y -= velocity_y
                cam.pos_cam_y += velocity_y



        pygame.display.flip()

    clock.tick(60)

pygame.quit()
