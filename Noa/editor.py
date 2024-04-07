import pygame
import json

pygame.init()

# Paramètres de base
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300
screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')

# Grille
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
level = 0
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

# Couleurs
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)

# Tuiles
tile_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
current_tile = 0

# Liste du niveau
world_data = [[-1 for _ in range(MAX_COLS)] for _ in range(ROWS)]

font = pygame.font.SysFont('Futura', 30)

def draw_grid():
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                pygame.draw.rect(screen, tile_colors[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_tile_panel():
    pygame.draw.rect(screen, GREY, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
    for i, color in enumerate(tile_colors):
        pygame.draw.rect(screen, color, (SCREEN_WIDTH + 50, i * 100 + 50, TILE_SIZE, TILE_SIZE))

def save_level():
    with open('level.json', 'w') as file:
        json.dump(world_data, file)
    print("Level saved!")

def load_level():
    global world_data
    with open('level.json', 'r') as file:
        world_data = json.load(file)
    print("Level loaded!")

run = True
while run:
    clock.tick(FPS)

    # Gestion du défilement
    if scroll_left and scroll > 0:
        scroll -= 5 * scroll_speed
    elif scroll_right and scroll < (MAX_COLS * TILE_SIZE) - SCREEN_WIDTH:
        scroll += 5 * scroll_speed

    screen.fill(GREEN)
    draw_grid()
    draw_world()
    draw_tile_panel()

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_s:
                save_level()
            if event.key == pygame.K_l:
                load_level()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False

    # Gestion de la sélection et du placement de tuiles
    if pygame.mouse.get_pressed()[0]:  # Bouton gauche
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x < SCREEN_WIDTH:
            grid_x = (mouse_x + scroll) // TILE_SIZE
            grid_y = mouse_y // TILE_SIZE
            if grid_y < ROWS and grid_x < MAX_COLS:
                world_data[grid_y][grid_x] = current_tile
        else:  # Sélection dans le panneau
            if mouse_y < len(tile_colors) * 100:
                current_tile = mouse_y // 100

    pygame.display.update()

pygame.quit()
