import list_class

if __name__ == '__main__':
    universities = [('AGH', 'Kraków', 1919),
                    ('UJ', 'Kraków', 1364),
                    ('PW', 'Warszawa', 1915),
                    ('UW', 'Warszawa', 1915),
                    ('UP', 'Poznań', 1919),
                    ('PG', 'Gdańsk', 1945)]

    list = list_class.List()

    for i in range(3):
        list.append(universities[i])

    for elem in universities:
        list.add(elem)

    list.print()
    print('\n', list.length)
    list.remove()
    print('\n', list.head)
    list.remove_end()
    list.print()
    list.destroy()
    print('\n', list.is_empty)
    list.remove()
    list.append(universities[0])
    list.remove_end()
    print('\n', list.is_empty)
    list.print()
