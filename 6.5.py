class Stationery:

    title = "TITLE"

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой.")

class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом.")

class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером.")

Stationery().draw()
Pen().draw()
Pencil().draw()
Handle().draw()