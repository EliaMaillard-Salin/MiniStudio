import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')


ROWS = 16
MAX_COLS = 150 # Permet d'imposer une limite de taille pour le niveau
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
level = 0
current_tile = 0
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1  

GREEN = (144, 201, 120)
WHITE = (255, 255, 255)


font = pygame.font.SysFont('Futura', 30)

# Liste qui va stocker les données du niveau
world_data = []
for row in range(ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)

run = True
while run:

    clock.tick(FPS)
                
    # Ajuste le défilement en fonction des touches enfoncées
    if scroll_left and scroll > 0:
        scroll -= 5 * scroll_speed
    elif scroll_right and scroll < (MAX_COLS * TILE_SIZE) - SCREEN_WIDTH:
        scroll += 5 * scroll_speed

    screen.fill(GREEN) 

    # Dessiner la grille
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
    for r in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, r * TILE_SIZE), (SCREEN_WIDTH, r * TILE_SIZE))


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    scroll_left = True
                if event.key == pygame.K_RIGHT:
                    scroll_right = True
                if event.key == pygame.K_RSHIFT:
                    scroll_speed = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    scroll_left = False
                if event.key == pygame.K_RIGHT:
                    scroll_right = False
                if event.key == pygame.K_RSHIFT:
                    scroll_speed = 1

    pygame.display.update()

pygame.quit()
