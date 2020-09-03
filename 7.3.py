class Cell:

    def __init__(self, cells_amount):
        if 0 < int(cells_amount):
            self.cells_amount = int(cells_amount)
        else: raise TypeError

    def __add__(self, other):
        return Cell(self.cells_amount + other.cells_amount)

    def __sub__(self, other):
        result = self.cells_amount - other.cells_amount
        if 0 < result:
            return Cell(result)
        print("Ошибка! Результат меньше или равен нулю!")
        return None

    def __mul__(self, other):
        return Cell(self.cells_amount * other.cells_amount)

    def __truediv__(self, other):
        result = self.cells_amount // other.cells_amount
        if 0 < result:
            return Cell(result)
        print("Ошибка! Результат меньше или равен нулю!")
        return None

    def __str__(self):
        return str(self.cells_amount)

    def make_order(self, form):
        result = ""
        form = int(form)
        for i in range(self.cells_amount // form):
            result += "*" * form + "\n"
        if self.cells_amount % form != 0:
            result += "*" * (self.cells_amount % form) + "\n"
        return result[:-1:1]

cell_1 = Cell(10)
cell_2 = Cell(9)
print(cell_1+cell_2)
print(cell_1-cell_2)
print(cell_2-cell_1)
print(cell_1*cell_2)
print(cell_1/cell_2)
print(cell_2/cell_1)
print(cell_1.make_order(3))
print(cell_2.make_order(3))