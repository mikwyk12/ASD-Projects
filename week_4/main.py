from hash_class import *


if __name__ == '__main__':
    keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15]
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    first_test(keys, values, 1, 0)
    second_test(values, 1, 0)
    second_test(values, 0, 1)
    first_test(keys, values, 0, 1)