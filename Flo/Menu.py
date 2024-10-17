import pygame as py

class Menu :
    def __init__(self, width, height):
        self.x = width/8*2
        self.y = height/6
        self.size = [(width/8)*4,height/6*4]
        self.size_button = [self.size[0]/5*2,self.size[1]/7]
        self.x_button = 0
        self.y_restart = 0
        self.y_option = 0
        self.y_quit = 0
        self.size_square = [30,30]
        self.x_square_sound = self.x + self.size[0]/9 - self.size_square[0]//2
        self.y_square_sound = self.y + self.size[1]/7*2
        self.width_sound = self.size[0]/9*8
        self.pos_on_sound = 0
        self.x_mouse = py.mouse.get_pos()[0]
        self.volume = self.pos_on_sound / self.width_sound

        #Condition
        self.status_pause = False
        self.option_status = False
        self.quit = False
        #IMG QUIT
        self.img_quit1 = py.image.load("Flo/Button/QUIT1.png")
        self.img_quit = py.image.load("Flo/Button/QUIT.png")
        #IMG OPTION
        self.img_option1 = py.image.load("Flo/Button/OPTION1.png")
        self.img_option = py.image.load("Flo/Button/OPTION.png")
        #IMG RESTART
        self.img_restart1 = py.image.load("Flo/Button/RESTART1.png")
        self.img_restart = py.image.load("Flo/Button/RESTART.png")

    def update(self, w, h):
        self.x = w/8*2
        self.y = h/6
        self.size = [(w/8)*4,h/6*4]
        self.x_button = self.x + self.size[0]/3
        self.size_button = [self.size[0]/3,self.size[1]/7]
        self.x_square_sound = self.x + self.size[0]/9 - self.size_square[0]//2
        self.y_square_sound = self.y + self.size[1]/7*2
        self.width_sound = self.size[0]/9*8
        self.x_mouse = py.mouse.get_pos()[0]
        self.volume = self.pos_on_sound / self.width_sound
    
    def test_collide(self,posY):
        pos_mouse = py.mouse.get_pos()
        if (self.x_button <= pos_mouse[0] <= self.x_button+self.size_button[0]) and (posY <= pos_mouse[1] <= posY + self.size_button[1]) :
            return True
        return False
    
    def button_restart(self,fen):
        self.y_restart = self.y + self.size[1]/7
        if self.test_collide(self.y_restart):
            newrestart = py.transform.scale(self.img_restart1,(self.size_button[0],self.size_button[1]))
        else :
            newrestart = py.transform.scale(self.img_restart,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_restart,self.size_button[0],self.size_button[1]))
        fen.blit(newrestart,(self.x_button,self.y_restart))

    def button_option(self,fen) :
        self.y_option = self.y + self.size[1]/7*3
        if self.test_collide(self.y_option):
            newoption = py.transform.scale(self.img_option1,(self.size_button[0],self.size_button[1]))
        else :
            newoption = py.transform.scale(self.img_option,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_option,self.size_button[0],self.size_button[1]))
        fen.blit(newoption,(self.x_button,self.y_option))
    
    def button_quit(self,fen) :
        self.y_quit = self.y + self.size[1]/7*5
        if self.test_collide(self.y_quit):
            newquit = py.transform.scale(self.img_quit1,(self.size_button[0],self.size_button[1]))
        else :
            newquit = py.transform.scale(self.img_quit,(self.size_button[0],self.size_button[1]))
        
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_quit,self.size_button[0],self.size_button[1]))
        fen.blit(newquit,(self.x_button,self.y_quit))

    def movement_sound(self):
        pos_mouse = py.mouse.get_pos()
        if (self.x_square_sound <= pos_mouse[0] <= self.x_square_sound+self.size_square[0]) and (self.y_square_sound <= pos_mouse[1] <= self.y_square_sound + self.size_square[1]) :
            return True
        return False
    
    def sound(self, fen) :
        self.x_square_sound = self.x + self.size[0]/9+self.pos_on_sound
        self.y_square_sound = self.y + self.size[1]/7*2
        py.draw.rect(fen, (255,0,0),(self.x_square_sound,self.y_square_sound,self.size_square[0],self.size_square[1]))
        py.draw.rect(fen, (255,0,0),(self.x_square_sound-self.pos_on_sound,self.y_square_sound+(self.size_square[1]//3),self.width_sound+(self.size_square[0]//2),self.size_square[1]//3))

    def menu_pause(self,fen):
        if not self.option_status :
            self.button_restart(fen)
            self.button_option(fen)
            self.button_quit(fen)
        else :
            self.sound(fen)
            self.button_quit(fen)

    def pause(self,w,h,fen):
        for eventMenu in py.event.get():
            if eventMenu.type == py.MOUSEBUTTONDOWN :
                if eventMenu.button == 1 and self.test_collide(self.y_restart) and not self.option_status:
                    self.status_pause = False
                elif eventMenu.button == 1 and self.test_collide(self.y_option) and self.status_pause :
                    self.option_status = True
                elif eventMenu.button == 1 and self.test_collide(self.y_quit) and not self.option_status:
                    self.quit = True
                elif eventMenu.button == 1 and self.test_collide(self.y_quit) and self.option_status:
                    self.option_status = False
                
            elif eventMenu.type == py.VIDEORESIZE :
                w, h = eventMenu.w, eventMenu.h
                self.fen = py.display.set_mode((w, h),py.RESIZABLE)
        if py.mouse.get_pressed()[0] and self.movement_sound() and self.option_status:
            if py.mouse.get_pos()[0] < self.x_mouse :
                if self.volume > 0:
                    self.pos_on_sound -= self.x_mouse - py.mouse.get_pos()[0]
            if py.mouse.get_pos()[0] > self.x_mouse :
                if self.volume < 1: 
                    self.pos_on_sound += py.mouse.get_pos()[0] - self.x_mouse
            

        self.update(w,h)
        self.menu_pause(fen)





        