## @file glass.py
#  @brief 包含 Glass 类，用于管理杯子的状态和内容。

class Glass:
    ## @brief 初始化 Glass 对象。
    #  设置杯子的初始内容为空。
    def __init__(self):
        self.contents = {"base": None, "flavor": None, "extra": None}

    ## @brief 添加原料到杯子中。
    #  @param type 原料类型（基底、口味、额外）。
    #  @param ingredient 原料名称。
    def add_ingredient(self, type, ingredient):
        if self.contents[type] == None:
            if type in self.contents:
                self.contents[type] = ingredient

    ## @brief 清空杯子内容。
    def clear(self):
        self.contents = {"base": None, "flavor": None, "extra": None}

    ## @brief 检查当前杯子的内容是否符合客户的订单。
    #  @param customer 客户对象，包含订单信息。
    #  @return 如果杯子内容与订单一致，返回 True，否则返回 False。
    def is_correct(self, customer):
        for key in self.contents:
            if self.contents[key] != customer.order[key]:
                return False
        return True
