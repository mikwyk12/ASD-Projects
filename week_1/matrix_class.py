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
