class Worker:

    def __init__(self, name, surname, position, wage, bonuse):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage" : wage, "bonuse" : bonuse}

class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name + self.surname}")

    def get_total_income(self):
        income = self._Worker__income
        print(f'Общий доход: {int(income.get("wage")) + int(income.get("bonuse"))}')

Ivan = Position("Ivan", "Ivanovich", "Worker", 20000, 5000)
Ivan.get_full_name()
Ivan.get_total_income()