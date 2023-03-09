#!/usr/bin/python
# -*- coding: utf-8 -*-

class Matrix:
    def __init__(self, elem, par=0):
        if isinstance(elem, tuple):
            rows, cols = elem
            self.matrix = [[par for j in range(cols)] for i in range(rows)]
        else:
            self.matrix = elem

    def __add__(self, sec_matrix):
        if self.size() == sec_matrix.size():
            result = Matrix(self.size())
            row, col = self.size()
            for i in range(row):
                for j in range(col):
                    result[i][j] = self.matrix[i][j] + sec_matrix[i][j]
            return result
        else:
            print("Error! The dimensions are wrong!")

    def __mul__(self, sec_matrix):
        if self.size()[1] == sec_matrix.size()[0]:
            rows, cols = self.size()[0], sec_matrix.size()[1]
            result = Matrix((rows, cols))
            for row in range(rows):
                for col in range(cols):
                    for elem in range(sec_matrix.size()[0]):
                        result[row][col] += self.matrix[row][elem] * sec_matrix[elem][col]
            return result
        else:
            print("Error! The dimensions are wrong!")

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __str__(self):
        msg = ""
        row, col = self.size()
        for i in range(row):
            msg += '| '
            for j in range(col):
                msg += str(self.matrix[i][j]) + ' '
            msg += "|\n"
        return msg

    def size(self):
        return len(self.matrix), len(self.matrix[0])


def determinant_2x2(matrix: Matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]


def determinant_chio(coef: float, matrix: Matrix):
    if matrix.size() == (2, 2):
        return coef * determinant_2x2(matrix)
    if matrix[0][0] == 0:
        for i in range(matrix.size()[0]):
            if matrix[i][0] != 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
                coef *= -1
                break
    new_coef = coef * 1 / (matrix[0][0] ** (matrix.size()[0] - 2))

    reduced_matrix = []
    for i in range(matrix.size()[0] - 1):
        row = []
        for j in range(matrix.size()[0] - 1):
            row.append(determinant_2x2(Matrix([[matrix[0][0], matrix[0][j+1]],
                                               [matrix[i+1][0], matrix[i+1][j+1]]])))
        reduced_matrix.append(row)
    return determinant_chio(new_coef, Matrix(reduced_matrix))


def calculate_determinant(matrix: Matrix):
    if matrix.size() == (2, 2):
        return determinant_2x2(matrix)
    else:
        return determinant_chio(1., matrix)


def transpose(matrix: Matrix):
    rows, cols = matrix.size()
    result = Matrix((cols, rows))
    for row in range(rows):
        for col in range(cols):
            result[col][row] = matrix[row][col]
    return result


if __name__ == "__main__":
    m1 = Matrix([
        [5, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])
    m2 = Matrix([
        [0, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])
    print(calculate_determinant(m1))
    print(calculate_determinant(m2))
