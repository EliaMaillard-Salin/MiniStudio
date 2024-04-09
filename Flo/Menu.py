import pygame as py

class Menu :
    def __init__(self, width, height):
        self.x = width/8*2
        self.y = height/6
        self.size = [(width/8)*4,height/6*4]
        self.size_button = [self.size[0]/5*2,self.size[1]/9]
        self.x_button = 0
        self.y_restart = 0
        self.y_save = 0
        self.y_option = 0
        self.y_quit = 0
        self.x_square_sound = width/8*2
        self.y_square_sound = 0
        #Condition
        self.status_pause = False
        self.option_status = False
        self.quit = False

    def update_size(self, w, h):
        self.x = w/8*2
        self.y = h/6
        self.size = [(w/8)*4,h/6*4]
        self.x_button = self.x + self.size[0]/3
        self.size_button = [self.size[0]/3,self.size[1]/9]
    
    def test_collide(self,posY):
        pos_mouse = py.mouse.get_pos()
        if (self.x_button <= pos_mouse[0] <= self.x_button+self.size_button[0]) and (posY <= pos_mouse[1] <= posY + self.size_button[1]) :
            return True
        return False
    
    def button_restart(self,fen):
        self.y_restart = self.y + self.size[1]/9
        if self.test_collide(self.y_restart):
            restart = py.image.load("Flo/Button/RESTART1.png")
        else :
            restart = py.image.load("Flo/Button/RESTART.png")
        newrestart = py.transform.scale(restart,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_restart,self.size_button[0],self.size_button[1]))
        fen.blit(newrestart,(self.x_button,self.y_restart))

    def button_save(self,fen):
            self.y_save = self.y + self.size[1]/9*3
            if self.test_collide(self.y_save):
                restart = py.image.load("Flo/Button/SAVE1.png")
            else :
                restart = py.image.load("Flo/Button/SAVE.png")
            newrestart = py.transform.scale(restart,(self.size_button[0],self.size_button[1]))
            py.draw.rect(fen, (255,0,0),(self.x_button,self.y_save,self.size_button[0],self.size_button[1]))
            fen.blit(newrestart,(self.x_button,self.y_save))

    def button_option(self,fen) :
        self.y_option = self.y + self.size[1]/9*5
        if self.test_collide(self.y_option):
            option = py.image.load("Flo/Button/OPTION1.png")
        else :
            option = py.image.load("Flo/Button/OPTION.png")
        newoption = py.transform.scale(option,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_option,self.size_button[0],self.size_button[1]))
        fen.blit(newoption,(self.x_button,self.y_option))
    
    def button_quit(self,fen) :
        self.y_quit = self.y + self.size[1]/9*7
        if self.test_collide(self.y_quit):
            quit = py.image.load("Flo/Button/QUIT1.png")
        else :
            quit = py.image.load("Flo/Button/QUIT.png")
        newquit = py.transform.scale(quit,(self.size_button[0],self.size_button[1]))
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_quit,self.size_button[0],self.size_button[1]))
        fen.blit(newquit,(self.x_button,self.y_quit))

    def square_sound(self, fen) :
        self.x_square_sound = self.x + self.size[0]/9
        self.y_square_sound = self.y + self.size[1]/9*3
        py.draw.rect(fen, (255,0,0),(self.x_button,self.y_save,30,30))
    def menu_pause(self,fen):
        if not self.option_status :
            self.button_restart(fen)
            self.button_save(fen)
            self.button_option(fen)
            self.button_quit(fen)
        else :
            self.square_sound(fen)
            
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
        self.update_size(w,h)
        self.menu_pause(fen)

