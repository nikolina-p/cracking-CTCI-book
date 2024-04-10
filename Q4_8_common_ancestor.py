"""
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
Assumption: You are given the tree root.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def enumerate(self, node1, node2, current=None, counter=None, index=None):
        """
        idea: do the inorder traversal, enumerate the tree nodes and return indexes of node1, node2 and root;
        index array keeps track of node1_index, node2_index, root_index
        """
        current = self.root if not current else current
        counter = [1] if not counter else counter
        index = [-1, -1, -1] if not index else index

        if current.left:
            self.enumerate(node1, node2, current.left, counter, index)

        if current == node1:
            index[0] = counter[0]
        if current == node2:
            index[1] = counter[0]
        if current == self.root:
            index[2] = counter[0]

        print(f"{counter} : {current.value}")
        counter[0] += 1

        if current.right:
            self.enumerate(node1, node2, current.right, counter, index)

        return index

    def find_common_ancestor(self, node1, node2, current=None):
        """idea: enumerate tree in in-order traversal
                if node1_index < root_index < node2_index: root is common acestor
                if node1_index  and node2_index < root_index: go to the left and do recursion
                if node1_index and node2_index > root_index: go to the right and do recursion
                if node1_index or node2_index == -1: node is not in the tree
                """
        try:
            current = self.root if not current else current
            index = self.enumerate(node1, node2, current)

            print(index)

            if index[0] == -1 or index[1] == -1 or index[2] == -1:
                raise IndexError("Node is not in the tree.")

            if index[0] < index[2] < index[1] or index[0] > index[2] > index[1]:
                return current

            if index[0] < index[2] and index[1] < index[2]:
                subtree = BinaryTree(current.left)
                return subtree.find_common_ancestor(node1, node2)

            if index[0] > index[2] and index[1] > index[2]:
                subtree = BinaryTree(current.right)
                return subtree.find_common_ancestor(node1, node2)
        except IndexError as err:
            print(err)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = h
    c.left = f
    c.right = g

    tree1 = BinaryTree(a)

    print("Common ancestor: ", tree1.find_common_ancestor(f, h).value)

    """
                a
            b          c
        d      e     f   g
              h
    """








