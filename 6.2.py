class Road:

    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width
        Road.mass(self, self.__length, self.__width)

    def mass(self, length, wigth):
        print(f"Масса асфальта: {round(length*wigth*5*25/1000)}т")

Road(20, 5000)