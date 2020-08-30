#у меня не было времени(

class Car:

    global chasing

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина под названием {self.name} отправилась в путь!")

    def stop(self):
        print(f"Машина под названием {self.name} остановилась!")

    def show_speed(self):
        print(f"Скорость машины: {self.speed}км/час")

    def turn(self, direction):
        print(f"Следующий пункт назначения - {direction}!")

class TownCar(Car):

    def show_speed(self):
        print(f"Скорость машины: {self.speed}км/час") if self.speed <= 60 else print(f"{self.speed}км/час - это слишком быстро!")

class WorkCar(Car):

    def show_speed(self):
        print(f"Скорость машины: {self.speed}км/час") if self.speed <= 40 else print(f"{self.speed}км/час - это слишком быстро!")

class SportCar(Car):

    def show_speed(self):
        print(f"Скорость машины: {self.speed}км/час") if self.speed <= 100 else print(
            f"{self.speed}км/час - это слишком быстро!")

class PoliceCar(Car):
    pass


TCar = TownCar(50, "red", "GPS", 0)
WCar = WorkCar(60, "blue", "SGP", 0)
SCar = SportCar(90, "green", "PFG", 0)
PCar = PoliceCar(50, "green", "PFG", 1)

for i in [TCar, WCar, SCar, PCar]:
    i.go()
    i.show_speed()
    i.turn("Работа")
    i.stop()