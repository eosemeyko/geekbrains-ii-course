class Complex:
    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b else 0

    def __repr__(self):
        return 'Complex({}, {})'.format(self.a, self.b)

    def __str__(self):
        return f'Complex({self.a} + {self.b}j)'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(
                self.a + other.a, self.b + other.b
            )

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(
                (self.a * other.a) - (self.b * other.b),
                (self.a * other.b) + (self.b * other.a)
            )


num1 = Complex(5)
print(num1)

num2 = Complex(2)
print(num2)

num3 = Complex(5, 2)
print(num3)

print('\nСложение комплексных чисел')
print(num1 + num2)
print(num3 + num2)
print(num3 + num3)

print('\nУмножение комплексных чисел')
print(num1 * num2)
print(num3 * num2)
print(num3 * num3)
