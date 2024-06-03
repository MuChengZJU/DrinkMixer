import random

class Customer:
    def __init__(self):
        self.ingredients = {
            "base": {
                "base_coffee": ["香浓", "苦味", "提神", "醇厚"],
                "base_soda": ["清新", "爽口", "刺激", "解渴", "轻盈"]
            },
            "flavor": {
                "flavor_fruit": ["多汁",  "果香", "新鲜", "营养丰富"],
                "flavor_gel": ["软滑", "粘性", "弹性", "有趣", "多彩"],
                "flavor_mint": ["清凉", "提神", "清新", "舒缓", "带有轻微的辛辣感"]
            },
            "extra": {
                "extra_milk": [ "香甜", "顺滑", "营养丰富", "奶香"],
                "extra_tomato": ["酸甜浓郁", "粘稠", "奇特创新"]
            }
        }
        self.namelist = {
            "anya", "frieren", "furina", "klee", "nwlt", "violet"
        }
        self.name = self.generate_name()
        self.order = self.generate_order()
        self.price = self.calculate_price()


    def generate_order(self):
        if(self.name=="anya"):
            order = {
                "base": "base_coffee",
                "flavor": "flavor_fruit",
                "extra": "extra_milk"
            }
        # order = {
        #     "base": random.choice(list(self.ingredients["base"].keys())),
        #     "flavor": random.choice(list(self.ingredients["flavor"].keys())),
        #     "extra": random.choice(list(self.ingredients["extra"].keys()))
        # }
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
        if self.order["base"] == "base_coffee":price += 5
        elif self.order["base"]=="base_soda":price += 4
        if self.order["flavor"]=="flavor_fruit": price += 5
        elif self.order["flavor"]=="flavor_gel": price += 3
        else: price += 2
        if self.order["extra"]=="extra_milk":price += 1;
        else: price += 2
        return price;