import pygame
import csv

# Initialize Pygame
pygame.init()

# Set up
screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Level-1")
clock = pygame.time.Clock()
scroll = 0
tile_size = 50
tile_width = screen_width // 18
tile_height = screen_height // 7

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

# Load images
bg1 = pygame.transform.scale(pygame.image.load("Ilan/img/background/sky_cloud.png"), screen.get_size())
bg2 = pygame.transform.scale(pygame.image.load("Ilan/img/background/pine1.png"), screen.get_size())
bg4 = pygame.transform.scale(pygame.image.load("Ilan/img/background/mountain.png"), screen.get_size())
bg3 = pygame.transform.scale(pygame.image.load("Ilan/img/background/pine2.png"), screen.get_size())
ground_1 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/0.png"), (tile_size, tile_size))
ground_2 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/1.png"), (tile_size, tile_size))
ground_3 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/2.png"), (tile_size, tile_size))
ground_4 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/3.png"), (tile_size, tile_size))
ground_5 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/4.png"), (tile_size, tile_size))
ground_6 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/5.png"), (tile_size, tile_size))
ground_7 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/6.png"), (tile_size, tile_size))
ground_8 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/7.png"), (tile_size, tile_size))
ground_9 = pygame.transform.scale(pygame.image.load("Ilan/img/tile/8.png"), (tile_size, tile_size))
box = pygame.transform.scale(pygame.image.load("Ilan/img/tile/12.png"), (tile_size, tile_size))
tile_list = [ground_1, ground_2, ground_3, ground_4, ground_5, ground_6, ground_7, ground_8, ground_9, box]

def load_level(level_path):
    with open(level_path, 'r') as file:
        return list(csv.reader(file))

def draw_level(level: list[list[int]]): # Draw the level
    for y, row in enumerate(level): # enumerate() permet d'itérer sur une liste en gardant une trace de l'index
        for x, tile_type in enumerate(row): # idem
            if tile_type != -1:  # -1 signifie pas de plateforme
                screen.blit(tile_list[level[y][x]], (x * tile_width - scroll, y * tile_height))

loading_level = load_level("Ilan/Levels/level_2.csv")
level = [[int(x) for x in inner] for inner in loading_level]
print(level)

# Game loop
running = True
while running:
    pygame.display.set_caption("Level Editor | FPS: %.2f" % clock.get_fps())
    clock.tick(60)
    screen.blit(bg1, (0, 0))
    screen.blit(bg2, (0, 0))
    screen.blit(bg3, (0, 0))
    
    # Draw the level
    draw_level(level)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle scrolling events
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_LEFT] and scroll > 0:
                scroll -= 100
            elif pygame.key.get_pressed()[pygame.K_RIGHT] and scroll < (len(level[0]) * tile_width) - screen_width:
                scroll += 100
        
    # Update the display
    pygame.display.flip()
    pygame.display.update()

# Quit the game
pygame.quit()