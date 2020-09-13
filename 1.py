import re

class NotValidDataError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Data:

    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day
        self.valid_data(self)

    @staticmethod
    def valid_data(self):
        days_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        if not (1 <= self.year):
            raise NotValidDataError
        elif not (1 <= self.month <= 12):
            raise NotValidDataError
        elif not (1 <= self.day <= days_dict.get(self.month)):
            raise NotValidDataError
        else: print("Ввод корректен.")

    @classmethod
    def set_data(cls, data):
        day, month, year = map(lambda x: int(x), data.split("-"))
        print(day, month, year)
        return cls(day, month, year)

Data.set_data("12-5-2004")
Data.set_data("13-13-2004")