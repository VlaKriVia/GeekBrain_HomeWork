from abc import ABC, abstractmethod

class Stock:

    def __init__(self, length, width, high):
        self.length = length
        self.width = width
        self.high = high
        self.size = length*width*high
        self.storage_equipment = {"scanner" : 0, "printer" : 0, "copier" : 0}

    @classmethod
    def set_stonk(cls, data):
        length, width, high = map(lambda x: int(x), data.split())
        return cls(length, width, high)

    def add_equipment(self, equipment):
        self.storage_equipment.update({equipment : self.storage_equipment.get(equipment)+1})
        print(f"Произведена отправка оборудования типа {equipment} на склад.")

    def send_equipment(self, equipment, office):
        if 0 <= self.storage_equipment.get(equipment):
            self.storage_equipment.update({equipment: self.storage_equipment.get(equipment) - 1})
            print(f"Произведена отправка оборудования типа {equipment} в оффис {office}.")
        else: print("Даный тип оборудования отсутсвует на складе.")

    def __str__(self):
        return f"length - {self.length}, width - {self.width}, high - {self.high}, size - {self.size}, storage equipment - {self.storage_equipment}"

class OfficeEquipment(ABC):

    @abstractmethod
    def __init__(self, type_equipment, length, width, high):
        self.type_equipment = type_equipment
        self.length = length
        self.width = width
        self.high = high
        self.size = length * width * high

    def __str__(self):
        return f"type - {self.type_equipment}, length - {self.length}, width - {self.width}, high - {self.high}, size - {self.size}"

class Scanner(OfficeEquipment):

    def __init__(self):
        self.type_equipment = "scanner"
        self.length = 40
        self.width = 30
        self.high = 5
        self.size = self.length * self.width * self.high

class Printer(OfficeEquipment):

    def __init__(self):
        self.type_equipment = "printer"
        self.length = 30
        self.width = 40
        self.high = 25
        self.size = self.length * self.width * self.high

class Copier(OfficeEquipment):

    def __init__(self):
        self.type_equipment = "copier"
        self.length = 50
        self.width = 30
        self.high = 20
        self.size = self.length * self.width * self.high

S_1 = Stock.set_stonk("100000 50000 20000")
print(S_1)
S_1.add_equipment("scanner")
print(S_1)
S_1.add_equipment("copier")
S_1.add_equipment("printer")
S_1.send_equipment("printer", "office_1")
print(S_1)