import pygame
import sys



# Initialisation de Pygame
pygame.init()


def collision(rectA: pygame.rect.Rect, rectB: pygame.rect.Rect):
         
    if rectA.left > rectB.right:
        return 0
    
    if rectA.right > rectB.left:
        return 0

    if rectA.top > rectB.bottom:
        return 0

    if rectA.bottom < rectB.top:
        return 0

    # Calculer les 4 distanes, on stockera dans un tableau de 4 cases
    distance = list(range(0))    
    distance.append(rectA.right - rectB.left) #0
    distance.append(rectA.bottom - rectB.top) #1
    distance.append(rectB.bottom - rectA.top) #2
    distance.append(rectB.right - rectA.left) #3
    print(distance)
   
    #on parcourt le tableau, on cherche la distance la plus grande
    smallest = 1000
    for i in range(len(distance)) :
        if distance[i] < smallest :
            smallest = distance[i]
            index = i
    return distance[index] 

# Paramètres de la fenêtre
screen_width = 800
screen_height = 600


purple = (80,00,80)

# Paramètres du joueur
hp = 1
player_x = 50
player_y = 50
player_width = 50
player_height = 50


posX = 530
posY = 540
width = 50 
height = 50
bot_velocity = 1
checkpoint1 = True
checkpoint2 = False


while running:
    
    # Déstruction d'un bot en sautant dessus
    bot_rect = pygame.Rect(bot_x,bot_y,bot_width,bot_height)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    if (player_rect.bottom >= bot_rect.top) and (bot_rect.top < player_rect.bottom) :
        col = collision(player_rect,bot_rect)
    if col == 2 :
        checkpoint1 = False
        checkpoint2 = False
        bot_height = 0
        bot_width = 0
        bot_x = -1111111
        bot_y = -1111111
        pv -= 1
        vertical_velocity = -jump_attack


        
        




    pygame.draw.rect(screen, black,  plateforms)
    pygame.draw.rect(screen, black,  plateforms)
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    if hp == 1:
        pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

pygame.quit()

