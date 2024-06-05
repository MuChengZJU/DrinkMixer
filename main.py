## @file main.py
#  @brief 游戏的入口文件，负责初始化并启动游戏。

import pygame
from game import Game  # 从 game.py 引用 Game 类


## @brief 主函数，初始化并启动游戏。
def main():
    # 初始化 Pygame 使用 pygame 之前必须执行的步骤。
    pygame.init()

    # 创建游戏实例 创建 Game 类的一个实例，并将其赋值给变量 game
    game = Game()

    # 启动游戏循环 调用 game 实例的 run 方法来启动游戏的主循环
    game.run()


# 如果当前脚本是作为主程序运行的，那么调用 main 函数，从而启动游戏
if __name__ == "__main__":
    main()
