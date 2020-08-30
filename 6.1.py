import time
import itertools


class TrafficLight:

    def __init__(self, __color):
        self.__color = __color
        for __color in next(itertools.cycle("rygy")):
            TrafficLight.running(self, __color)

    def running(self, __color):
        color_dict = {"r": 7, "y": 2, "g": 7}
        print(__color)
        time.sleep(color_dict.get(__color))

for color in next(itertools.cycle("rygy")):
    TrafficLight(color)