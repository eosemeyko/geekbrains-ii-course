from abc import ABC, abstractmethod


ROUND_AMOUNT = 2


class Cloth(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Cloth):
    @property
    def fabric_consumption(self):
        return round(self.param / 6.5 + 0.5, ROUND_AMOUNT)


class Costume(Cloth):
    @property
    def fabric_consumption(self):
        return round(self.param * 2 + 0.3, ROUND_AMOUNT)


coat = Coat(36)
print('Пальто расход ткани: %s' % coat.fabric_consumption)

costume = Costume(1.64)
print('Костюм расход ткани: %s' % costume.fabric_consumption)

print(f'Общий расход ткани {round(coat.fabric_consumption + costume.fabric_consumption, ROUND_AMOUNT)}')
