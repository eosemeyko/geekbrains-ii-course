class Road:
    def __init__(self, length: int, width: int):
        self.__length, self.__width = length, width

    def get_mass_asphalt(self, ration: float, web_thickness: float) -> float:
        return (self.__length * self.__width) * ration * web_thickness


asphalt_road = Road(20, 5000)

print(asphalt_road.get_mass_asphalt(25, 0.5))
