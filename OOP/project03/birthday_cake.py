from bakery import Bakery


class BirthdayCake(Bakery):
    def __init__(self, message, pound, flavor="", unit_price=0):
        super().__init__(flavor, unit_price)
        self.message = message
        self.pound = pound

    def get_message(self):
        return self.message

    def change_message(self, new_message):
        self.message = new_message

    def __str__(self):
        total_price = self.get_unit_price() * self.pound

        return (
            f"{super().__str__()}\n"
            f"{self.get_flavor()} birthday cake (message={self.get_message()})\n"
            f"Total price of Birhtday Cake = {total_price}"
        )
