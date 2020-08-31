class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")
        print(self.title)

class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой.")
        print(f"\033[34m{self.title}\033[0m")

class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом.")
        print(f"\033[31m{self.title}\033[0m")

class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером.")
        print(f"\033[30m{self.title.upper()}\033[0m")

Stationery("Просто текст").draw()
Pen("Синяя ручка").draw()
Pencil("Красный карандаш").draw()
Handle("Жирнющий маркер").draw()