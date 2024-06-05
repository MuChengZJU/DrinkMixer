class Glass:
    def __init__(self):
        self.contents = {"base": None, "flavor": None, "extra": None}

    def add_ingredient(self, type, ingredient):
        if self.contents[type] == None:
            if type in self.contents:
                self.contents[type] = ingredient

    def clear(self):
        self.contents = {"base": None, "flavor": None, "extra": None}

    def is_correct(self, customer):
        for key in self.contents:
            if self.contents[key] != customer.order[key]:
                return False
        return True
