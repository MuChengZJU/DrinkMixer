import pygame
from pygame.locals import *


class Display:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((800, 600))
        self.load_assets()
        self.font = pygame.font.Font('assets/fonts/HYWenHei-85W.ttf', 20)

        # 定义所有可交互元素的位置
        self.element_positions = {
            'buttons': {
                'quit_button': pygame.Rect(700, 0, 100, 40),
                'reset_button': pygame.Rect(700, 100, 70, 70),
                'mixing_cup': pygame.Rect(300, 280, 175, 175)
            },
            'ingredients': {
                'base_coffee': (0, 400),
                'base_soda': (100, 400),
                'flavor_fruit': (200, 430),
                'flavor_gel': (325, 430),
                'flavor_mint': (450, 430),
                'extra_milk': (550, 400),
                'extra_tomato': (650, 400)
            },
            'status':{
                'glass_content': (230, 310)
            }
        }

        # 定义变量名到中文名称的映射
        self.ingredient_names = {
            'base_coffee': '咖啡基底',
            'base_soda': '苏打基底',
            'flavor_fruit': '水果味',
            'flavor_gel': '果冻味',
            'flavor_mint': '薄荷味',
            'extra_milk': '额外牛奶',
            'extra_tomato': '额外番茄'
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
            # ingredients
            "base_coffee": 'assets/images/ingredients/base_coffee.png',
            "base_soda": 'assets/images/ingredients/base_soda.png',
            "flavor_fruit": 'assets/images/ingredients/flavor_fruit.png',
            "flavor_gel": 'assets/images/ingredients/flavor_gel.png',
            "flavor_mint": 'assets/images/ingredients/flavor_mint.png',
            "extra_milk": 'assets/images/ingredients/extra_milk.png',
            "extra_tomato": 'assets/images/ingredients/extra_tomato.png',
            # buttons
            "mixing_cup": 'assets/images/mixing_cup.png',
            "redo_button": 'assets/images/redo_button.png',
            "glass_content": "assets/images/glass_content.png",
            # icons
            "icon_base_coffee": 'assets/images/icons/icon_base_coffee.png',
            "icon_base_soda": 'assets/images/icons/icon_base_soda.png',
            "icon_flavor_fruit": 'assets/images/icons/icon_flavor_fruit.png',
            "icon_flavor_gel": 'assets/images/icons/icon_flavor_gel.png',
            "icon_flavor_mint": 'assets/images/icons/icon_flavor_mint.png',
            "icon_extra_milk": 'assets/images/icons/icon_extra_milk.png',
            "icon_extra_tomato": 'assets/images/icons/icon_extra_tomato.png',
        }.items():
            image = pygame.image.load(path)
            if name == "mixing_cup":
                # 调整mixing_cup图像大小
                self.images[name] = pygame.transform.scale(image, (175, 175))
            elif name == "redo_button":
                # 调整redo_button图像大小
                self.images[name] = pygame.transform.scale(image, (70, 70))
            elif name.startswith('icon'):
                # 调整icon图像大小
                self.images[name] = pygame.transform.scale(image, (30, 30))
            else:
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
        if self.element_positions['buttons']['quit_button'].collidepoint(x, y):
            self.game.running = False
        # 检查点击是否在重置按钮上
        elif self.element_positions['buttons']['reset_button'].collidepoint(x, y):
            self.game.reset_game()
        # 检查点击是否在某个原料图标上
        elif self.is_click_on_ingredient(x, y):
            ingredient = self.get_clicked_ingredient(x, y)
            self.game.glass.add_ingredient(ingredient['type'], ingredient['name'])
        # 检查点击是否在杯子上
        elif self.element_positions['buttons']['mixing_cup'].collidepoint(x, y):
            if self.game.check_order():
                self.game.reset_game()
            else:
                self.game.glass.clear()

    def is_click_on_ingredient(self, x, y):
        # 用集中管理的原料位置来检查点击是否在某个原料图标上
        for name, (ix, iy) in self.element_positions['ingredients'].items():
            if ix <= x <= ix + 125 and iy <= y <= iy + 125:
                return True
        return False

    def get_clicked_ingredient(self, x, y):
        # 根据点击的位置返回相应的原料信息
        for name, (ix, iy) in self.element_positions['ingredients'].items():
            if ix <= x <= ix + 125 and iy <= y <= iy + 125:
                type_ = 'base' if 'base' in name else 'flavor' if 'flavor' in name else 'extra'
                return {'type': type_, 'name': name}
        return None

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
        # 在屏幕上绘制可选择的原料及其名称
        for name, (ix, iy) in self.element_positions['ingredients'].items():
            # 绘制原料图标
            self.screen.blit(self.images[name], (ix, iy))

            # 获取中文名称
            ingredient_label = self.ingredient_names.get(name, name)
            label_surface = self.font.render(ingredient_label, True, (255, 255, 255))
            label_rect = label_surface.get_rect(center=(ix + 62.5, 550))  # 图标中心下方
            self.screen.blit(label_surface, label_rect)

    def draw_mixing_cup(self):
        pos = self.element_positions['buttons']['mixing_cup']
        self.screen.blit(self.images['mixing_cup'], (pos.x, pos.y))

    def draw_customer_order(self):
        # 在屏幕上绘制顾客的饮品需求
        order_text = f"Order: {self.game.customer.order['base_adjective']}, {self.game.customer.order['flavor_adjective']}, {self.game.customer.order['extra_adjective']}"
        order_surface = self.font.render(order_text, True, (0, 0, 0))
        self.screen.blit(order_surface, (50, 40))

    def draw_reset_button(self):
        pos = self.element_positions['buttons']['reset_button']
        self.screen.blit(self.images['redo_button'], (pos.x, pos.y))

    def draw_income(self):
        income_text = f"Income: {self.game.income}"
        income_surface = self.font.render(income_text, True, (0, 0, 0))
        self.screen.blit(income_surface, (50, 60))

    def draw_state(self):
        # 绘制杯子的里的原料
        self.screen.blit(self.images['glass_content'], self.element_positions['status']['glass_content'])
        if self.game.glass.contents['base'] is not None:
            base_pos = list(self.element_positions['status']['glass_content'])
            base_pos[0] += 45
            base_pos[1] += 10
            base_pos = tuple(base_pos)
            if self.game.glass.contents['base'] == 'base_coffee':
                self.screen.blit(self.images['icon_base_coffee'], base_pos)
            elif self.game.glass.contents['base'] == 'base_soda':
                self.screen.blit(self.images['icon_base_soda'], base_pos)
        if self.game.glass.contents['flavor'] is not None:
            flavor_pos = list(self.element_positions['status']['glass_content'])
            flavor_pos[0] += 45
            flavor_pos[1] += 50
            flavor_pos = tuple(flavor_pos)
            if self.game.glass.contents['flavor'] == 'flavor_fruit':
                self.screen.blit(self.images['icon_flavor_fruit'], flavor_pos)
            elif self.game.glass.contents['flavor'] == 'flavor_gel':
                self.screen.blit(self.images['icon_flavor_gel'], flavor_pos)
            elif self.game.glass.contents['flavor']== 'flavor_mint':
                self.screen.blit(self.images['icon_flavor_mint'], flavor_pos)
        if self.game.glass.contents['extra'] is not None:
            extra_pos = list(self.element_positions['status']['glass_content'])
            extra_pos[0] += 45
            extra_pos[1] += 90
            extra_pos = tuple(extra_pos)
            if self.game.glass.contents['extra'] == 'extra_milk':
                self.screen.blit(self.images['icon_extra_milk'], extra_pos)
            elif self.game.glass.contents['extra'] == 'extra_tomato':
                self.screen.blit(self.images['icon_extra_tomato'], extra_pos)

    def draw_quit_button(self):
        pos = self.element_positions['buttons']['quit_button']
        pygame.draw.rect(self.screen, (255, 246, 218), pos)
        quit_text = self.font.render("退出游戏", True, (168, 128, 79))
        text_rect = quit_text.get_rect(center=pos.center)
        self.screen.blit(quit_text, text_rect)