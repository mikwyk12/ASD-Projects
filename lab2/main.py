#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class List:
    def __init__(self):
        self.head = None

    def __get__(self):
        return self.head

    def destroy(self):
        self.head = None

    def add(self, other):
        elem = Node(other, self.head)
        self.head = elem

    def append(self, other):
        if self.is_empty():
            last = Node(other)
            self.head = last
        else:
            pointer = self.head
            last = None
            while pointer:
                last = pointer
                pointer = pointer.next
            elem = Node(other)
            last.next = elem

    def remove(self):
        self.head = self.head.next

    def remove_end(self):
        pointer = self.head.next
        last = None
        while pointer:
            last = pointer
            pointer = pointer.next
        last = None

    def is_empty(self):
        return True if (self.head is None) else False

    def length(self):
        if self.is_empty():
            return 0
        pointer = self.head
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    def print_list(self):
        pointer = self.head
        while pointer:
            print("-> " + pointer.data.__str__())
            pointer = pointer.next

if __name__ == "__main__":
    lst = [('AGH', 'Kraków', 1919),
           ('UJ', 'Kraków', 1364),
           ('PW', 'Warszawa', 1915),
           ('UW', 'Warszawa', 1915),
           ('UP', 'Poznań', 1919),
           ('PG', 'Gdańsk', 1945)]
    uczelnie = List()
    for i in range(3):
        uczelnie.append(lst.pop(0))

    for elem in lst:
        uczelnie.add(elem)

    uczelnie.print_list()
    print(uczelnie.length())

    uczelnie.remove()
    print(uczelnie.head)

    uczelnie.remove_end()
    uczelnie.print_list()
