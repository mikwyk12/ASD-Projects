def realloc(tab, size):
    old_size = len(tab)
    return [tab[i] if i < old_size else None for i in range(size)]


class Queue:
    def __init__(self, size=5):
        self.size = size
        self.tab = [None for _ in range(size)]
        self.front = 0
        self.back = 0

    def __str__(self):
        if not self.is_empty:
            txt = '['
            if self.front < self.back:
                for i in range(self.front, self.back):
                    if self.tab[i] is not None:
                        txt += str(self.tab[i]) + " "
            elif self.front > self.back:
                for j in range(self.front, self.size):
                    if self.tab[j] is not None:
                        txt += str(self.tab[j]) + " "
                for k in range(self.back):
                    if self.tab[k] is not None:
                        txt += str(self.tab[k]) + " "
            return txt[:-1] + "]"
        return "[]"

    def enqueue(self, other):
        self.tab[self.back] = other
        self.back += 1
        if self.back == self.size:
            self.back = 0
        if self.back == self.front:
            old_size = self.size
            self.size = old_size * 2
            self.tab = realloc(self.tab, self.size)
            last = self.size
            for i in range(self.front, old_size):
                i = old_size - i
                self.tab[last - 1] = self.tab[i]
                last -= 1
            self.front = last

    def dequeue(self):
        if not self.is_empty:
            result = self.peek
            self.front += 1
            if self.front == self.size:
                self.front = 0
            return result
        return None

    @property
    def is_empty(self):
        return True if self.front == self.back else False

    @property
    def peek(self):
        return self.tab[self.front]
