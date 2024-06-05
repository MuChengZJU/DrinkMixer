import random


class Customer:
    def __init__(self):
        self.ingredients = {
            "base": {
                "base_coffee": ["香浓醇厚", "苦味提神"],
                "base_soda": ["清新爽口", "刺激轻盈"]
            },
            "flavor": {
                "flavor_fruit": ["多汁果香", "新鲜营养"],
                "flavor_gel": ["软滑粘性", "弹性有趣"],
                "flavor_mint": ["清凉提神", "清新辛辣"]
            },
            "extra": {
                "extra_milk": ["香甜顺滑", "营养奶香"],
                "extra_tomato": ["酸甜浓郁", "粘稠奇特"]
            }
        }
        self.namelist = {
            "anya", "frieren", "furina", "klee", "nwlt", "violet"
        }
        self.namelist_cn = {
            'anya': '阿尼亚',
            'frieren': '芙莉莲',
            'furina': '芙宁娜',
            'klee': '可莉',
            'nwlt': '那维莱特',
            'violet': '薇鹅莉特'
        }
        self.name = self.generate_name()
        self.order = self.generate_order()
        self.price = self.calculate_price()

    def generate_order(self):
        if (self.name == "anya"):
            order = {
                "base": "base_coffee",
                "flavor": "flavor_fruit",
                "extra": "extra_milk"
            }
        if (self.name == "frieren"):
            order = {
                "base": "base_coffee",
                "flavor": "flavor_fruit",
                "extra": "extra_milk"
            }
        if (self.name == "furina"):
            order = {
                "base": "base_soda",
                "flavor": "flavor_fruit",
                "extra": "extra_milk"
            }
        if (self.name == "klee"):
            order = {
                "base": "base_coffee",
                "flavor": "flavor_gel",
                "extra": "extra_tomato"
            }
        if (self.name == "nwlt"):
            order = {
                "base": "base_soda",
                "flavor": "flavor_gel",
                "extra": "extra_milk"
            }
        if (self.name == "violet"):
            order = {
                "base": "base_soda",
                "flavor": "flavor_mint",
                "extra": "extra_tomato"
            }
        # 随机选择形容词
        order["base_adjective"] = random.choice(self.ingredients["base"][order["base"]])
        order["flavor_adjective"] = random.choice(self.ingredients["flavor"][order["flavor"]])
        order["extra_adjective"] = random.choice(self.ingredients["extra"][order["extra"]])
        return order

    def generate_name(self):
        name = random.choice(list(self.namelist))
        return name

    def calculate_price(self):
        price = 0
        if self.order["base"] == "base_coffee":
            price += 5
        elif self.order["base"] == "base_soda":
            price += 4
        if self.order["flavor"] == "flavor_fruit":
            price += 5
        elif self.order["flavor"] == "flavor_gel":
            price += 3
        else:
            price += 2
        if self.order["extra"] == "extra_milk":
            price += 1;
        else:
            price += 2
        return price;
