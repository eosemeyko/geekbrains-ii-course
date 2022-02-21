class Car:
    warning_speed: int = 60

    def __init__(self, speed: int, color: str, name: str, is_police: bool = False):
        self.name, self.color, self.speed, self.is_police = name, color, speed, is_police

    def go(self):
        print(f'Car: {self.name}, color: {self.color}, drive at speed {self.speed}')
        if self.is_police:
            print('Police siren! уиу уиу уиу')

    def stop(self):
        print(f'Car: {self.name}, color: {self.color}, stopped')

    def turn(self, direction: str):
        print(f'Car: {self.name}, color: {self.color}, turn to {direction}')

    def show_speed(self):
        if not self.is_police and self.speed > self.warning_speed:
            print('Warning car speed!')
            self.stop()
        else:
            print(f'Car: {self.name}, color: {self.color}, speed {self.speed}')


class TownCar(Car):
    warning_speed = 60


class SportCar(Car):
    warning_speed = 90


class WorkCar(Car):
    warning_speed = 40


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, is_police=True)


# TownCar -> Bus
town_car = TownCar(60, 'blue', 'Bus')
town_car.go()
town_car.turn('right')
town_car.show_speed()
print('-----------')

# SportCar -> porsche 911
sport_cat = SportCar(120, 'red', 'Porsche 911')
sport_cat.go()
sport_cat.show_speed()
print('-----------')

# WorkCar -> gazel
work_car = WorkCar(30, 'white', 'Gazel')
work_car.go()
work_car.show_speed()
print('-----------')

# Police -> ford explorer
police = PoliceCar(100, 'black', 'Ford Explorer')
police.go()
police.turn('right')
police.show_speed()
