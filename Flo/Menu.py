import pygame as py

class Menu :
    def __init__(self, width, height):
        self.x = width/8*2
        self.y = height/6
        self.size = [(width/8)*4,height/6*4]
        self.size_button = [self.size[0]/5*2,self.size[1]/8]
        self.x_button = 0
        self.y_restart = 0
        self.y_option = 0
        self.y_quit = 0
        #Condition
        self.option_status = False

    def update_size(self, w, h):
        self.x = w/8*2
        self.y = h/6
        self.size = [(w/8)*4,h/6*4]
        self.x_button = self.x + self.size[0]/3
        self.size_button = [self.size[0]/3,self.size[1]/8]
    
    def test_collide(self,posY):
        pos_mouse = py.mouse.get_pos()
        if (self.x_button <= pos_mouse[0] <= self.x_button+self.size_button[0]) and (posY <= pos_mouse[1] <= posY + self.size_button[1]) :
            return True
        return False
    
    def button_restart(self):
        self.y_restart = self.y + self.size[1]/8*2
        if self.test_collide(self.y_restart):
            restart = py.image.load("Flo/Button/RESTART1.png")
        else :
            restart = py.image.load("Flo/Button/RESTART.png")
        newrestart = py.transform.scale(restart,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_restart,self.size_button[0],self.size_button[1]))
        fen.blit(newrestart,(self.x_button,self.y_restart))

    def button_option(self) :
        self.y_option = self.y + self.size[1]/8*4
        if self.test_collide(self.y_option):
            option = py.image.load("Flo/Button/OPTION1.png")
        else :
            option = py.image.load("Flo/Button/OPTION.png")
        newoption = py.transform.scale(option,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_option,self.size_button[0],self.size_button[1]))
        fen.blit(newoption,(self.x_button,self.y_option))
    
    def button_quit(self) :
        self.y_quit = self.y + self.size[1]/8*6
        if self.test_collide(self.y_quit):
            quit = py.image.load("Flo/Button/QUIT1.png")
        else :
            quit = py.image.load("Flo/Button/QUIT.png")
        newquit = py.transform.scale(quit,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_quit,self.size_button[0],self.size_button[1]))
        fen.blit(newquit,(self.x_button,self.y_quit))

    def menu_pause(self):
        py.draw.rect(fen, (255,255,255),(self.x,self.y,self.size[0],self.size[1]))
        if not self.option_status :
            self.button_restart()
            self.button_option()
            self.button_quit()

    


w_screen = 800
h_screen = 600
fen = py.display.set_mode((w_screen, h_screen),py.RESIZABLE)
clock = py.time.Clock()
menu = Menu(w_screen,h_screen)
continuer = True

while continuer :
    
    for event in py.event.get():
        if event.type == py.QUIT:
            continuer = False
        elif event.type == py.KEYDOWN :
            if event.key == py.K_p :
                continuer = False
        elif event.type == py.VIDEORESIZE :
            w_screen, h_screen = event.w, event.h
            fen = py.display.set_mode((w_screen, h_screen),py.RESIZABLE)
    menu.update_size(w_screen,h_screen)
    menu.menu_pause()
    py.display.flip()
    clock.tick(60)