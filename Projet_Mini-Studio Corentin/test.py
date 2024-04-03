import pygame

s_width : int = 1600
s_height : int = 900
ongoing : bool = True

gray : tuple = (150, 150, 150)
red : tuple = (255, 0, 0)
blue : tuple = (0, 0, 255)

picture_cars = pygame.image.load("Pictures/Test.png")

pos_x : int = 10
pos_y : int = 400

gravity_y : int = 1
jump_height : int = 20

velocity_x : int = 10
velocity_y : int = jump_height

jumping : bool = False

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()

while ongoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ongoing = False

        screen.fill(gray)
        screen.blit(picture_cars, (pos_x, pos_y))

        ispressed = pygame.key.get_pressed()

        if ispressed[pygame.K_d]:
            pos_x += velocity_x

        if ispressed[pygame.K_q]:
            pos_x -= velocity_x

        if ispressed[pygame.K_SPACE]:
            jumping = True
    
        if jumping:
            pos_y -= velocity_y
            velocity_y -= gravity_y
            if velocity_y < -jump_height:
                jumping = False
                velocity_y = jump_height

        pygame.display.flip()

    clock.tick(60)

pygame.quit()
