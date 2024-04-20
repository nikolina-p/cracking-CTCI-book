"""
Binary tree class with insert, find and delete methods
the data can be of any type, not just int, so functionality is developed on that assumption
"""
from treeprint import tree_print
from random import randint


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root

        parents = [self.root]
        while True:
            _ = []
            for parent in parents:
                if not parent.left:
                    parent.left = Node(data)
                    return parent.left
                else:
                    _.append(parent.left)

                if not parent.right:
                    parent.right = Node(data)
                    return parent.right
                else:
                    _.append(parent.right)
            parents = _

    def find(self, data):
        # do the level-order traversal
        if self.root is None:
            return None

        if self.root.data == data:
            return self.root

        parents = [self.root]
        while True:
            _ = []
            for parent in parents:
                if parent.left:
                    if parent.left.data == data:
                        return parent.left
                    else:
                        _.append(parent.left)
                if parent.right:
                    if parent.right.data == data:
                        return parent.right
                    else:
                        _.append(parent.right)
            if all(x is None for x in parents):
                return None
            parents = _

    def __find_node_and_parent(self, data, current: Node = None, parent: Node = None):
        # do the pre-order traversal
        if self.root is None:
            return None, None

        if self.root.data == data:
            return self.root, None

        if not current:
            current = self.root

        if not parent:
            parent = self.root

        if current.data == data:
            return current, parent

        parent = current

        if current.left:
            left_node, left_parent = self.__find_node_and_parent(data, current.left, parent)
            if left_node:
                return left_node, left_parent

        if current.right:
            right_node, right_parent = self.__find_node_and_parent(data, current.right, parent)
            if right_node:
                return right_node, right_parent

        return None, None

    def delete(self, data):
        # find the node, while also keeping the reference to its parent
        # find a leaf under the deleted node and put it in the place of deleted node
        # assumption: it is "just" binary tree, there are no requirements for tree structure or order of nodes

        del_node, del_parent = self.__find_node_and_parent(data)

        if del_node is None:
            return

        # if the node to be deleted is leaf
        if del_node.left is None and del_node.right is None:
            if del_parent.left == del_node:
                del_parent.left = None
            else:
                del_parent.right = None
            del del_node
            return

        # find a leaf - right(could be left also) descendant that has no left or right children
        leaf = del_node
        while True:
            while leaf.right:
                leaf_parent = leaf
                leaf = leaf.right

            # check if "right leaf" has left children
            while leaf.left:
                leaf_parent = leaf
                leaf = leaf.left

            if leaf.left is None:
                break

        # break parent-child relationship of the leaf
        if leaf_parent.left == leaf:
            leaf_parent.left = None
        else:
            leaf_parent.right = None

        # check if the node to be deleted is root (no parent node)
        if not del_parent:
            self.root = leaf
        else:
            # make leaf a child of a del_parent (left or right)
            if del_parent.left == del_node:
                del_parent.left = leaf
            else:
                del_parent.right = leaf

        # add del_node's children to leaf
        leaf.left = del_node.left
        leaf.right = del_node.right

        del del_node

    def __get_depth(self):
        # do the level-order traversal
        if not self.root:
            return 0

        current = self.root
        parents = [current]
        counter = 1
        while parents:
            _ = []
            for node in parents:
                if node.left:
                    _.append(node.left)
                if node.right:
                    _.append(node.right)
            if _:
                counter += 1
            parents = _

        return counter

    def __get_size(self, current: Node = None, counter=None):
        # return number of nodes in the tree
        # in-order traversal
        if not self.root:
            return 0

        if not current:
            current = self.root

        if not counter:
            counter = [0]

        if current.left:
            self.__get_size(current.left, counter)

        counter[0] += 1

        if current.right:
            self.__get_size(current.right, counter)

        return counter[0]


if __name__ == "__main__":
    # insert() test
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bt = BinaryTree()
    for v in values:
        bt.insert(v)

    tree_print(bt.root)

    # find() test
    x = 17
    node = bt.find(x)
    print(f"FIND {x}: ", node)

    # delete() test
    bt.delete(3)
    tree_print(bt.root)
