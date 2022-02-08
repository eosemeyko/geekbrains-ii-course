class Warehouse:
    __sector_name = 'B1'

    def __init__(self):
        print(f'Техника находится на складе {self.__sector_name}')


class OfficeEquipment(Warehouse):
    __brands = ['Samsung', 'Apple']
    _boxes = 100
    _box_width = 60
    _box_height = 60

    def __init__(self):
        super().__init__()
        print(f'Оргтехника брендов {", ".join(self.__brands)}')
        print(f'{self.__class__.__name__} на складе: {self._boxes} шт.')
        print(f'Размеры коробок: {self._box_width}x{self._box_height}')

    @property
    def get_brands(self):
        return self.__brands

    @property
    def get_boxes_count(self):
        return self._boxes


class Printer(OfficeEquipment):
    _box_width = 50
    _box_height = 40

    def __init__(self, _counts: int, cartridges: list):
        self._boxes = _counts
        super().__init__()
        print(f'Картриджи: {", ".join(cartridges)}')


class Scanner(OfficeEquipment):
    _box_width = 40
    _box_height = 10

    def __init__(self, _counts: int, glass: str):
        self._boxes = _counts
        super().__init__()
        print(f'Модель стекла: {glass}')


class Xerox(OfficeEquipment):
    _box_width = 70

    def __init__(self, _counts: int, paper: int):
        self._boxes = _counts
        super().__init__()
        print(f'Бумаги для ксерокса: {paper}')


if __name__ == '__main__':
    printers = Printer(50, ['SV-01', 'SV-02'])
    # print(printers.get_brands)
    # print(printers.get_boxes_count)
    print('\n')

    scanners = Scanner(10, "Gorilla Glass")
    print('\n')

    xerox = Xerox(5, 18)
    print('\n')
