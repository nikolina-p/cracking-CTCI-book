"""
4.9. BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
"""

from treeprint import tree_print


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self, root: Node = None):
        self.root = root

    def insert_array(self, array):
        if self.root is None:
            self.root = Node(array[0])

        for n in array[1:]:
            current = self.root
            previous = None
            while current:    # find leaf node where to insert n (previous)
                previous = current
                if current.data < n:
                    current = current.right
                elif current.data > n:
                    current = current.left

            # set Node(n) as a child of previous
            if previous.data < n:
                previous.right = Node(n)
            else:
                previous.left = Node(n)

    def tree_size(self, current: Node = None, count: list = None) -> int:
        """return number of nodes in the tree"""
        if self.root is None:
            return 0

        current = self.root if not current else current

        count = [0] if not count else count

        if current.left:
            self.tree_size(current.left, count)

        count[0] += 1

        if current.right:
            self.tree_size(current.right, count)

        return count[0]

    def permutate_tree(self, result=None, possible_next=None, temp_order: list = None, size: int = None):
        if self.root is None:
            return []

        if size is None:
            size = self.tree_size()

        if result is None:
            result = []

        # when initialized like this, python is making a copy of result in each recursion call
        # ...and method is always returning empty array []
        #result = result if result else []
        #result = [] if not result else result

        if temp_order is None:
            temp_order = [self.root.data]

        # initialize list of possible next nodes(values) in result array
        if possible_next is None:
            possible_next = []
            if self.root.left:
                possible_next.append(self.root.left)
            if self.root.right:
                possible_next.append(self.root.right)
            if not possible_next:   # root has no children
                return result

        # start recursive call for each node
        for node in possible_next:
            temp = temp_order[:]
            temp.append(node.data)

            # possible_next.remove(node)
            _ = possible_next[:]  # make copy of possible_next to put in recursion for current node
            _.remove(node)
            # add chldren of current node to possible_next array
            if node.left:
                _.append(node.left)
            if node.right:
                _.append(node.right)

            if _:
                self.permutate_tree(result, _, temp, size)

            if len(temp) == size:
                result.append(temp)

        return result

    def array_permutation(self, arr=None, result=None, temp_order: list = None, size: int = None):
        if arr is None:
            return arr

        if result is None:
            result = []

        if temp_order is None:
            temp_order = []

        size = size if size else len(arr)

        for i, val in enumerate(arr):
            _ = temp_order[:]
            _.append(val)
            rest_of_arr = arr[:]
            rest_of_arr.remove(val)
            self.array_permutation(rest_of_arr, result, _, size)

            if len(_) == size:
                result.append(_)

        return result


if __name__ == "__main__":
    tree = BinarySearchTree()
    #a = [8, 10, 5]
    a = [8, 10, 5, 3, 6, 9, 23]

    # CREATE A TEST TREE FROM AN ARRAY AND PRINT TREE
    tree.insert_array(a)
    tree_print(tree.root)

    permutations = tree.permutate_tree()
    for permutation in permutations:
        print(permutation)

    print("There are {} permutations.".format(len(permutations)))

"""
OUTPUT:

 8        
    /        \    
    5        10    
  /    \    /    \  
  3    6    9    23  
[8, 5, 10, 3, 6, 9, 23]
[8, 5, 10, 3, 6, 23, 9]
[8, 5, 10, 3, 9, 6, 23]
[8, 5, 10, 3, 9, 23, 6]
    ...
    ...
    ...
[8, 10, 23, 5, 6, 3, 9]
[8, 10, 23, 9, 5, 3, 6]
[8, 10, 23, 9, 5, 6, 3]
There are 80 permutations.

"""
