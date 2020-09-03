from abc import abstractmethod

class Clothes:

    @abstractmethod
    def __init__(self):
        self.clothes = []

    @abstractmethod
    def __str__(self):
        return str(round(Clothes.calculate_fabric(self), 3))

    @abstractmethod
    def calculate_fabric(self):
        fabric = 0
        for i in self.clothes:
            fabric += i.calculate_fabric
        return fabric

    def add_new_clothes(self, clothes):
        self.clothes.append(clothes)

class Coat(Clothes):

    def __init__(self, size, amount=1):
        self.size = size
        self.amount = amount

    def __str__(self):
        return str(round(self.calculate_fabric, 3))

    @property
    def calculate_fabric(self):
        return self.amount * (self.size / 6.5 + 0.5)

class Suit(Clothes):

    def __init__(self, size, amount=1):
        self.size = size
        self.amount = amount

    def __str__(self):
        return str(round(self.calculate_fabric, 3))

    @property
    def calculate_fabric(self):
        return self.amount * (2 * self.size + 0.3)

class Sock(Clothes):

    def __init__(self, size, amount=1):
        self.size = size
        self.amount = amount

    def __str__(self):
        return str(round(self.calculate_fabric, 3))

    @property
    def calculate_fabric(self):
        return self.amount * (2 * self.size + 0.3)

Check = Clothes()
Check.add_new_clothes(Coat(65, 3))
Check.add_new_clothes(Suit(65))
print(Check)

Check.add_new_clothes(Coat(78))
Check.add_new_clothes(Coat(65, 10))
print(Check)