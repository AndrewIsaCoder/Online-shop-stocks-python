from person import Person

class User(Person):
    def __init__(self, name, username, phone, address):
        super().__init__(name, username, address)
        self.phone = phone
        self.shopping_history = []

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def add_product(self, product):
        self.shopping_history.append(product)

    def total_spent(self):
        return sum(product.get_price() for product in self.shopping_history)

    def display_info(self):
        return f"User: {self.name}, Email: {self._email}, Phone: {self.phone}, Address: {self._address}, Total Spent: {self.total_spent()}"
