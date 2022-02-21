class Matrix:
    __new_line = '\n'
    __error_msg = 'Please check matrix dimensions'

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        line = self.__new_line
        for row in self.matrix:
            for el in row:
                line += f'{el:>10}'
            line += self.__new_line
        return line

    def __add__(self, other):
        add = []
        if len(self.matrix) != len(other.matrix):
            return print(self.__error_msg)

        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return print(self.__error_msg)

            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            add.append(row)

        return Matrix(add)


mtx1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'my_m1 = {mtx1}')

mtx2 = Matrix([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(f'my_m2 = {mtx2}')

print(f'my_m1 + my_m2 = {mtx1 + mtx2}')
