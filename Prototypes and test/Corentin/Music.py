import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(8) #valeur de base = 8

s_width : float = 1600
s_height : float = 900

screen = pygame.display.set_mode((s_width, s_height))

class Sound:

    def __init__(self):
        
        self.soundThemeList : list = ['Corentin/MusicBank/OST_Jeux_Main_Menu.mp3', 'MusicBank/Athena.mp3', 'MusicBank/a_travers_la_Grece.mp3', 'MusicBank/Pour_Aglae.mp3']

        #soubdSFXList : [Dash, Jump, Death]
        self.soundSFXList : list = ['Corentin/MusicBank/dash.mp3', 'Corentin/MusicBank/Jump.mp3', 'Corentin/MusicBank/roblox-death-sound-effect.mp3']

        self.channel1 = pygame.mixer.Channel(1)
        self.channel2 = pygame.mixer.Channel(2)

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
    

    
    def StartAnSFX(self, index):

        sfxPlay = self.soundSFXList[index]
        print(self.soundSFXList[index])

        pygame.mixer.music.load(sfxPlay)
        pygame.mixer.music.play()

sound = Sound()

sound.StartTheme(0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        sound.StartAnSFX(1)
    
    sound.TryRelaunchTheme(0)

