from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self._email = email
        self._address = address

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def check_email(self):
        return '@' in self._email

    @abstractmethod
    def display_info(self):
        pass
