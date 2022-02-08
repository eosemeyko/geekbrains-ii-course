from typing import Tuple


class Data:
    _datetime = None

    def __init__(self, dt: str):
        self.format_to_int(dt)

    def __str__(self):
        return f'{self._datetime[0]}, {self._datetime[1]}, {self._datetime[2]}'

    @property
    def get_dt(self):
        return self._datetime

    @classmethod
    def format_to_int(cls, dt: str):
        cls._datetime = tuple(map(int, dt.split('-')))

    @staticmethod
    def validate_dt(dt: Tuple[int]):
        days_in_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
        }
        if not 1 <= dt[1] <= 12:
            return print('invalid month: 1-12')
        if not (0 < dt[0] <= days_in_month[dt[1]]):
            return print(f'invalid day: 1-{days_in_month[dt[1]]}')
        if not 1900 <= dt[2] <= 2035:
            return print('invalid year: 1900-2035')


if __name__ == '__main__':
    data = Data('07-05-2035')
    print(data)
    print(data.get_dt)
    data.validate_dt(data.get_dt)
