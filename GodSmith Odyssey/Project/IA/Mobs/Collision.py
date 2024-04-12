import pygame 
from . import BotInfo as Bot
def collision(rectA: pygame.rect.Rect, rectB: pygame.rect.Rect):
    # 0 None
    # 1 Left
    # 2 Top
    # 3 Bottom
    # 4 Right
 
    if rectA.left > rectB.right:
        return 0
    
    if rectA.right < rectB.left:
        return 0

    if rectA.top > rectB.bottom:
        return 0

    if rectA.bottom < rectB.top:
        return 0

    #calculer les 4 distanes, on stockera dans un tableau de 4 cases
    distance = list(range(0))    
    distance.append(rectA.right - rectB.left) #0
    distance.append(rectA.bottom - rectB.top) #1
    distance.append(rectB.bottom - rectA.top) #2
    distance.append(rectB.right - rectA.left) #3

    #on parcourt le tableau, on cherche la distance la plus grande
    smallest = 1000
    for i in range(len(distance)) :
        if distance[i] < smallest :
            smallest = distance[i]
            index = i
    return index + 1  
 

