import pygame
from game import Game  # 从game.py里面引用class Game？


def main():
    # 初始化 Pygame 使用pygame之前必须执行的步骤。
    pygame.init()

    # 创建游戏实例  创建Game类的一个实例，并将其赋值给变量game
    game = Game()

    # 启动游戏循环 调用game实例的run方法来启动游戏的主循环
    game.run()

    # 如果当前脚本是作为主程序运行的，那么调用main函数，从而启动游戏


if __name__ == "__main__":
    main()
