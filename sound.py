import pygame

class Sound:
    def __init__(self):
        self.load_sounds()
        self.background_music.play()

    def load_sounds(self):
        self.background_music = pygame.mixer.Sound('assets/sound/background_music.mp3')  # 加载背景音乐
        self.sound_click1 = pygame.mixer.Sound('assets/sound/click_sound1.mp3')  # 加载点击音效
        self.sound_click2 = pygame.mixer.Sound('assets/sound/click_sound2.mp3')