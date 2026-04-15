class Inventory:
    name = ""
    stock = 0

    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def get_name(self):
        return self.name

    def get_stock(self):
        return self.stock

    def add_stock(self, amount):
        if amount > 0:
            self.stock += amount

    def remove_stock(self, amount):
        if amount > 0 and amount <= self.stock:
            self.stock -= amount
