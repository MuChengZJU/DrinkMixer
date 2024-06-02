import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

        # 加载音效文件
        self.load_sounds()

        # 加载并播放背景音乐
        self.play_background_music('assets/sounds/background_music.mp3')

    def load_sounds(self):
        sound_files = {
            "base_coffee": 'assets/sounds/base_coffee.wav',
            "base_soda": 'assets/sounds/base_soda.mp3',
            "extra_milk": 'assets/sounds/extra_milk.wav',
            "extra_tomato": 'assets/sounds/extra_tomato.wav',
            "flavor_fruit": 'assets/sounds/flavor_fruit.mp3',
            "flavor_gel": 'assets/sounds/flavor_gel.wav',
            "flavor_mint": 'assets/sounds/flavor_mint.mp3',
            "klee": 'assets/sounds/klee.mp3',
        }

        for name, path in sound_files.items():
            sound = pygame.mixer.Sound(path)
            self.sounds[name] = sound

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def play_background_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)  # -1 表示无限循环播放