import pygame
import EditorClass.button as button
import csv

pygame.init()

# Param
clock = pygame.time.Clock()
FPS :int  = 60
SCREEN_WIDTH : int = 1000
SCREEN_HEIGHT : int = 600
LOWER_MARGIN : int = 100
SIDE_MARGIN : int = 300
screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')

# Grid
ROWS : int = 16
MAX_COLS : int = 150
TILE_SIZE : int = SCREEN_HEIGHT // ROWS
TILE_TYPES : int = 12
level : int = 0
current_tile : int = 0
scroll_left : bool = False
scroll_right : bool = False
scroll : int = 0
scroll_speed : int = 1

#load images
# pine1_img : pygame.Surface = pygame.image.load('Ilan/img/Background/pine1.png').convert_alpha()
# pine2_img  : pygame.Surface = pygame.image.load('Ilan/img/Background/pine2.png').convert_alpha()
# mountain_img : pygame.Surface = pygame.image.load('Ilan/img/Background/mountain.png').convert_alpha()

sky_img : pygame.Surface = pygame.image.load('PythonFiles/Assets/PNG/Background.png').convert_alpha()

# Colors
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)

# Store tiles in a list
img_list : list[pygame.Surface] = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'PythonFiles/Assets/PNG/Blocs/{x}.png').convert_alpha()
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)

save_img : pygame.Surface = pygame.image.load('PythonFiles/Assets/PNG/Boutons/SAVE.png').convert_alpha()
load_img : pygame.Surface = pygame.image.load('PythonFiles/Assets/PNG/Boutons/LOAD.png').convert_alpha()
save_imgOver : pygame.Surface = pygame.image.load('PythonFiles/Assets/PNG/Boutons/SAVE1.png')
load_imgOver : pygame.Surface = pygame.image.load('PythonFiles/Assets/PNG/Boutons/LAOD1.png')

GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)

font : pygame.font.Font = pygame.font.Font('PythonFiles/Assets/Fonts/Unbounded-Regular.ttf', 30)

# create empty tile list
world_data : list[list[int]] = []
for row in range(ROWS):
	r : list[int] = [-1] * MAX_COLS
	world_data.append(r)


# Paralaxe
def draw_bg() -> None:
	screen.blit(sky_img, (0,0))
	width = sky_img.get_width()
	for x in range(4):
		screen.blit(sky_img, ((x * width) - scroll * 0.5, 0))
		# screen.blit(mountain_img, ((x * width) - scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
		# screen.blit(pine1_img, ((x * width) - scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
		# screen.blit(pine2_img, ((x * width) - scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))


#function for outputting text onto the screen
def draw_text(text: str , font: pygame.font.Font , text_col : tuple[int,int,int] , x : int , y : int ) -> None :
	img : pygame.Surface = font.render(text, True, text_col)
	screen.blit(img, (x, y))



#draw grid
def draw_grid() -> None:
	#vertical lines
	for c in range(MAX_COLS + 1):
		pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
	#horizontal lines
	for c in range(ROWS + 1):
		pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


#function for drawing the world tiles
def draw_world() -> None:
	for y, row in enumerate(world_data):
		for x, tile in enumerate(row):
			if tile >= 0:
				screen.blit(img_list[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE))

#create buttons
save_button = button.Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT  + 10, save_img, 0.3, save_imgOver)
load_button = button.Button(SCREEN_WIDTH // 2 + 300 - 50, SCREEN_HEIGHT + 10, load_img, 0.3, load_imgOver)
#make a button list
button_list : list[button.Button] = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
	tile_button : button.Button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1, None)
	button_list.append(tile_button)
	button_col += 1
	if button_col == 3:
		button_row += 1
		button_col = 0    
  
run = True

while run:

	clock.tick(FPS)

	draw_bg()
	draw_grid()
	draw_world()

	pygame.draw.rect(screen, (255,197,132), (0,SCREEN_HEIGHT+LOWER_MARGIN-105, SCREEN_WIDTH + SIDE_MARGIN,150))

	draw_text(f'Level: {level}', font, (0,0,0), 30, SCREEN_HEIGHT + LOWER_MARGIN - 90)
	draw_text('Press UP or DOWN to change level', font, (0,0,0), 30, SCREEN_HEIGHT + LOWER_MARGIN - 60)

	#save and load data
	if save_button.draw(screen, True):
		#save level data
		with open(f"PythonFiles/Levels/level{level}_data.csv", "w") as file:
			for row in world_data:
				file.write(",".join(map(str, row)) + "\n")
			print("Level saved")

	if load_button.draw(screen, True ):
		scroll = 0
		with open(f'PythonFiles/Levels/level{level}_data.csv') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',')
			for x, row in enumerate(reader):
				for y, tile in enumerate(row):
					world_data[x][y] = int(tile)
			print(f'Level {level} loaded')
		
	#draw tile panel and tiles
	pygame.draw.rect(screen, (255,197,132) , (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

	#choose a tile
	button_count = 0
	for button_count, i in enumerate(button_list):
		if i.draw(screen, False):
			current_tile = button_count

	#highlight the selected tile
	pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

	#scroll the map
	if scroll_left == True and scroll > 0:
		scroll -= 5 * scroll_speed
	if scroll_right == True and scroll < (MAX_COLS * TILE_SIZE) - SCREEN_WIDTH:
		scroll += 5 * scroll_speed

	#add new tiles to the screen

	#get mouse position
	pos = pygame.mouse.get_pos()
	x = (pos[0] + scroll) // TILE_SIZE
	y = pos[1] // TILE_SIZE

	#check that the coordinates are within the tile area
	if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
		#update tile value
		if pygame.mouse.get_pressed()[0] == 1:
			if world_data[y][x] != current_tile:
				world_data[y][x] = current_tile
		if pygame.mouse.get_pressed()[2] == 1:
			world_data[y][x] = -1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		#keyboard presses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level += 1
			if event.key == pygame.K_DOWN and level > 0:
				level -= 1
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
