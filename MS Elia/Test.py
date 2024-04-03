
import pygame
import time

pygame.init()

clock = pygame.time.Clock()


class Player: 
    def __init__(self, speed, posX, posY,screen):
        self.jumpCount = 10
        self.isJumping = False
        self.onGround = True
        self.speed = speed
        self.posX = posX
        self.posY = posY
        self.screen = screen
        self.powerJump = 100
        self.Rect = pygame.Rect(self.posX,self.posY,100,100)
    
    def UpdatePlayer(self):
        self.Rect = pygame.Rect(self.posX,self.posY,100,100)
        pygame.draw.rect(self.screen, "white", self.Rect)
    
    def MovingPlayer(self,side, dt): 
        self.posX += side* self.speed*dt
        self.UpdatePlayer()

    def Jump(self, dt):
        
        if player.onGround == True and self.isJumping == True: 
            self.onGround = False
            if self.jumpCount >= -10:
                self.posY -= (self.jumpCount**2)*0.5
                self.jumpCount -=1
            else :
                self.jumpCount = 10
                self.isJumping = False

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
    

screen = pygame.display.set_mode((900,900))

running = True

player = Player(400,400,700,screen)

ground  = pygame.Rect(0,800,900,100)


while running: 
    dt = clock.tick(60) * 0.001


    screen.fill("grey")

    pygame.draw.rect(screen,"green",ground)

    player.UpdatePlayer()


    if player.onGround == False:
        player.Fall(dt)
        player.onGround = player.Collision(ground)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE and player.onGround == True:
                player.isJumping = True
                player.Jump(dt)


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]: 
            player.MovingPlayer(1,dt)
        if pressed[pygame.K_q]: 
            player.MovingPlayer(-1,dt)

    pygame.display.flip()


pygame.quit()