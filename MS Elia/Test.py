
import pygame
import time

pygame.init()

clock = pygame.time.Clock()


class Player: 
    def __init__(self, speed, posX, posY,screen):
        self.jumpCount = 10
        self.isJumping = False
        self.onGround = False
        self.speed = speed
        self.posX = posX
        self.posY = posY
        self.screen = screen
        self.powerJump = 10
        self.Rect = pygame.Rect(self.posX,self.posY,100,100)
    
    def UpdatePlayer(self):
        self.Rect = pygame.Rect(self.posX,self.posY,100,100)
        pygame.draw.rect(self.screen, "white", self.Rect)

    def Fall(self, dt): 
        if self.onGround == False:
            self.posY += 100 * dt
            self.UpdatePlayer()

    def Collision(self, Rect):  
        if (self.Rect.left + self.Rect.width >= Rect.left and
            self.Rect.left <= Rect.left + Rect.width and
            self.Rect.top + self.Rect.height >= Rect.top and 
            self.Rect.top <= Rect.top + Rect.height):
            return True
        return False


    

screen = pygame.display.set_mode((500,500))

running = True

player = Player(400,400,200,screen)

ground  = pygame.Rect(0,400,500,100)

yGravity = 1

while running: 

    dt = clock.tick(60) * 0.001


    screen.fill("grey")

    pygame.draw.rect(screen,"green",ground)

    player.UpdatePlayer()


    if player.onGround == False:
        player.Fall(dt)
        player.onGround = player.Collision(ground)
    if (player.posY + player.Rect.height) >= ground.top: 
        player.Rect.bottom = ground.top

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_d]: 
            player.posX += player.speed * dt
        if pressed[pygame.K_q]: 
            player.posX += -player.speed * dt
        if pressed[pygame.K_SPACE]:
            player.isJumping = True

    if player.isJumping: 
        if player.jumpCount >= -10:
            player.posY -= (player.jumpCount * abs(player.jumpCount)) * 0.5
            player.jumpCount -= 1
        else: 
            player.jumpCount = 10
            player.isJumping = False
    pygame.display.flip()


pygame.quit()