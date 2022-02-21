from task5 import (
    MovingOfficeEquipment as MovingOfficeEquipmentBase,
    Printer as PrinterBase, Scanner as ScannerBase, Xerox as XeroxBase
)


class MovingOfficeEquipment(MovingOfficeEquipmentBase):
    def moving_acceptance(self, brand: str, amount: int):
        if not isinstance(amount, int):
            raise ValueError('Acceptance amount only number')
        super().moving_acceptance(brand, amount)

    def moving_transfer(self, brand: str, amount: int, _to: str):
        if not isinstance(amount, int):
            raise ValueError('Transfer amount only number')
        if not isinstance(_to, str):
            raise ValueError('Transfer name company only string')
        super().moving_transfer(brand, amount, _to)


class Printer(PrinterBase, MovingOfficeEquipment):
    pass


class Scanner(ScannerBase, MovingOfficeEquipment):
    pass


class Xerox(XeroxBase, MovingOfficeEquipment):
    pass


if __name__ == '__main__':
    printer = Printer(50, ['SV-01', 'SV-02'])
    printer.moving_acceptance('Samsung', 9)
    printer.moving_transfer('Samsung', 2, 'OAO NewWorld')
    print(printer.moving_log)

    scanner = Scanner(10, "Gorilla Glass")
    scanner.moving_acceptance('Samsung', 18)
    print(scanner.moving_log)
