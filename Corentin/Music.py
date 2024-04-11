import pygame

pygame.init()
pygame.mixer.init()

s_width : float = 1600
s_height : float = 900

screen = pygame.display.set_mode((s_width, s_height))

class Sound:

    def __init__(self):
        
        self.soundThemeList : list = ['Corentin/MusicBank/OST_Jeux_Main_Menu.mp3', 'MusicBank/Athena.mp3', 'MusicBank/a_travers_la_Grece.mp3', 'MusicBank/Pour_Aglae.mp3']

        #soubdSFXList : [Dash, Jump, Death]
        self.soundSFXList : list = ['MusicBank/dash.mp3', 'MusicBank/Jump.mp3', 'MusicBank/roblox-death-sound-effect.mp3']

        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)

        self.isPlaying : bool = True

        self.x = 0

    def StartTheme(self, index):
        themePlay = self.soundThemeList[index]
        pygame.mixer.music.load(themePlay)
        pygame.mixer.music.play()
        self.isPlaying = True

    def TryRelaunchTheme(self, index):
        if self.IsBusy():
            return
        
        self.StartTheme(index)

    def IsBusy(self):
        return pygame.mixer.music.get_busy()

    def StopTheme(self, isPlaying):
        return isPlaying == False
    
    def StartAnSFX(self, index, isPlaying):

        fxPlay = self.soundSFXList[index]
        print(self.soundSFXList[index])

        pygame.mixer.music.load(fxPlay)
        pygame.mixer.music.play()

        while isPlaying:

            if pygame.mixer.music.get_busy():
                continue
            else :
                isPlaying == False
      



    
sound = Sound()

sound.StartTheme(0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        sound.StartAnSFX(0, sound.isPlaying)
    
    sound.TryRelaunchTheme(0)

