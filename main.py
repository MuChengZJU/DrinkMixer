import pygame
from game import Game

def main():
    # 初始化 Pygame
    pygame.init()

    # 创建游戏实例
    game = Game()

    # 启动游戏循环
    game.run()

if __name__ == "__main__":
    main()