import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tilemap Editor")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # New color for the mouse position
GREY = (128, 128, 128)

# Define tile size
tile_size = 32

# Create a 2D array to store the tilemap
tilemap = [[0 for _ in range(screen_width // tile_size)] for _ in range(screen_height // tile_size)]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Get the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Validate the mouse position
                if 0 <= mouse_x < screen_width and 0 <= mouse_y < screen_height:
                    # Calculate the tile position
                    tile_x = mouse_x // tile_size
                    tile_y = mouse_y // tile_size

                    # Set the tile in the tilemap to a specific value (e.g., 1 for a wall tile)
                    tilemap[tile_y][tile_x] = 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the tilemap
    for y in range(len(tilemap)):
        for x in range(len(tilemap[y])):
            if tilemap[y][x] == 1:
                pygame.draw.rect(screen, GREY, (x * tile_size, y * tile_size, tile_size, tile_size))
            pygame.draw.rect(screen, BLACK, (x * tile_size, y * tile_size, tile_size, tile_size), 1)  # Draw grid lines

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Validate the mouse position
    if 0 <= mouse_x < screen_width and 0 <= mouse_y < screen_height:
        # Calculate the tile position
        tile_x = mouse_x // tile_size
        tile_y = mouse_y // tile_size

        # Draw a colored rectangle at the mouse position
        pygame.draw.rect(screen, RED, (tile_x * tile_size, tile_y * tile_size, tile_size, tile_size))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
