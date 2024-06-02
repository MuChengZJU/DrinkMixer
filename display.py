import pygame
from pygame.locals import *

class Display:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((800, 600))
        self.load_assets()
        self.font = pygame.font.Font('assets/fonts/HYWenHei-85W.ttf', 20)
        self.quit_button_rect = pygame.Rect(700, 0, 100, 40)  # 定义退出按钮的位置和大小
        self.ingredient_positions = {
            'base_coffee': (0, 350),
            'base_soda': (100, 350),
            'flavor_fruit': (200, 380),
            'flavor_gel': (325, 380),
            'flavor_mint': (450, 380),
            'extra_milk': (550, 350),
            'extra_tomato': (650, 350)
        }

    def load_assets(self):
        self.images = {}

        # 加载背景图
        self.background = pygame.image.load('assets/images/backgound.jpeg')
        # 获取窗口尺寸
        window_size = self.screen.get_size()
        # 调整背景图大小以适应窗口
        self.background = pygame.transform.scale(self.background, window_size)

        for name, path in {
            "base_coffee": 'assets/images/base_coffee.png',
            "base_soda": 'assets/images/base_soda.png',
            "flavor_fruit": 'assets/images/flavor_fruit.png',
            "flavor_gel": 'assets/images/flavor_gel.png',
            "flavor_mint": 'assets/images/flavor_mint.png',
            "extra_milk": 'assets/images/extra_milk.png',
            "extra_tomato": 'assets/images/extra_tomato.png',
            "mixing_cup": 'assets/images/mixing_cup.png',
            "redo_button": 'assets/images/redo_button.png'
        }.items():
            image = pygame.image.load(path)
            self.images[name] = pygame.transform.scale(image, (125, 125))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.game.running = False
            elif event.type == MOUSEBUTTONDOWN:
                self.handle_click(event.pos)

    def handle_click(self, pos):
        x, y = pos
        # 检查点击是否在退出按钮上
        if self.quit_button_rect.collidepoint(x, y):
            self.game.running = False
        # 检查点击是否在某个原料图标上
        elif self.is_click_on_ingredient(x, y):
            ingredient = self.get_clicked_ingredient(x, y)
            self.game.glass.add_ingredient(ingredient['type'], ingredient['name'])
        # 检查点击是否在重置按钮上
        elif self.is_click_on_reset_button(x, y):
            self.game.reset_game()
        # 检查点击是否在杯子上
        elif self.is_click_on_glass(x, y):
            if self.game.check_order():
                self.game.reset_game()
            else:
                self.game.glass.clear()

    def is_click_on_ingredient(self, x, y):
        # 用集中管理的原料位置来检查点击是否在某个原料图标上
        for name, (ix, iy) in self.ingredient_positions.items():
            if ix <= x <= ix + 100 and iy <= y <= iy + 100:
                return True
        return False

    def get_clicked_ingredient(self, x, y):
        # 根据点击的位置返回相应的原料信息
        for name, (ix, iy) in self.ingredient_positions.items():
            if ix <= x <= ix + 100 and iy <= y <= iy + 100:
                type_ = 'base' if 'base' in name else 'flavor' if 'flavor' in name else 'extra'
                return {'type': type_, 'name': name}
        return None

    def is_click_on_reset_button(self, x, y):
        if 700 <= x <= 750 and 500 <= y <= 550:
            return True
        return False

    def is_click_on_glass(self, x, y):
        if 400 <= x <= 500 and 300 <= y <= 400:
            return True
        return False

    def update(self):
        pass

    def render(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.draw_ingredients()
        self.draw_mixing_cup()
        self.draw_customer_order()
        self.draw_reset_button()
        self.draw_income()
        self.draw_state()
        self.draw_quit_button()
        pygame.display.flip()

    def draw_ingredients(self):
        # 在屏幕上绘制可选择的原料
        for name, (ix, iy) in self.ingredient_positions.items():
            self.screen.blit(self.images[name], (ix, iy))

    def draw_mixing_cup(self):
        self.screen.blit(self.images['mixing_cup'], (350, 350))

    def draw_customer_order(self):
        order_text = f"Order: {self.game.customer.order['base']}, {self.game.customer.order['flavor']}, {self.game.customer.order['extra']}"
        order_surface = self.font.render(order_text, True, (0, 0, 0))
        self.screen.blit(order_surface, (50, 40))

    def draw_reset_button(self):
        self.screen.blit(self.images['redo_button'], (700, 500))

    def draw_income(self):
        income_text = f"Income: {self.game.income}"
        income_surface = self.font.render(income_text, True, (0, 0, 0))
        self.screen.blit(income_surface, (50, 60))

    def draw_state(self):
        state_text = f"State: {self.game.glass.contents['base']}, {self.game.glass.contents['flavor']}, {self.game.glass.contents['extra']}"
        state_surface = self.font.render(state_text, True, (0, 0, 0))
        self.screen.blit(state_surface, (50, 80))

    def draw_quit_button(self):
        pygame.draw.rect(self.screen, (255, 246, 218), self.quit_button_rect)
        quit_text = self.font.render("退出游戏", True, (168, 128, 79))
        text_rect = quit_text.get_rect(center=self.quit_button_rect.center)
        self.screen.blit(quit_text, text_rect)