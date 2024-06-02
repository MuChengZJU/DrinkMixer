import pygame
from customer import Customer
from glass import Glass
from sound import SoundManager
from display import Display
import random

class Game:
    def __init__(self):
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
        self.i += 1
        self.customer = self.customers[self.i]

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