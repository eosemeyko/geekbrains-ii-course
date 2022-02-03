class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self) -> str:
        return f'{self.surname} {self.name}'

    def get_total_income(self) -> float:
        return self._income['wage'] + self._income['bonus']


staff = Position('Петя', 'Петров', 'manager', 80000, 20000)
print('%s доход: %s' % (staff.get_full_name(), staff.get_total_income()))
