import pygame
from pygame.locals import *
from sound import SoundManager
class Display:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((800, 600))
        self.load_assets()
        self.font = pygame.font.Font('assets/fonts/HYWenHei-85W.ttf', 20)
        self.sound = SoundManager()

        # 定义所有可交互元素的位置
        self.element_positions = {
            'buttons': {
                'quit_button': pygame.Rect(700, 0, 100, 40),
                'redo_button': pygame.Rect(450, 320, 70, 70),
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
                'glass_content': (230, 310),
                'income': (600, 50)
            }
        }

        # 定义变量名到中文名称的映射
        self.ingredient_names = {
            'base_coffee': '咖啡基底',
            'base_soda': '苏打基底',
            'flavor_fruit': '水果味',
            'flavor_gel': '果冻味',
            'flavor_mint': '薄荷味',
            'extra_milk': '牛奶',
            'extra_tomato': '番茄'
        }

        # 订单队列和客户
        self.element_positions['order_queue'] = (600, 200)  # 队列起始位置
        self.element_positions['klee'] = (0, 100)  # 客户照片位置

    def load_assets(self):
        self.images = {}

        # 加载背景图
        self.background = pygame.image.load('assets/images/background.jpeg')
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
            # others
            "mixing_cup": 'assets/images/mixing_cup.png',
            "redo_button": 'assets/images/redo_button.png',
            "glass_content": "assets/images/glass_content.png",
            "income": "assets/images/income.png",
            # icons
            "icon_base_coffee": 'assets/images/icons/icon_base_coffee.png',
            "icon_base_soda": 'assets/images/icons/icon_base_soda.png',
            "icon_flavor_fruit": 'assets/images/icons/icon_flavor_fruit.png',
            "icon_flavor_gel": 'assets/images/icons/icon_flavor_gel.png',
            "icon_flavor_mint": 'assets/images/icons/icon_flavor_mint.png',
            "icon_extra_milk": 'assets/images/icons/icon_extra_milk.png',
            "icon_extra_tomato": 'assets/images/icons/icon_extra_tomato.png',
            # customers
            "klee": "assets/images/customers/klee.png",
            "frieren": "assets/images/customers/frieren.png",
            "furina": "assets/images/customers/furina.png",
            "klee": "assets/images/customers/klee.png",
            "nwlt": "assets/images/customers/nwlt.png",
            "violet": "assets/images/customers/violet.png"
        }.items():
            image = pygame.image.load(path)
            if name == "mixing_cup":
                # 调整mixing_cup图像大小
                self.images[name] = pygame.transform.scale(image, (175, 175))
            elif name == "redo_button":
                # 调整redo_button图像大小
                self.images[name] = pygame.transform.scale(image, (60, 60))
            elif name.startswith('icon'):
                # 调整icon图像大小
                self.images[name] = pygame.transform.scale(image, (30, 30))
            elif name == "income":
                # 调整收入板图像大小
                self.images[name] = pygame.transform.scale(image, (200, 100))
            elif name in ["klee", "frieren", "furina", "klee", "nwlt", "violet"]:
                # 调整顾客图像大小
                self.images[name] = pygame.transform.scale(image, (300, 300))
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
        elif self.element_positions['buttons']['redo_button'].collidepoint(x, y):
            self.game.reset_game()
        # 检查点击是否在某个原料图标上
        elif self.is_click_on_ingredient(x, y):
            ingredient = self.get_clicked_ingredient(x, y)
            self.game.glass.add_ingredient(ingredient['type'], ingredient['name'])
            # 播放音效
            self.sound.play_sound(ingredient['name'])
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
        self.draw_redo_button()
        self.draw_income()
        self.draw_state()
        self.draw_quit_button()
        self.draw_order_queue()  # 绘制订单队列
        self.draw_current_customer()  # 绘制当前客户信息
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

    def draw_redo_button(self):
        pos = self.element_positions['buttons']['redo_button']
        self.screen.blit(self.images['redo_button'], (pos.x, pos.y))
        redo_text = self.font.render("重做这杯", True, (168, 128, 79))
        text_rect = redo_text.get_rect(center=(pos.centerx, pos.centery + pos.height / 2))
        self.screen.blit(redo_text, text_rect)
        redo_text = self.font.render("重做这杯", True, (255, 246, 218))
        text_rect.x -= 2
        text_rect.y -= 2
        self.screen.blit(redo_text, text_rect)

    def draw_income(self):
        # 绘制收入板
        self.screen.blit(self.images['income'], self.element_positions['status']['income'])
        # 绘制收入文本
        income_line1 = f"收入"
        income_line2 = f"{self.game.income} 信用点"

        income_surface1 = self.font.render(income_line1, True, (255, 246, 218))
        income_text_pos1 = list(self.element_positions['status']['income'])
        income_text_pos1[0] += 85
        income_text_pos1[1] += 25
        income_text_pos1 = tuple(income_text_pos1)
        self.screen.blit(income_surface1, income_text_pos1)

        income_surface2 = self.font.render(income_line2, True, (255, 246, 218))
        income_text_pos2 = list(self.element_positions['status']['income'])
        income_text_pos2[0] += 70
        income_text_pos2[1] += 56  # 第二行文本的高度为30
        income_text_pos2 = tuple(income_text_pos2)
        self.screen.blit(income_surface2, income_text_pos2)

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
            elif self.game.glass.contents['flavor'] == 'flavor_mint':
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

    def draw_order_queue(self):
        y_offset = 0
        for customer in self.game.customers[:5]:  # 只绘制列表中的前5个客户的订单
            order_text = f"{customer.order['base_adjective']}, {customer.order['flavor_adjective']}, {customer.order['extra_adjective']}"
            order_surface = self.font.render(order_text, True, (0, 0, 0))
            self.screen.blit(order_surface, (
            self.element_positions['order_queue'][0], self.element_positions['order_queue'][1] + y_offset))
            y_offset += 30  # 每个订单之间的间隔

    def draw_current_customer(self):
        # 绘制客户照片
        self.screen.blit(self.images['klee'], self.element_positions['klee'])
        # 绘制客户订单
        order_text = f"可莉想要{self.game.customer.order['base_adjective']}的, {self.game.customer.order['flavor_adjective']}的, {self.game.customer.order['extra_adjective']}的饮料！"
        order_surface = self.font.render(order_text, True, (0, 0, 0))
        self.screen.blit(order_surface, (
        self.element_positions['klee'][0] + 50, 50))  # 在照片上方显示订单
        # TODO: 客户变量

