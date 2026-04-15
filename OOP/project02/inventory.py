class Inventory:
    def __init__(self, name="", stock=0):
        self.__name = name
        self.__stock = stock

    @property
    def name(self):
        return self.__name

    @property
    def stock(self):
        return self.__stock

    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount

    def remove_stock(self, amount):
        if amount > 0 and amount <= self.stock:
            self.__stock -= amount
