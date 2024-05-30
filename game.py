import pygame
from customer import Customer
from glass import Glass
from display import Display

class Game:
    def __init__(self):
        self.running = True
        self.income = 0
        self.customer = Customer()
        self.glass = Glass()
        self.display = Display(self)

    def reset_game(self):
        self.glass = Glass()
        self.customer = Customer()

    def check_order(self):
        if self.glass.is_correct(self.customer):
            self.income += 114
            return True
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