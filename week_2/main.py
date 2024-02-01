from list_class import *


def single_list_process(data):
    single_list = List()

    for i in range(3):
        single_list.append(data[i])

    for elem in data:
        single_list.add(elem)

    single_list.print()
    print('Number of elements: ', single_list.length)
    single_list.remove()
    print('Head: ', single_list.head)
    single_list.remove_end()
    single_list.print()
    single_list.destroy()
    print('Is Single List empty?: ', single_list.is_empty)
    single_list.remove()
    single_list.append(data[0])
    single_list.remove_end()
    print('Is Single List empty?: ', single_list.is_empty)
    single_list.print()


def double_list_process(data):
    double_list = DoubleList()

    for i in range(3):
        double_list.append(data[i])

    for elem in data:
        double_list.add(elem)

    double_list.print()
    print('Number of elements: ', double_list.length)
    double_list.remove()
    print('Head: ', double_list.head)
    double_list.remove_end()
    double_list.print()
    double_list.destroy()
    print('Is Double List empty?: ', double_list.is_empty)
    double_list.remove()
    double_list.append(data[0])
    double_list.remove_end()
    print('Is Double List empty?: ', double_list.is_empty)
    double_list.print()


if __name__ == '__main__':
    universities = [('AGH', 'Kraków', 1919),
                    ('UJ', 'Kraków', 1364),
                    ('PW', 'Warszawa', 1915),
                    ('UW', 'Warszawa', 1915),
                    ('UP', 'Poznań', 1919),
                    ('PG', 'Gdańsk', 1945)]
    print("1. Single Linked List")
    single_list_process(universities)

    print("\n2. Doubled Linked List")
    double_list_process(universities)
