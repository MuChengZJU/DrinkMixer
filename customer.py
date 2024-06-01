import random

class Customer:
    def __init__(self):
        self.order = self.generate_order()

    def generate_order(self):
        bases = ["base_coffee", "base_soda"]
        flavors = ["flavor_fruit", "flavor_gel", "flavor_mint"]
        extras = ["extra_milk", "extra_tomato"]
        return {
            "base": random.choice(bases),
            "flavor": random.choice(flavors),
            "extra": random.choice(extras)
        }