class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class DoubleNode(Node):
    def __init__(self, data, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev

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
        if not self.is_empty:
            print("Single List: ", end="")
            pointer = self.head

            while pointer.next:
                print(pointer, end=" -> ")
                pointer = pointer.next
            print(pointer)

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


class DoubleList(List):
    def __init__(self, head=None, tail=None):
        super().__init__(head)
        self.tail = tail

    def destroy(self):
        pointer = self.tail

        while pointer:
            last = pointer
            pointer.prev = None
            pointer = last.prev

        self.head = None

    def add(self, other):
        if self.is_empty:
            new_node = DoubleNode(other)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = DoubleNode(other, self.head)
            self.head.prev = new_node
            self.head = new_node

    def append(self, other):
        if self.is_empty:
            new_node = DoubleNode(other)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = DoubleNode(other, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if not self.is_empty:
            self.head.prev = None
            self.head = self.head.next

    def remove_end(self):
        if not self.is_empty:
            if self.length == 1:
                self.destroy()
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def print(self):
        if not self.is_empty:
            print("Double List: ", end="")
            pointer = self.head

            while pointer.next:
                print(pointer, end=" <-> ")
                pointer = pointer.next
            print(pointer)
