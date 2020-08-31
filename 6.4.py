import random

class Car:

    def __init__(self, speed, color, name):
        global cars_speed

        self.speed = speed
        self.color = color
        self.name = name

        cars_speed.append(self.speed)

    def go(self):
        print(f"Машина под названием {self.name} отправилась в путь!")

    def turn(self, direction):
        print(f"Следующий пункт назначения - {direction}!")

    def stop(self):
        print(f"Машина под названием {self.name} приехала на место!")

    def show_speed(self):
        print(f"Скорость машины: {self.speed}км/час")

class TownCar(Car):

    is_police = False

    def show_speed(self):
        global pursued_cars

        if self.speed <= 60:
            print(f"Скорость машины: {self.speed}км/час")
        else:
            print(f"{self.speed}км/час - это слишком быстро!")
            if self not in pursued_cars:
                print(f"Отныне машину {self.name} будут преследовать!")
                pursued_cars.append(self)

class WorkCar(Car):

    is_police = False

    def show_speed(self):
        global pursued_cars

        if self.speed <= 40:
            print(f"Скорость машины: {self.speed}км/час")
        else:
            print(f"{self.speed}км/час - это слишком быстро!")
            if self not in pursued_cars:
                print(f"Отныне машину {self.name} будут преследовать!")
                pursued_cars.append(self)

class SportCar(Car):

    is_police = False

    def pont(self):
        self.speed = max(cars_speed) + 10
        cars_speed.append(self.speed)
        print(f"{self.name} обгоняет все машины на своём пути, просто потому, то может!")
        self.show_speed()

    def show_speed(self):
        global pursued_cars

        if self.speed <= 100:
            print(f"Скорость машины: {self.speed}км/час")
        else:
            print(f"{self.speed}км/час - это слишком быстро!")
            if self not in pursued_cars:
                print(f"Отныне машину {self.name} будут преследовать!")
                pursued_cars.append(self)

class PoliceCar(Car):

    is_police = True
    max = 70

    def pursue(self):
        global pursued_cars
        pursued_car = random.choice(pursued_cars)

        print(f"Полицейская машина {self.name} наконец начала делать что-то полезное, и отправилась в погоню за ближайшим преступником!")
        print(f"Преследуемая машина: {pursued_car.name}!")
        while True:
            self.speed = int(input("Впишите скорость, с которой бравые полицейские выполняют свои обязанности!"))
            if self.speed < pursued_car.speed:
                print("Медленно! Преследуемая машина начинает отдалятся!")
            elif self.speed == pursued_car.speed:
                print("Полиция едет наравне с преступником!")
            else:
                print("Успех! Преступник пойман и наказан!")
                pursued_cars.remove(pursued_car)
                break

    def show_speed(self):

        if self.speed <= 100:
            print(f"Скорость машины: {self.speed}км/час")
        else:
            print(f"{self.speed}км/час - это слишком быстро!")
            print(f"Но {self.name} полицейская машина, так что ей закон неписан!")

    pass

cars_speed = []
pursued_cars = []
places = ["Home", "Job", "SomeWhere", "NoWhere", "BigRoad"]

TCar = TownCar(50, "red", "GPS")
WCar = WorkCar(60, "blue", "SGP")
S_1Car = SportCar(90, "green", "CoolCar")
S_2Car = SportCar(101, "orange", "NitroCar")
PCar = PoliceCar(110, "white", "BigBossCar")

for i in [TCar, WCar, S_1Car, S_2Car, PCar]:
    i.go()
    i.show_speed()
    i.turn(random.choice(places))

TCar.stop()
WCar.stop()

for i in range(3):
    for j in [S_1Car, S_2Car]:
        j.pont()

while len(pursued_cars) != 0:
    print(f"Преследуемые машины: {', '.join(map(lambda x: x.name, pursued_cars))}")
    PCar.pursue()

print("Все нарушители пойманы, а все добропорядочные люди добрались до своих целей!")
print("Конец пьессы")