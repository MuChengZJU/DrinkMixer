import pygame
from customer import Customer
from glass import Glass
from sound import SoundManager
from display import Display
import random
from sound import SoundManager

class Game:
    def __init__(self):
        self.sound = SoundManager()
        self.running = True
        self.income = 0
        self.customers = []
        self.glass = Glass()
        pygame.display.set_caption("Drink Mixer")  # 设置窗口标题
        self.clock = pygame.time.Clock()  # 创建一个Clock对象
        self.display = Display(self)
        for i in range(10):
           self.customers.append(Customer())
        if not hasattr(self, "static_var"):
           self.customer = self.customers[0]
           self.i = 0
    def reset_game(self):  # 重置游戏状态
        self.glass = Glass()
        self.customers.pop(0)  # 移除已完成的客户
        self.customers.append(Customer())  # 在列表末尾添加新的客户
        self.customer = self.customers[0]  # 更新当前客户
        self.sound.play_sound("klee")  # 在订单刷新时播放"klee"的音效


    def reset_glass(self):  # 重置杯子状态
        self.glass = Glass()


    def check_order(self):
        if self.glass.is_correct(self.customer):
            self.income += self.customer.price  # random.randint(9, 30);
            return True
        self.income -= 5  # 做错了倒扣
        return False

    def run(self):
        while self.running:
            self.display.handle_events()
            self.display.update()
            self.display.render()
            self.clock.tick(60)  # 设置帧率为60 FPS
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()