class Complex:

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    @classmethod
    def set_complex(cls, complex_num):
        real_part, imaginary_part = map(lambda x: int(x), complex_num.split(" i"))
        return cls(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real_part} i{self.imaginary_part}"

    def __add__(self, other):
        return Complex(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        return Complex(self.real_part * other.real_part - self.imaginary_part * other.imaginary_part,
                       self.real_part * other.imaginary_part + self.imaginary_part * other.real_part)

num_1 = Complex.set_complex("2 i1")
num_2 = Complex.set_complex("4 i10")
print(num_1)
print(num_1 + num_2)
print(num_1 * num_2)