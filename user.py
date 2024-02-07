from base import BaseClass

class User(BaseClass):
    def __init__(self, first_name: str, last_name: str, phone_number: str, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)

    @property
    def fullname(self):
        return f'{self.first_name.title()} {self.last_name}'