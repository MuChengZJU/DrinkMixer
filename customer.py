import random

class Customer:
    def __init__(self):
        self.order = self.generate_order()

    def generate_order(self):
        bases = ["coffee", "soda"]
        flavors = ["fruit", "gel", "mint"]
        extras = ["milk", "tomato"]
        return {
            "base": random.choice(bases),
            "flavor": random.choice(flavors),
            "extra": random.choice(extras)
        }