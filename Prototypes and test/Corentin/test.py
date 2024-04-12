import pygame
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Simple Game")
clock = pygame.time.Clock()
BACKGROUND_COLOR = (255, 255, 255)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT - PLAYER_HEIGHT - 20
PLAYER_SPEED = 10
RECTANGLE_COLOR_1 = (255, 0, 0)
RECTANGLE_COLOR_2 = (0, 0, 255)
rectangle_1 = pygame.Rect(200, 200, 100, 100)
rectangle_2 = pygame.Rect(500, 300, 150, 50)

# Set the camera offset
camera_offset_x = 0
camera_offset_y = 0

class Player:

    def __init__(self, x,y,c,w,h):
        self.x = x
        self.y = y
        self.color = c
        self.width = w
        self.height = h

    def move(self, m):
        self.x += m*5

player = Player(400, 400, RECTANGLE_COLOR_1, 50, 50)

while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    screen.blit(player, (0,0))

    # Draw the static rectangles
    rectangle_1_draw_pos = rectangle_1.move(camera_offset_x, camera_offset_y)
    pygame.draw.rect(screen, RECTANGLE_COLOR_1, rectangle_1_draw_pos)
        
    rectangle_2_draw_pos = rectangle_2.move(camera_offset_x, camera_offset_y)
    pygame.draw.rect(screen, RECTANGLE_COLOR_2, rectangle_2_draw_pos)

    # Draw the player
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)   
    pygame.draw.rect(screen, (0, 0, 0), player_rect)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        player.move(1)
    elif pressed[pygame.K_q] :
        player.move(-1)

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            camera_offset_x -= PLAYER_SPEED

        elif event.key == pygame.K_RIGHT:
            camera_offset_x += PLAYER_SPEED

        elif event.key == pygame.K_UP:
            camera_offset_y -= 10

        elif event.key == pygame.K_DOWN:
            camera_offset_y += 10

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(30)








"""#Mouvement
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
        
        
        
rect_1 = pygame.Rect(800, 400, 40, 100)
rect_2 = pygame.Rect(400, 40, 35, 120)
rect_3 = pygame.Rect(0, 700, 1600, 120)


    screen.fill(gray)
    rect_1_draw_pos = P1.move(cam.camera_offset_x, cam.camera_offset_y)
    pygame.draw.rect(screen, red, rect_1_draw_pos)
    rect_2_draw_pos = P2.move(cam.camera_offset_x, cam.camera_offset_y)
    pygame.draw.rect(screen, blue, rect_2_draw_pos)

    rect_3_draw_pos = P3.move(cam.camera_offset_x, cam.camera_offset_y)
    pygame.draw.rect(screen, green, rect_3_draw_pos)


        rect_1_draw_pos = rect_1.move(cam.camera_offset_x, cam.camera_offset_y)
        pygame.draw.rect(screen, red, rect_1_draw_pos)
        rect_2_draw_pos = rect_2.move(cam.camera_offset_x, cam.camera_offset_y)
        pygame.draw.rect(screen, blue, rect_2_draw_pos)
        rect_3_draw_pos = rect_3.move(cam.camera_offset_x, cam.camera_offset_y)
        pygame.draw.rect(screen, green, rect_3_draw_pos)

"""