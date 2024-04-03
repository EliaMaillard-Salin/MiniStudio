import pygame, math

# ===== Lunch Page =====
def page_accueil():
    running = True
    while running:
        clock.tick(60)
        # Tracé des éléments de la page
        screen.fill(BLANC)
        dessin_text1 = police.render("Space : Lunch the game", 1, NOIR)
        screen.blit(dessin_text1, (100,100))
        dessin_text_quitter = police.render("Echap : Quitter", 1, NOIR)
        screen.blit(dessin_text_quitter, (100, 280))
        pygame.display.flip()
        # Navigation dans les pages
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    running = False
                    Game()
    pygame.quit()


def Game():
    pygame.mouse.set_visible(0)   
    
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    
    i = 0
    running = True
    while running:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        
        # 
        screen.fill((0,0,0))
        screen.blit(bg,(i,0))
        screen.blit(bg,(width+i,0))
        if (i==-width):
            screen.blit(bg,(width+i,0))
            i=0
        i-=1
        
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.draw.circle(screen, BLEU, player_pos, 20)

        if player_pos.x <= 0 or player_pos.y <= 0 or player_pos.x >= screen.get_width() or player_pos.y >= screen.get_height():
            player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        
        #player_pos.y += 200 * dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]: #Up
            player_pos.y -= 500 * dt
        if keys[pygame.K_q]: #Left
            player_pos.x -= 500 * dt
        if keys[pygame.K_d]: #Right
            player_pos.x += 500 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        pygame.display.update()
        
    pygame.quit()



# ===== Pygame Setup =====
pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("maison.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Coders Legacy")
# Loading the images
bg = pygame.image.load("Assets/background2.png")
bg = pygame.transform.scale(bg, (width, height))


clock = pygame.time.Clock()
dt = 0 #DataTime

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
police = pygame.font.Font("AcherusGrotesqueFont/horizon-type-acherusgrotesque-regular.otf", 75)

page_accueil()
