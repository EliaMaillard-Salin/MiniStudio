import pygame as py

class mouvement : 
    def __init__(self,x,y,h,l,c,e) -> None:
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.color = c
        self.epaiseur = e

    def mov(self,right) :
        self.x += right*5

    def jump(self, v) :
         for _ in range(10) :
             self.y -= 2
             self.x += 1*v
             fen.fill(115,115,115)
             py.draw.rect(fen, self.color,(self.x,self.y,self.width,self.height))
             py.

         pass

py.init()

# Taille Fenêtre 
largeur = 1000
hauteur = 800

# Couleur 
GRIS = (150, 150, 150)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)

# Variable
pos_x = 0
pos_y = hauteur - 200

fen = py.display.set_mode((largeur, hauteur))
# image_ballon = py.image.load("ballon.png")

continuer = True
while continuer :
    fen.fill(GRIS)
    for event in py.event.get():
        pressed = py.key.get_pressed()
        if event.type == py.QUIT:
            continuer = False
        if pressed[py.K_d]:
            pos_x = pos_x + 1
        if pressed[py.K_q] :
            pos_x = pos_x - 1
        if pressed[py.K_z] : 
            pos_y = pos_y - 2
       # if event.type == py.KEYDOWN :
            
    
    py.draw.line(fen, BLEU, (pos_x,pos_y), (pos_x,pos_y), 30) # (Fenêtre, couleur, point de départ, poin d'arriver, épaiseur)
    #  fen.blit(image_ballon, (pos_x, 200)) # (image, position(x,y))
    py.display.flip()  # Actualise la page 
py.quit()
