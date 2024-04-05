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
