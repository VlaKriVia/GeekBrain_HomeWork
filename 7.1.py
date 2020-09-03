class Matrix:

    def __init__(self, matrix):
        for I in matrix:
            for i in I:
                if not str(i).isdecimal():
                    raise ValueError
        self.matrix = [[int(i) for i in I] for I in matrix]


    def __str__(self):
        out_put = ""
        #список длинн самых днинных цифр в каждой колонке для корректоного вывода
        len_list = [max([len(str(self.matrix[row][col])) for row in range(len(self.matrix)-1)]) for col in range(len(self.matrix)-1)]
        for i in self.matrix:
            for count, j in enumerate(i):
                out_put += f"|{j}{' ' * (len_list[count]-len(str(j)))}"
            out_put += "|\n"
        return out_put

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise IndexError
        if False in [len(A) == len(B) for A, B in [(self.matrix[c], other.matrix[c]) for c in range(len(self.matrix))]]:
            raise IndexError

        new_matrix = []
        for C in range(len(self.matrix)):
            i, j = self.matrix[C], other.matrix[C]
            new_matrix.append([i[c]+j[c] for c in range(len(i))])
        return Matrix(new_matrix)

#классы не должны работать с исключениями, только поднимать их, экранировать надо на этом уровне.
try:
    a = Matrix([["536", 567], [4354, "3"], [8, 9]])
    b = Matrix([[536, 567], [4354, 3], [8, 9]])
    print(a+b)
except IndexError:
    print("Матрицы разной длинны!")
except ValueError:
    print("Введена не матрица!")

try:
    a = Matrix([["536", 567], [4354, "3"]])
    b = Matrix([[536, 567], [4354, 3], [8, 9]])
    print(a+b)
except IndexError:
    print("Матрицы разной длинны!")
except ValueError:
    print("Введена не матрица!")

try:
    a = Matrix([["536", 567], [4354]])
    b = Matrix([[536, 567], [4354, 3], [8, 9]])
    print(a + b)
except IndexError:
    print("Матрицы разной длинны!")
except ValueError:
    print("Введена не матрица!")

try:
    a = Matrix([["536", 567], [4354, "3"], ["a", 9]])
    b = Matrix([[536, 567], [4354, 3], [8, 9]])
    print(a+b)
except IndexError:
   print("Матрицы разной длинны!")
except ValueError:
    print("Введена не матрица!")

try:
    a = Matrix([["536", 567], [4354, "3"], [8, 9]])
    b = Matrix([[536, 567], [4354, 3], [8, 9]])
    c = Matrix([[345, 56], [3, 10], [99, 678]])
    print(a+b+c)
except IndexError:
    print("Матрицы разного формата!")
except ValueError:
    print("Введена не матрица!")