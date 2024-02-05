class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def search(self, key):
        def int_search(node, in_key):
            if node is not None:
                if node.key < in_key:
                    return int_search(node.right, in_key)
                elif node.key > in_key:
                    return int_search(node.left, in_key)
                else:
                    return node.value

            return None

        return int_search(self.root, key)

    def insert(self, key, value) -> None:
        def int_insert(node, in_key, in_value):
            if in_key < node.key:
                if node.left is None:
                    node.left = Node(in_key, in_value)
                else:
                    int_insert(node.left, in_key, in_value)
            elif in_key > node.key:
                if node.right is None:
                    node.right = Node(in_key, in_value)
                else:
                    int_insert(node.right, in_key, in_value)
            else:
                node.value = in_value

        if self.root is None:
            self.root = Node(key, value)
        else:
            int_insert(self.root, key, value)

    def delete(self, key):
        def int_delete(node, in_key):
            if in_key < node.key:
                node.left = int_delete(node.left, in_key)
            elif in_key > node.key:
                node.right = int_delete(node.right, in_key)
            else:
                if node.left is None:
                    temp = node.right
                    return temp
                elif node.right is None:
                    temp = node.left
                    return temp

                temp = node.right
                while temp.left is not None:
                    temp = temp.left

                node.key = temp.key
                node.data = temp.value

                node.right = int_delete(node.right, temp.key)

            return node

        current = self.root

        if current is not None:
            return int_delete(current, key)
        return None

    def print(self):
        return self.__print(self.root)

    def __print(self, cur_node):
        if cur_node.left:
            self.__print(cur_node.left)
        print(f"{cur_node.key} {cur_node.value}", end=', ')
        if cur_node.right:
            self.__print(cur_node.right)

    def print_tree(self):
        print("\n============================")
        self.__print_tree(self.root, 0)
        print("============================")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)

            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left, lvl + 5)

    def height(self):
        def int_height(node):
            if node is None:
                return 0
            left_ans = int_height(node.left)
            right_ans = int_height(node.right)

            return max(left_ans, right_ans) + 1

        return int_height(self.root)
