from heap_class import *


def test(heap: Heap):
    heap.print_tree(0, 0)
    heap.print_tab()

    first = heap.dequeue()
    print(heap.peek())
    heap.print_tab()
    print(first)
    while not heap.is_empty():
        print(heap.dequeue())
    heap.print_tree(0, 0)


if __name__ == '__main__':
    priority = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    value = "GRYMOTYLA"

    heap = Heap()

    for i in range(len(priority)):
        elem = HeapElement(value[i], priority[i])
        heap.enqueue(elem)

    test(heap)
