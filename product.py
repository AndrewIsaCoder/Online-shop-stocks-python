class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self._description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def check_quantity(self):
        return self.quantity >= 10
