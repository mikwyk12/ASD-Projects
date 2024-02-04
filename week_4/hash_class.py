class HashElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def is_key_equal(self, key):
        return True if self.key == key else False


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash_fun(self, elem):
        result = elem
        if isinstance(elem, str):
            result = 0
            for i in elem:
                result += ord(i)
        return result % self.size

    def search_index(self, key):
        index = self.hash_fun(key)
        element = self.tab[index]
        if element is not None:
            if (element.key is not None) and (element.is_key_equal(key)):
                return index
            new_index = self.solve_col_search(index, key)
            return new_index
        return None

    def search(self, key):
        index = self.search_index(key)
        if index is not None:
            return self.tab[index].value

    def insert(self, key, data):
        index = self.hash_fun(key)
        if (self.tab[index] is None) or (self.tab[index].key is None) or (self.tab[index].is_key_equal(key)):
            self.tab[index] = HashElement(key, data)
        else:
            new_index = self.solve_col_insert(index, key)
            if new_index is None:
                raise MemoryError
            else:
                self.tab[new_index] = HashElement(key, data)

    def remove(self, key):
        index = self.search_index(key)
        if index is not None:
            self.tab[index].key = None
        else:
            raise ValueError

    def solve_col_search(self, index, key):
        for i in range(1, self.size + 1):
            new_index = (index + (self.c1 * i) + (self.c2 * i ** 2)) % self.size
            if self.tab[new_index] is None:
                return None
            elif (self.tab[new_index].key is not None) and (self.tab[new_index].is_key_equal(key)):
                return new_index
        return None

    def solve_col_insert(self, index, key):
        for i in range(1, self.size + 1):
            new_index = (index + (self.c1 * i) + (self.c2 * i**2)) % self.size
            if (self.tab[new_index] is None) or (self.tab[new_index].key is None) or (self.tab[new_index].is_key_equal(key)):
                return new_index
        return None

    def __str__(self):
        result = "["
        for i in range(self.size):
            if self.tab[i] is None:
                result += 'None, '
            else:
                result += '{' + str(self.tab[i].key) + ':' + str(self.tab[i].value) + '}' + ', '
        result = result[:-2] + "]"
        return result


def insert_fun(arr, key, data):
    try:
        arr.insert(key, data)
    except MemoryError:
        print("Out of space")


def remove_fun(arr, key):
    try:
        arr.remove(key)
    except ValueError:
        print("No data available")


def first_test(keys, values, c1, c2):
    array = HashTable(13, c1, c2)
    for i in range(15):
        insert_fun(array, keys[i], values[i])
    print(array)
    print(array.search(5))
    print(array.search(14))
    insert_fun(array, 5, 'Z')
    print(array.search(5))
    remove_fun(array, 5)
    print(array)
    print(array.search(31))
    insert_fun(array, "test", "W")
    print(array)


def second_test(values, c1, c2):
    my_second_list = HashTable(13, c1, c2)
    for i in range(13):
        insert_fun(my_second_list, 13 + (13 * i), values[i])
    print(my_second_list)
