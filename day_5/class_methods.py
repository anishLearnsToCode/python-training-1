import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string: str):
        first_name, last_name, age = string.split('-')
        return Employee(first_name, last_name, age)

    @staticmethod
    def is_work_day(day):
        if day.weekday() in (5, 6):
            return False
        return True


class Developer(Employee):
    def __init__(self, first_name, last_name, age, language):
        super().__init__(first_name, last_name, age)
        self.language = language


anish = Developer(first_name='Anish', last_name='Sachdeva', age=22, language='Java')
ada = Developer(first_name='Ada', last_name='Lovelace', age=30, language='Python')


print(ada.language)
