import pygame
from customer import Customer
from glass import Glass
from display import Display
import random

class Game:
    def __init__(self):  # init 好像是初始化
        self.running = True
        self.income = 0
        self.customer = Customer()
        self.glass = Glass()
        self.display = Display(self)

    def reset_game(self):  # 重置游戏状态
        self.glass = Glass()
        self.customer = Customer()

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
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()