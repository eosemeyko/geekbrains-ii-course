class Cell:
    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError('num > 0')
            self.num = int(num)
        except TypeError:
            self.num = 1
            print('Error type num')
        except ValueError:
            self.num = 1
            print('Error value num')

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Sub is impossible!')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)


cell1 = Cell(25)
print(cell1.make_order(15), '\n')

cell2 = Cell(10)
print(cell2.make_order(7), '\n')

cell3 = cell2 * cell1
print(cell3.make_order(34))
