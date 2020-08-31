class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self):
        print(f"Масса асфальта: {round(self._Road__length*self._Road__width*5*25/1000)}т")

Road(2000, 50).mass()