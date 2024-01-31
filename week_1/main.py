from matrix_class import *


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
    # Basic Matrix
    m1 = Matrix([[1, 0, 2], [-1, 3, 1]])

    # Matrix Transpose
    print(transpose(m1))

    # Adding matrices
    m2 = Matrix((2, 3), 1)
    print(m1 + m2)

    # Multiplying matricies
    m3 = Matrix([[3, 1], [2, 1], [1, 0]])
    print(m1 * m3)

    # Chio Determinant
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
