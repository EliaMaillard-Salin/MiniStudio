import pygame

pygame.init()
pygame.mixer.init()

class Sound:

    def __init__(self):
        
        self.soundThemeList : list = ['MusicBank/OST_Jeux_Main_Menu.mp3', 'MusicBank/Athena.mp3', 'MusicBank/a_travers_la_Grece.mp3', 'MusicBank/Pour_Aglae.mp3']

        #soubdSFXList : [Dash, Jump, Death]
        self.soundSFXList : list = ['MusicBank/dash.mp3', 'MusicBank/Jump.mp3', 'MusicBank/roblox-death-sound-effect.mp3']

        self.isPlaying : bool = True

        self.x = 0

    def StartTheme(self, index, isPlaying):

        themePlay = self.soundThemeList[index]
        print(self.soundThemeList[index])

        pygame.mixer.music.load(themePlay)
        pygame.mixer.music.play()

        while isPlaying:

            if pygame.mixer.music.get_busy():
                continue
            else :
                pygame.mixer.music.play()

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

sound.StartTheme(1, sound.isPlaying)






