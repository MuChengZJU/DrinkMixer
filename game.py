## @file game.py
#  @brief 包含 Game 类，负责游戏的核心逻辑和流程控制。

import pygame
from customer import Customer
from glass import Glass
from sound import SoundManager
from display import Display
import time


class Game:
    ## @brief 初始化 Game 对象。
    #  设置游戏初始状态、加载资源并创建客户队列。
    def __init__(self):
        self.sound = SoundManager()
        self.running = True
        self.income = 0
        self.customers = []
        self.glass = Glass()
        pygame.display.set_caption("求是创新奶茶店")  # 设置窗口标题
        self.clock = pygame.time.Clock()  # 创建一个 Clock 对象
        self.display = Display(self)
        for i in range(10):
            self.customers.append(Customer())
        if not hasattr(self, "static_var"):
            self.customer = self.customers[0]

    ## @brief 重置游戏状态。
    #  重置杯子、更新客户队列并播放音效。
    def reset_game(self):
        self.glass = Glass()
        self.customers.pop(0)  # 移除已完成的客户
        # self.customers.append(new Customer())  # 在列表末尾添加新的客户
        time.sleep(5)
        self.customer = self.customers[0]  # 更新当前客户
        self.sound.play_sound(self.customer.name + "_come")  # 在订单刷新时播放的音效

    ## @brief 重置杯子状态。
    def reset_glass(self):
        self.glass = Glass()

    ## @brief 检查客户订单是否正确。
    #  @return 如果订单正确，增加收入并返回 True，否则减少收入并返回 False。
    def check_order(self):
        if self.glass.is_correct(self.customer):
            self.income += self.customer.price  # random.randint(9, 30);
            self.sound.play_sound(self.customer.name + "_succ")  # 播放成功音效
            return True
        else:
            self.sound.play_sound(self.customer.name + "_fail")  # 播放失败音效
            self.income -= 5  # 做错了倒扣
            return False

    ## @brief 运行游戏主循环。
    def run(self):
        while self.running:
            self.display.handle_events()
            self.display.update()
            self.display.render()
            self.clock.tick(60)  # 设置帧率为 60 FPS
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
