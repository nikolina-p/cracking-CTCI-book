"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

From the book: A binary search tree is a binary tree in which every node fits a specific ordering property: all left
descendents <= n < all right descendents.
"""

from random import randint


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, root: Node = None) -> None:
        self.root = root

    def insert(self, node: Node, parent: Node = None) -> None:
        if not node:
            return

        if not self.root:
            self.root = node
            return

        if not parent:
            parent = self.root

        if node.value <= parent.value:
            if parent.left is None:
                parent.left = node
                node.parent = parent
            else:
                self.insert(node, parent.left)

        if node.value > parent.value:
            if parent.right is None:
                parent.right = node
                node.parent = parent
            else:
                self.insert(node, parent.right)

    def tree_print(self):
        levels = self.in_level_traversal()
        for level in levels:
            print([node.value if isinstance(node, Node) else node for node in level])  # last level can contain str '-'

    def in_level_traversal(self, all_nodes: list = None, parents: list = None) -> list:
        """return list of levels, where level is a list containing nodes in that level;
        Nonexistent child is replaced with '-' sign for printing purposes"""
        if parents is None:
            parents = [self.root]

        if all_nodes is None:
            all_nodes = [parents]

        _ = []
        for parent in parents:
            if isinstance(parent, Node):
                if parent.left:
                    _.append(parent.left)
                else:
                    _.append("-")
                if parent.right:
                    _.append(parent.right)
                else:
                    _.append("-")
            else:
                _ += ['-', '-']
        parents = _

        if any(isinstance(item, Node) for item in parents):
            all_nodes.append(parents)
            self.in_level_traversal(all_nodes, parents)

        return all_nodes

    def __str__(self):
        return str(self.root.value)

    def get_min(self, node) -> Node:
        """return minimum element in the subtree under the node"""
        if not node.left:
            return node
        else:
            return self.get_min(node.left)

    def get_successor(self, node: Node):
        """returns successor node or None if node doesn't exist'"""
        if node.right:
            return self.get_min(node.right)

        if node.parent.value > node.value:
            return node.parent

        current = node.parent
        while current.value < node.value:
            if current.parent:
                current = current.parent
            else:
                return None

        return current


if __name__ == '__main__':
    tree = BinarySearchTree()
    values = [50, 25, 75, 10, 30, 60, 85, 29, 45, 55, 70, 80, 100, 39, 47, 72]
    nodes = []
    for i, val in enumerate(values):
        nodes.append(Node(val))
        tree.insert(nodes[i])

    tree.tree_print()

    node = nodes[5]
    successor = tree.get_successor(node)
    print(f"Node: {node.value}, successor: {successor.value if successor else None}")



