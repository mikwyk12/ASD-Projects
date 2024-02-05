from tree_class import *


def test(obj: Tree) -> None:
    obj.print_tree()
    obj.print()
    print(f"\n{obj.search(24)}")
    obj.insert(20, "AA")
    obj.insert(6, "M")
    obj.delete(62)
    obj.insert(59, "N")
    obj.insert(100, "P")
    obj.delete(8)
    obj.delete(15)
    obj.insert(55, "R")
    obj.delete(50)
    obj.delete(5)
    obj.delete(24)
    print(obj.height())
    obj.print()
    obj.print_tree()


if __name__ == '__main__':
    nodes = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}

    tree = Tree()

    for key, value in nodes.items():
        tree.insert(key, value)

    test(tree)
