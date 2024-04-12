import pygame
from . import Collision



class Bot:
    def __init__(self, posX : int , posY : int , width : int , height : int, checkPointL : tuple[int,int], checkPointR : tuple[int,int] ):
        self.posX = posX
        self.posY = posY
        self.Width = width
        self.Height = height


        # Bot Info
        self.BotVelocity : int = 1
        self.BotDirection : int = -1
        self.hp : int = 3
        self.hurt : bool = False
        self.attack : bool = False
        self.death : bool = False
        self.walk  : bool = True
        self.damage = False
        self.PlayerDeath = False

        # Bot Checkpoint Info
        self.Check : list[int]= [checkPointL[0],checkPointL[1],20,50]
        self.Check1 : list[int] = [checkPointR[0],checkPointR[1],20,50]
        self.Checkpoint1  : bool = True
        self.Checkpoint2  : bool = False

        # Rects for display 
        self.BotRect : pygame.rect.Rect = pygame.Rect(self.posX,self.posY,self.Width,self.Height)

        self.botdesign : list[str]= ['Elia/Create Level/Assets/PNG/Animations/Mobs/mov/Déplacement0001.png','Elia/Create Level/Assets/PNG/Animations/Mobs/mov/Déplacement0002.png','Elia/Create Level/Assets/PNG/Animations/Mobs/mov/Déplacement0003.png','Elia/Create Level/Assets/PNG/Animations/Mobs/mov/Déplacement0004.png','Elia/Create Level/Assets/PNG/Animations/Mobs/mov/Déplacement0005.png']
        self.botdesign_nb : int = 0

        self.bothurt : list[str] = ['Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0001.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0002.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0003.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0004.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0005.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0006.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0007.png',
                        'Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0008.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0009.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0010.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0011.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0012.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0013.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0014.png',
                        'Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0015.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0016.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0017.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0018.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Degats/Mort0019.png']
        self.bothurt_nb : int = 0

        self.botAttack : list[str] = ['Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0001.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0002.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0003.png',
                          'Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0006.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0007.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0008.png',
                          'Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0009.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0010.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0011.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0012.png',
                          'Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0013.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0014.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0015.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0016.png',
                          'Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0017.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0018.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0019.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0020.png',
                          'Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0021.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0022.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0023.png','Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0024.png',
                          'Elia/Create Level/Assets/PNG/Animations/Mobs/Attack/Attaque0025.png']
        self.botAttack_nb : int = 0
        
        self.botdeath : list[str] = ['Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0001.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0002.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0003.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0004.png',
                         'Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0005.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0006.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0007.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0008.png',
                         'Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0009.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0010.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0011.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0012.png',
                         'Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0013.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0014.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0015.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0016.png',
                         'Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0017.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0018.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0019.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0020.png',
                         'Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0021.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0022.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0023.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0024.png',
                         'Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0025.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0026.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0027.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0028.png',
                         'Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0029.png','Elia/Create Level/Assets/PNG/Animations/Mobs/death/Mort Long0030.png',]
        self.botdeath_nb :int = 0
    
        self.all_anim : list[list[str]] = [self.botdesign,self.bothurt,self.botAttack,self.botdeath]

        self.imganim : list[list[pygame.Surface]]= []

    def load_anim_bot(self) -> None:
        for elt in self.all_anim:
            newAmin : list[pygame.Surface] = []
            for i in range(len(elt)):
                newAmin.append(pygame.image.load(elt[i]))
            self.imganim.append(newAmin)



    def walking(self, fen, cam : tuple[int,int]) -> None :
        if self.walk == True :
            if self.BotDirection == -1:
                walk = pygame.transform.flip(pygame.transform.scale(self.imganim[0][self.botdesign_nb],(self.Width + 180,self.Height + 40)), True,False)
                fen.blit(walk,(self.posX - 95 - cam[0],self.posY - 25- cam[1]))
            elif self.BotDirection == 1:
                walk = pygame.transform.scale(self.imganim[0][self.botdesign_nb],(self.Width + 180,self.Height + 40))
                fen.blit(walk,(self.posX - 85- cam[0],self.posY - 25- cam[1]))

    def BotHurt(self, fen, cam : tuple[int,int]):
        if self.BotDirection == -1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[1][self.bothurt_nb],(self.Width + 30,self.Height + 35)), True,False)
            fen.blit(walk,(self.posX - 15- cam[0],self.posY - 25- cam[1]))
        elif self.BotDirection == 1:
            walk = pygame.transform.scale(self.imganim[1][self.bothurt_nb],(self.Width + 30,self.Height + 35))
            fen.blit(walk,(self.posX - 15- cam[0],self.posY - 25- cam[1]))
    
    def BotAttack(self,fen, cam : tuple[int,int]):
        if self.BotDirection == -1:  
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[2][self.botAttack_nb],(self.Width + 30,self.Height + 35)), True,False)
            fen.blit(walk,(self.posX - 15- cam[0],self.posY - 25- cam[1])) 
        elif self.BotDirection == 1:
            walk = pygame.transform.scale(self.imganim[2][self.botAttack_nb],(self.Width + 30,self.Height + 35))
            fen.blit(walk,(self.posX - 15- cam[0],self.posY - 25- cam[1]))
                

    def BotDeath(self,fen, cam : tuple[int,int]) :
        if self.BotDirection == -1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[3][self.botdeath_nb],(self.Width + 30,self.Height + 35)), True,False)
            fen.blit(walk,(self.posX - 15 - cam[0] ,self.posY - 25- cam[1]))
        elif self.BotDirection == 1:
            walk = pygame.transform.scale(self.imganim[3][self.botdeath_nb],(self.Width + 30,self.Height + 35))
            fen.blit(walk,(self.posX - 15 - cam[0],self.posY - 25 - cam[1]))
    
    def Death(self, listMobs: list) : 
        self.Width = 0
        self.Height = 0
        listMobs.remove(self)

    def MovementBot(self):

        if self.Checkpoint1 :
            self.posX -= self.BotVelocity
            self.BotDirection = -1
        if self.Checkpoint2 :
            self.posX += self.BotVelocity
            self.BotDirection = 1
    
    def DisplayBot(self, surface : pygame.Surface):
        self.BotRect = pygame.Rect(self.posX,self.posY,self.Width,self.Height)
        #pygame.draw.rect(surface, "blue", self.BotRect)

    def DisplayCheckBot(self,surface  : pygame.Surface ):
        self.CheckRect = pygame.Rect(self.Check[0],self.Check[1],self.Check[2],self.Check[3])
        #pygame.draw.rect(surface, (0,0,0), (50,550,20,20))
        self.Check1Rect = pygame.Rect(self.Check1[0],self.Check1[1],self.Check1[2],self.Check1[3] )
        #pygame.draw.rect(surface, (0,0,0), (750,550,20,20))

    def BotOnGround(self, Y): 
            if (self.verticalVelocity > 0 ):
                self.posY = Y - self.Height
                self.verticalVelocity = 0 
                self.onGround = False 

    def CheckCollision(self):
        # Vérifier la collision avec le checkpoint 1 pour bot
        check_rect = pygame.Rect(self.Check[0],self.Check[1],self.Check[2],self.Check[3])
        if self.BotRect.colliderect(check_rect):
            self.Checkpoint1 = False
            self.Checkpoint2 = True
                
        # Vérifier la collision avec le checkpoint 1 pour bot        
        check_rect = pygame.Rect(self.Check1[0],self.Check1[1],self.Check1[2],self.Check1[3])
        if self.BotRect.colliderect(check_rect):
            self.Checkpoint2 = False
            self.Checkpoint1 = True

    def CollisionBot(self,player):

    # Déstruction d'un bot en sautant dessus
        bot_rect = pygame.Rect(self.posX,self.posY,self.Width, self.Height)
        self.col = Collision.collision(player.playerRect,bot_rect)
        ColWeapon = Collision.collision(player.weaponRect, bot_rect)
        if self.col == 2 and player.isDashing == False:
            if self.hp == 1 :
                self.death = True
                self.hp -= 1
                self.Checkpoint1 = False
                self.Checkpoint2 = False
                player.verticalVelocity = -player.jumpForce
            else:
                player.verticalVelocity = -player.jumpForce
                self.hurt = True
                self.hp -= 1

        if ColWeapon == 1 or ColWeapon == 4 or (self.BotDirection == -1 and self.col == 4 and player.isDashing == True) or (self.BotDirection == 1 and self.col == 1 and player.isDashing == True):
            if self.hp == 0:
                self.death = True
                self.hp -= 1
                self.Checkpoint1 = False
                self.Checkpoint2 = False
            else :
                self.hp -= 1
                self.bothurt = True

        if (self.col != 0 and self.col != 2 and player.isDashing == False) or (self.col == 1 and player.isDashing == True and self.BotDirection == -1 ) or (self.col == 4 and player.isDashing == True and self.BotDirection == 1):
            player.LooseOrWinHP(-1)
            player.getHit = True
            if player.health == 0 : 
                self.attack = True
                self.PlayerDeath = True
            self.attack = True
            if self.BotDirection == 1:
                if self.col == 4 :
                    player.posX += 20
                elif self.col == 1 :
                    player.posX -= 10
                elif self.col == 3 : 
                    player.posY += 10 
            elif self.BotDirection == -1:
                if self.col == 4 :
                    player.posX += 10
                elif self.col == 1 :
                    player.posX -= 20
                elif self.col == 3 : 
                    player.posY += 10 