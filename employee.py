from person import Person

class Employee(Person):
    def __init__(self, name, email, salary, address):
        super().__init__(name, email, address)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    def display_info(self):
        return f"Employee: {self.name}, Email: {self._email}, Salary: {self.__salary}, Address: {self._address}"
