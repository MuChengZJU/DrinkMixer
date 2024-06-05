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
            # character voice
            'furina_come': 'assets/sounds/furina_come.mp3',
            'furina_fail': 'assets/sounds/furina_fail.mp3',
            'furina_succ': 'assets/sounds/furina_succ.mp3',
            'klee_come': 'assets/sounds/klee_come.ogg',
            'klee_fail': 'assets/sounds/klee_fail.mp3',
            'klee_succ': 'assets/sounds/klee_succ.mp3',
            'nwlt_come': 'assets/sounds/nwlt_come.mp3',
            'nwlt_fail': 'assets/sounds/nwlt_fail.mp3',
            'nwlt_succ': 'assets/sounds/nwlt_succ.mp3',
            'anya_come': 'assets/sounds/anya_come.mp3',
            'anya_fail': 'assets/sounds/anya_fail.mp3',
            'anya_succ': 'assets/sounds/anya_succ.mp3',
            'violet_come': 'assets/sounds/violet_come.mp3',
            'violet_fail': 'assets/sounds/violet_fail.mp3',
            'violet_succ': 'assets/sounds/violet_succ.mp3',
            'frieren_come': 'assets/sounds/frieren_come.mp3',
            'frieren_fail': 'assets/sounds/frieren_fail.mp3',
            'frieren_succ': 'assets/sounds/frieren_succ.mp3',
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