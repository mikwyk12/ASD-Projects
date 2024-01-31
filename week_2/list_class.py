class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class List:
    def __init__(self, head=None):
        self.head = head

    def destroy(self):
        self.head = None

    def add(self, other):
        new_node = Node(other, self.head)
        self.head = new_node

    def append(self, other):
        if self.is_empty:
            self.add(other)
        else:
            pointer = self.head
            last = None
            while pointer:
                last = pointer
                pointer = pointer.next
            new_node = Node(other)
            last.next = new_node

    def remove(self):
        if not self.is_empty:
            self.head = self.head.next

    def remove_end(self):
        if not self.is_empty:
            if self.length == 1:
                self.destroy()
            else:
                pointer = self.head
                last = self.head

                while pointer.next:
                    last = pointer
                    pointer = pointer.next

                last.next = None

    def print(self):
        pointer = self.head

        while pointer:
            print(pointer)
            pointer = pointer.next
        pass

    @property
    def is_empty(self):
        return True if self.head is None else False

    @property
    def length(self):
        if self.is_empty:
            return 0
        else:
            pointer = self.head
            counter = 0
            while pointer:
                counter += 1
                pointer = pointer.next
            return counter

    @property
    def get(self):
        return self.head.data
