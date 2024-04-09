import pygame
import csv

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1800
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()
curent_element = 0
tile_size = 100

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # New color for the mouse position
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

# Create a 2D array to store the level
level = [[-1 for _ in range(18)] for _ in range(7)]

def isInTile(x, y):
    return x >= 0 and x < len(level[0]) and y >= 0 and y < len(level)

def draw_tilemap(level: list[list[int]], drawGrid: bool = False): # Draw the level
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] != -1:
                screen.blit(tile_list[level[y][x]], (x * tile_size, y * tile_size))
            if drawGrid:
                pygame.draw.rect(screen, BLACK, (x * tile_size, y * tile_size, tile_size, tile_size), 1)

# Game loop
running = True
while running:
    pygame.display.set_caption("Level Editor | FPS: %.2f" % clock.get_fps())
    clock.tick(60)
    screen.blit(bg1, (0, 0))
    screen.blit(bg2, (0, 0))
    screen.blit(bg3, (0, 0))
    
    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Validate the mouse position
    if 0 <= mouse_x < screen_width and 0 <= mouse_y < screen_height: # Check if the mouse is inside the screen
        # Calculate the tile position
        tile_x = mouse_x // tile_size
        tile_y = mouse_y // tile_size
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                with open("Ilan/Levels/level_2.csv", "w") as file:
                    for row in level:
                        file.write(",".join(map(str, row)) + "\n")
                    print("Level saved")
        
        # Handle mouse events
        if pygame.mouse.get_pressed()[0]: # Check if the left mouse button is pressed
            # Set the tile in the level to a specific value (e.g., 1 for a wall tile)
            if isInTile(tile_x, tile_y):
                level[tile_y][tile_x] = curent_element

        elif event.type == pygame.MOUSEWHEEL: # Check if the mouse wheel is used
            # Increase or decrease the current element based on the direction of the mouse wheel
            if event.y > 0:
                if curent_element > 0:
                    curent_element -= 1
            else:
                if curent_element < len(tile_list) - 1:
                    curent_element += 1
        
        elif pygame.mouse.get_pressed()[2]: # Check if the right mouse button is pressed
            # Set the tile in the level to 0 (delete the tile)
            if isInTile(tile_x, tile_y):
                level[tile_y][tile_x] = -1

    # Draw the tilemap
    draw_tilemap(level, True)

    # Draw the elements at the mouse position
    if isInTile(tile_x, tile_y):
        screen.blit(tile_list[curent_element], (tile_x * tile_size, tile_y * tile_size))
        
    # Update the display
    pygame.display.flip()
    pygame.display.update()

# Quit the game
pygame.quit()