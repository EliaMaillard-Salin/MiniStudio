import pygame
import PlayerMovement as Player
import Collision



class Bot:
    def __init__(self, posX, posY, width, height):
        self.posX = posX
        self.posY = posY
        self.Width = width
        self.Height = height


        # Bot Info
        self.BotVelocity = 1
        self.BotDirection = -1
        self.hp = 1
        self.invicible = 0
        self.PlayerIncivible = False
        self.hurt = False
        self.attack = False

        # Bot Checkpoint Info
        self.Check = [(50,550,20,20)]
        self.Check1 = [(750,550,20,20)]
        self.Checkpoint1 = True
        self.Checkpoint2 = False

        # Rects for display 
        self.BotRect = pygame.Rect(self.posX,self.posY,self.Width,self.Height)

        self.botdesign = ['Hugo/ministudio/img/bot/mov/Déplacement0001.png','Hugo/ministudio/img/bot/mov/Déplacement0002.png','Hugo/ministudio/img/bot/mov/Déplacement0003.png','Hugo/ministudio/img/bot/mov/Déplacement0004.png','Hugo/ministudio/img/bot/mov/Déplacement0005.png']
        self.botdesign_nb = 0

        self.bothurt = ['Hugo/ministudio/img/bot/Degats/Mort0001.png','Hugo/ministudio/img/bot/Degats/Mort0002.png','Hugo/ministudio/img/bot/Degats/Mort0003.png','Hugo/ministudio/img/bot/Degats/Mort0004.png','Hugo/ministudio/img/bot/Degats/Mort0005.png','Hugo/ministudio/img/bot/Degats/Mort0006.png','Hugo/ministudio/img/bot/Degats/Mort0007.png',
                        'Hugo/ministudio/img/bot/Degats/Mort0008.png','Hugo/ministudio/img/bot/Degats/Mort0009.png','Hugo/ministudio/img/bot/Degats/Mort0010.png','Hugo/ministudio/img/bot/Degats/Mort0011.png','Hugo/ministudio/img/bot/Degats/Mort0012.png','Hugo/ministudio/img/bot/Degats/Mort0013.png','Hugo/ministudio/img/bot/Degats/Mort0014.png',
                        'Hugo/ministudio/img/bot/Degats/Mort0015.png','Hugo/ministudio/img/bot/Degats/Mort0016.png','Hugo/ministudio/img/bot/Degats/Mort0017.png','Hugo/ministudio/img/bot/Degats/Mort0018.png','Hugo/ministudio/img/bot/Degats/Mort0019.png']
        self.bothurt_nb = 0

        self.botAttack = ['Hugo/ministudio/img/bot/Attack/Attaque0001.png','Hugo/ministudio/img/bot/Attack/Attaque0002.png','Hugo/ministudio/img/bot/Attack/Attaque0003.png',
                          'Hugo/ministudio/img/bot/Attack/Attaque0006.png','Hugo/ministudio/img/bot/Attack/Attaque0007.png','Hugo/ministudio/img/bot/Attack/Attaque0008.png',
                          'Hugo/ministudio/img/bot/Attack/Attaque0009.png','Hugo/ministudio/img/bot/Attack/Attaque0010.png','Hugo/ministudio/img/bot/Attack/Attaque0011.png','Hugo/ministudio/img/bot/Attack/Attaque0012.png',
                          'Hugo/ministudio/img/bot/Attack/Attaque0013.png','Hugo/ministudio/img/bot/Attack/Attaque0014.png','Hugo/ministudio/img/bot/Attack/Attaque0015.png','Hugo/ministudio/img/bot/Attack/Attaque0016.png',
                          'Hugo/ministudio/img/bot/Attack/Attaque0017.png','Hugo/ministudio/img/bot/Attack/Attaque0018.png','Hugo/ministudio/img/bot/Attack/Attaque0019.png','Hugo/ministudio/img/bot/Attack/Attaque0020.png',
                          'Hugo/ministudio/img/bot/Attack/Attaque0021.png','Hugo/ministudio/img/bot/Attack/Attaque0022.png','Hugo/ministudio/img/bot/Attack/Attaque0023.png','Hugo/ministudio/img/bot/Attack/Attaque0024.png',
                          'Hugo/ministudio/img/bot/Attack/Attaque0025.png']
        self.botAttack_nb = 0
        self.all_anim : list[list[str]] = [self.botdesign,self.bothurt,self.botAttack]

        self.imganim : list[list[pygame.Surface]]= []

    def load_anim(self):
        for elt in self.all_anim:
            newAmin : list[pygame.Surface] = []
            for i in range(len(elt)):
                newAmin.append(pygame.image.load(elt[i]))
            self.imganim.append(newAmin)



    def walking(self, fen):
        if self.BotDirection == -1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[0][self.botdesign_nb],(self.Width + 180,self.Height + 40)), True,False)
            fen.blit(walk,(self.posX - 95,self.posY - 25))
        elif self.BotDirection == 1:
            walk = pygame.transform.scale(self.imganim[0][self.botdesign_nb],(self.Width + 180,self.Height + 40))
            fen.blit(walk,(self.posX - 85,self.posY - 25))

    def BotHurt(self, fen):
        if self.BotDirection == -1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[1][self.bothurt_nb],(self.Width + 30,self.Height + 35)), True,False)
            fen.blit(walk,(self.posX - 15,self.posY - 25))
        elif self.BotDirection == 1:
            walk = pygame.transform.scale(self.imganim[1][self.bothurt_nb],(self.Width + 30,self.Height + 35))
            fen.blit(walk,(self.posX - 15,self.posY - 25))
    
    def BotAttack(self,fen):
        if self.BotDirection == -1:
            walk = pygame.transform.flip(pygame.transform.scale(self.imganim[2][self.botAttack_nb],(self.Width + 30,self.Height + 35)), True,False)
            fen.blit(walk,(self.posX - 15,self.posY - 25))
        elif self.BotDirection == 1:
            walk = pygame.transform.scale(self.imganim[2][self.botAttack_nb],(self.Width + 30,self.Height + 35))
            fen.blit(walk,(self.posX - 15,self.posY - 25))



    def MovementBot(self):

        if self.Checkpoint1 :
            self.posX -= self.BotVelocity
            self.BotDirection = -1
        if self.Checkpoint2 :
            self.posX += self.BotVelocity
            self.BotDirection = 1
    
    def DisplayBot(self, surface):
        self.BotRect = pygame.Rect(self.posX,self.posY,self.Width,self.Height)
        pygame.draw.rect(surface, "blue", self.BotRect)

    def DisplayCheckBot(self,surface):
        self.CheckRect = pygame.Rect((50,550,20,20))
        #pygame.draw.rect(surface, (0,0,0), (50,550,20,20))
        self.Check1Rect = pygame.Rect((750,550,20,20))
        #pygame.draw.rect(surface, (0,0,0), (750,550,20,20))

    def BotOnGround(self, Y): 
            if (self.verticalVelocity > 0 ):
                self.posY = Y - self.Height
                self.verticalVelocity = 0 
                self.onGround = False 

    def CheckCollision(self):
        # Vérifier la collision avec le checkpoint 1 pour bot
        for self.Plateforms in self.Check:
            check_rect = pygame.Rect(50,550,20,20)
            if self.BotRect.colliderect(check_rect):
                self.Checkpoint1 = False
                self.Checkpoint2 = True


                
        # Vérifier la collision avec le checkpoint 1 pour bot
        for self.Plateform in self.Check1:
            check_rect = pygame.Rect(750,550,20,20)
            if self.BotRect.colliderect(check_rect):
                self.Checkpoint2 = False
                self.Checkpoint1 = True

    def CollisionBot(self,player):

    # Déstruction d'un bot en sautant dessus
        bot_rect = pygame.Rect(self.posX,self.posY,self.Width, self.Height)
        player_rect = pygame.Rect(player.posX, player.posY, player.width, player.height)
        col = Collision.collision(player_rect,bot_rect)
        ColWeapon = Collision.collision(player.weaponRect, bot_rect)
        if col == 2 and player.isDashing == False:
            if self.hp == 0 :
                self.Checkpoint1 = False
                self.Checkpoint2 = False
                self.Height = 0
                self.Width = 0
                self.posX = -11111
                self.posY = -11111
                player.verticalVelocity = -player.jumpForce
            else:
                player.verticalVelocity = -player.jumpForce
                self.hurt = True
                self.hp -= 1

        if ColWeapon == 1 or ColWeapon == 4 or (self.BotDirection == -1 and col == 4 and player.isDashing == True) or (self.BotDirection == 1 and col == 1 and player.isDashing == True):
            if self.hp == 0:
                self.Checkpoint1 = False
                self.Checkpoint2 = False
                self.Height = 0
                self.Width = 0
                self.posX = -11111
                self.posY = -11111
            else :
                self.hp -= 1
                self.bothurt = True

        if (col != 0 and col != 2 and player.isDashing == False) or (col == 1 and player.isDashing == True and self.BotDirection == -1 ) or (col == 4 and player.isDashing == True and self.BotDirection == 1):
            if player.hp == 0:
                player.height = 0
                player.width = 0 
                player.posX = -11111
                player.posY = -11111
                self.attack = True
            else:
                player.hp -= 1
                self.attack = True
                self.invicible = 30 
                self.PlayerIncivible = True
                if self.BotDirection == 1:
                    player.posX -= -player.playerDirection * player.dashVelocity
                    player.posY = 0
                elif self.BotDirection == -1:
                    player.posX += -player.playerDirection * player.dashVelocity
                    player.posY = 0

        if self.PlayerIncivible:          
            self.invicible -= 1
            if self.invicible <= 20:
                self.PlayerIncivible = False
