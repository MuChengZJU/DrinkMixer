import random

class Customer:
    def __init__(self):
        self.order = self.generate_order()
        self.price = self.calculate_price()

    def generate_order(self):
        bases = ["base_coffee", "base_soda"]
        flavors = ["flavor_fruit", "flavor_gel", "flavor_mint"]
        extras = ["extra_milk", "extra_tomato"]
        return {
            "base": random.choice(bases),
            "flavor": random.choice(flavors),
            "extra": random.choice(extras)
        }
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