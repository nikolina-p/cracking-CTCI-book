"""
4.11 Random Node: You are implementing a binary tree class from scratch which, in addition to
i n s e r t , f i n d , and d e l e t e , has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.

My assumption: this is not a BST, data stored in nodes can be of any type, not necessarily integer
"""
from treeprint import tree_print
from random import randint


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1
        self.parent = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def __insert_node(self, data):
        """helper function to insert. Does in-level traversal and inserts the node on the first empty spot"""
        if self.root is None:
            self.root = Node(data)
            return self.root

        parents = [self.root]
        new = Node(data)
        while True:
            _ = []
            for parent in parents:
                if not parent.left:
                    parent.left = new
                    new.parent = parent
                    return new
                else:
                    _.append(parent.left)

                if not parent.right:
                    parent.right = new
                    new.parent = parent
                    return new
                else:
                    _.append(parent.right)
            parents = _

    def insert(self, data):
        """do the in-level traversal and insert the node on the first empty spot.
        Update size attribute of each parent node on the path from the root to the new node"""
        new = self.__insert_node(data)

        # update size of parent nodes on the path
        _ = new
        while _.parent is not None:
            _ = _.parent
            _.size += 1

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

    def __update_path(self, del_node):
        """helper method to delete(). Updates size attribute of elements on the path
        from deleted node to the root"""
        if del_node is None:
            return

        while del_node:
            del_node.size -= 1
            del_node = del_node.parent

    def delete(self, data):
        # find the node
        # find the leaf under the deleted node and put it in the place of deleted node
        # assumption: it is "just" a binary tree, there are no requirements for tree structure or order of nodes

        del_node = self.find(data)
        del_parent = del_node.parent

        if del_node is None:
            return

        # find the leaf
        leaf = del_node
        while True:
            while leaf.right:
                leaf = leaf.right

            # check if "right leaf" has left children
            while leaf.left:
                leaf = leaf.left

            if leaf.left is None and leaf.right is None:
                break

        # delete the node
        if del_node != leaf:
            # case when node to be deleted is not the leaf - do the swap, put the leaf on the place of deleted
            leaf.size = del_node.size
            # set parent -> child relationships
            if del_parent:
                if del_parent.left == del_node:
                    del_parent.left = leaf
                elif del_parent.right == del_node:
                    del_parent.right = leaf
            else:
                leaf.size = self.root.size
                self.root = leaf

            if leaf.parent:
                if leaf.parent.left == leaf:
                    leaf.parent.left = None
                elif leaf.parent.right == leaf:
                    leaf.parent.right = None

            leaf.left = del_node.left
            leaf.right = del_node.right

            self.__update_path(leaf)

            # set child -> parent relationships
            leaf.parent = del_parent

            if del_node.left:
                del_node.left.parent = leaf
            if del_node.right:
                del_node.right.parent = leaf
        else:
            # case when node to be deleted in leaf
            if del_parent:
                # if the node to be deleted is not root, delete parent relationship
                if del_parent.left == del_node:
                    del_parent.left = None
                else:
                    del_parent.right = None
            # update size up to the root
            self.__update_path(del_node)
            del del_node
            return

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

    def get_random_node(self, current: Node = None, n=None):
        # SOLUTION 1:
        # get a random number N (from 1 to size of the tree - number of nodes)
        # using size property of tree nodes, find Nth node in a tree and return it
        if self.root is None:
            return None

        if current is None:
            current = self.root

        if n is None:
            n = randint(1, self.root.size)

        if current.left:
            if n == current.left.size + 1:
                return current

            if n <= current.left.size:
                return self.get_random_node(current.left, n)
            else:
                if current.right:
                    return self.get_random_node(current.right, n - current.left.size - 1)
        else:
            if n == current.size:
                return current

            if current.right:
                return self.get_random_node(current.right, n - 1)

    def get_random_inorder(self, current: Node = None, n=None, counter=None):
        # SOLUTION 2:
        # get a random number n, and return the n-th element in inorder traversal
        if self.root is None:
            return None

        if not n:
            n = randint(1, self.__get_size())

        if not counter:
            counter = [0]

        if not current:
            current = self.root

        rand_node = None
        if current.left:
            rand_node = self.get_random_inorder(current.left, n, counter)

        # if didn't find in left subtree
        if rand_node is None:
            counter[0] += 1
            if counter[0] == n:
                return current

            # search right subtree
            if current.right:
                rand_node = self.get_random_inorder(current.right, n, counter)

        return rand_node


if __name__ == "__main__":
    # insert() test
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bt = BinaryTree()
    for v in values:
        bt.insert(v)

    tree_print(bt.root)

    # find() test
    """node = bt.find(9)
    print(node)"""

    # delete() test
    """
    print(bt.root.size)
    print(bt.root.left.size)
    print(bt.root.right.size)
    
    bt.delete(8)
    tree_print(bt.root)"""

    print("Root size: ", bt.root.size)
    print("Left size: ", bt.root.left.size)
    print("Right size: ", bt.root.right.size)

    print("RANDOM (solution 1): ", bt.get_random_node())
    print("RANDOM (solution 2): ", bt.get_random_inorder())
