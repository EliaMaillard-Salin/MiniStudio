import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tilemap Editor")

# Define grid properties
grid_size = 32
num_rows = 10
num_cols = 60

# Create an empty grid
grid = [["Void" for _ in range(num_cols)] for _ in range(num_rows)]

# Define element colors
element_colors = {
    "Element": (44, 44, 44),  # Dark gray
    "Void": (255, 255, 255, 0) # Add a transparent color for the "void" element
}

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // grid_size
                col = mouse_pos[0] // grid_size
                # Fill the grid with different elements
                grid[row][col] = "Element"
            

    # Update game logic

    # Render graphics
    screen.fill((255, 255, 255))  # Fill the screen with white color
    # Draw the grid lines
    for x in range(0, screen_width, grid_size):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, screen_height))
    for y in range(0, screen_height, grid_size):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (screen_width, y))

    # Draw the grid
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] != "Void":
                pygame.draw.rect(screen, element_colors[grid[row][col]], (col * grid_size, row * grid_size, grid_size, grid_size))
    
    # Draw preview element at mouse position
    mouse_pos = pygame.mouse.get_pos()
    row = mouse_pos[1] // grid_size
    col = mouse_pos[0] // grid_size
    pygame.draw.rect(screen, element_colors["Element"], (col * grid_size, row * grid_size, grid_size, grid_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
