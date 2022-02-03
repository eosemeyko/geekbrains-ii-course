from time import sleep


class TrafficLight:
    color_times = {'красный': 7, 'желтый': 2, 'зеленый': 9}

    def __init__(self, color: str):
        if color not in self.color_times.keys():
            raise ValueError('Такой цвет не найден!')
        self.__color = color

    def running(self):
        while True:
            print(f'Current traffic light: {self.__color}')
            sleep(self.color_times[self.__color])
            if self.__color == 'красный':
                self.__color = 'желтый'
            elif self.__color == 'желтый':
                self.__color = 'зеленый'
            elif self.__color == 'зеленый':
                self.__color = 'красный'


traffic_light = TrafficLight('зеленый')
traffic_light.running()
