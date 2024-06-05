## @file sound.py
#  @brief 包含 SoundManager 类，负责加载和播放游戏的音效和背景音乐。

import pygame


class SoundManager:
    ## @brief 初始化 SoundManager 对象。
    #  初始化音频系统并加载音效文件和背景音乐。
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

        # 加载音效文件
        self.load_sounds()

        # 加载并播放背景音乐
        self.play_background_music('assets/sounds/background_music.mp3')

    ## @brief 加载所有音效文件。
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

    ## @brief 播放指定名称的音效。
    #  @param name 音效名称。
    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    ## @brief 播放背景音乐。
    #  @param path 背景音乐文件路径。
    def play_background_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)  # -1 表示无限循环播放
