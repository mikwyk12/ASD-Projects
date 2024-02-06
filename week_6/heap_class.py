class HeapElement:
    def __init__(self, data=None, priority=None):
        self.__data = data
        self.__priority = priority

    def __str__(self):
        return str(self.__priority) + ":" + str(self.__data)

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority


class Heap:
    def __init__(self):
        self.tab = []
        self.size = 0

    def is_empty(self):
        return True if self.size == 0 else False

    def peek(self):
        return self.tab[0]

    def enqueue(self, new_elem):
        self.tab.append(new_elem)
        self.size += 1
        index = self.size - 1
        par_index = self.parent(index)

        while index and self.tab[index] > self.tab[par_index]:
            self.tab[index], self.tab[par_index] = self.tab[par_index], self.tab[index]
            index = par_index
            par_index = self.parent(par_index)

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.size == 1:
            self.size -= 1
            return self.peek()
        else:
            temp = self.peek()
            self.tab[0] = self.tab[self.size-1]
            self.tab[self.size-1] = temp
            result = self.tab.pop()
            self.size -= 1
            el = self.tab[0]
            el_index = 0
            next_index = 0
            right = self.right(next_index)
            left = self.left(next_index)
            if left is None:
                return result
            elif right is None:
                next_index = left
            elif self.tab[right] > self.tab[left]:
                next_index = right
            else:
                next_index = left
            if next_index is not None:
                while el < self.tab[next_index]:
                    self.tab[el_index] = self.tab[next_index]
                    self.tab[next_index] = el
                    el_index = next_index
                    right = self.right(next_index)
                    left = self.left(next_index)
                    if left is None:
                        return result
                    elif right is None:
                        next_index = left
                    elif self.tab[right] > self.tab[left]:
                        next_index = right
                    else:
                        next_index = left
                    if next_index is None:
                        return result
            return result

    def parent(self, index):
        return (index-1)//2

    def left(self, index):
        result = 2*index + 1
        return result if result <= self.size - 1 else None

    def right(self, index):
        result = 2*index + 2
        return result if result <= self.size - 1 else None

    def print_tab(self):
        if self.size == 0:
            print("{}")
        else:
            print('{', end='')
            for i in range(self.size - 1):
                print(self.tab[i], end=', ')
            if self.tab[self.size - 1]:
                print(self.tab[self.size - 1], end='')
            print('}')

    def print_tree(self, idx, lvl):
        if self.size == 0:
            print("{}")
        elif idx is not None:
            if idx < self.size:
                self.print_tree(self.right(idx), lvl + 1)
                print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
                self.print_tree(self.left(idx), lvl + 1)
