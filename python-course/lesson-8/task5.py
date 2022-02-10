from task4 import (
    OfficeEquipment,
    Printer as PrinterBase, Scanner as ScannerBase, Xerox as XeroxBase
)


class BrandError(Exception):
    pass


class MovingOfficeEquipment(OfficeEquipment):
    _moving_log = {}

    def check_brand(self, brand: str):
        # Проверка наличия разрешенных брендов
        if brand not in self.get_brands:
            raise BrandError('Такого бренда нет в базе склада')
        if not self._moving_log.get(brand):
            self._moving_log[brand] = {}

    def __get_moving_brand_log(self, brand: str):
        return self._moving_log.get(brand, {})

    def __get_moving_log(self, brand: str):
        brand_log = self.__get_moving_brand_log(brand)
        return brand_log.get(self.__class__.__name__, {})

    def __set_moving_log(self, brand: str, data: dict):
        _log = self.__get_moving_log(brand)
        _log.update(data)
        self._moving_log[brand][self.__class__.__name__] = _log

    def moving_acceptance(self, brand: str, amount: int):
        # Принятие на склад
        self.check_brand(brand)
        self._boxes += amount
        _log = self.__get_moving_log(brand)
        _log['acceptance_amount'] = amount
        self.__set_moving_log(brand, _log)
        print(f'{self.__class__.__name__} принято на склад в количестве {amount} ед.')
        print(f'Изменения наличия на складе {self.get_boxes_count} ед.')

    def moving_transfer(self, brand: str, amount: int, _to: str):
        # Передача со склада
        self.check_brand(brand)
        if amount > self._boxes:
            return print(f'!!! Количество передачи превышает наличие на складе! Отмена')
        self._boxes -= amount
        _log = self.__get_moving_log(brand)
        _log['transfer_count'] = amount
        _log['transfer_to'] = _to
        self.__set_moving_log(brand, _log)
        print(f'{self.__class__.__name__} передано: {_to} в количестве {amount} ед.')
        print(f'Изменение наличия на складе {self.get_boxes_count} ед.')

    @property
    def moving_log(self):
        return self._moving_log


class Printer(PrinterBase, MovingOfficeEquipment):
    pass


class Scanner(ScannerBase, MovingOfficeEquipment):
    pass


class Xerox(XeroxBase, MovingOfficeEquipment):
    pass


if __name__ == '__main__':
    printer = Printer(50, ['SV-01', 'SV-02'])
    printer.moving_acceptance('Samsung', 12)
    printer.moving_transfer('Apple', 7, 'OOO Compass')
    printer.moving_transfer('Samsung', 2, 'OAO NewWorld')
    printer.moving_acceptance('Apple', 15)
    print(printer.moving_log)

    xerox = Xerox(13, 18)
    xerox.moving_acceptance('Samsung', 2)
    xerox.moving_transfer('Apple', 9, 'OOO ReStore')
    print(xerox.moving_log)
