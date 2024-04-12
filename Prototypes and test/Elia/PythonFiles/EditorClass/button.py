import pygame 

#button class
class Button():
	def __init__(self,x: int , y: int , image: pygame.Surface , scale: int, imageOver : pygame.Surface | None ):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		if imageOver != None : 
			self.imgOver = pygame.transform.scale(imageOver, (int(width * scale), int(height * scale)))

	def draw(self, surface : pygame.Surface, changeOver : bool) -> bool :
		displayImg = self.image
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):

			if changeOver == True : 
				displayImg = self.imgOver
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		surface.blit(displayImg, (self.rect.x, self.rect.y))

		return action
