import pygame
import csv

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
TILE_TYPES = 21
level = 0
current_tile = 0
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

# Couleurs
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)

# Stockage des tuiles dans une liste
img_list = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'img/tile/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)

save_img = pygame.image.load('img/save_btn.png').convert_alpha()
load_img = pygame.image.load('img/load_btn.png').convert_alpha()

#define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)


#create empty tile list
world_data = []
for row in range(ROWS):
	r = [-1] * MAX_COLS
	world_data.append(r)

#create ground
for tile in range(0, MAX_COLS):
	world_data[ROWS - 1][tile] = 0
 
 #draw grid
def draw_grid():
	#vertical lines
	for c in range(MAX_COLS + 1):
		pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
	#horizontal lines
	for c in range(ROWS + 1):
		pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


#function for drawing the world tiles
def draw_world():
	for y, row in enumerate(world_data):
		for x, tile in enumerate(row):
			if tile >= 0:
				screen.blit(img_list[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE))